from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models.functions import ExtractMonth
from django.db.models import Count, Sum
from .models import Ticket
from .serializers import TicketSerializers
from rest_framework.permissions import IsAuthenticated 

from .utils.list_to_dict import from_list_to_year_month_dict

# Create your views here.
class TicketViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated, ) 
    def list(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializers(tickets, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = TicketSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializers(ticket)
        return Response(serializer.data)

    def update(self, request, pk=None):
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializers(instance=ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        ticket = Ticket.objects.get(id=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def total_sale(self, request):
        response = ''
        try:
            method = request.query_params.get('method')
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            if method == "aggregation":
                response = self.__analytics_aggregation(start_date=start_date, end_date=end_date)
            elif method == 'algorithm': 
                response = self.__analytics_algorithm(start_date=start_date, end_date=end_date)
            else:
                response = {'error': 'incorrect method'}
        except Exception as e:
            response = {'error': str(e)}

        return Response(response)
    
    def __analytics_aggregation(self, start_date, end_date):
        sales = (Ticket.objects
                         .filter(performance_time__lte=end_date, performance_time__gte=start_date)
                         .values_list('performance_time__year', 'performance_time__month')
                         .annotate(Sum('price'))
                         .order_by('performance_time__year', 'performance_time__month'))
        visits = (Ticket.objects
                         .filter(performance_time__lte=end_date, performance_time__gte=start_date)
                         .values_list('performance_time__year', 'performance_time__month')
                         .annotate(Count('creation_date'))
                         .order_by('performance_time__year', 'performance_time__month'))

        sales_response = from_list_to_year_month_dict(sales)
        visits_response = from_list_to_year_month_dict(visits)

        return {'visits': visits_response, 'sales': sales_response}
    

    def __analytics_algorithm(self, start_date, end_date):
        tickets = (Ticket.objects
                         .filter(performance_time__lte=end_date, performance_time__gte=start_date)
                         .values('performance_time', 'price'))
        results = {}
        visits = {}
        for ticket in tickets:
            year = str(ticket.get('performance_time').strftime("%Y"))
            month = str(ticket.get('performance_time').strftime("%B"))
            if year in results.keys():
                if month in results[year].keys():
                    results[year][month] += ticket.get('price')
                    visits[year][month] += 1
                else:
                    results[year][month] = ticket.get('price')
                    visits[year][month] = 1
            else:
                results[year] = {}
                visits[year] = {}
                results[year][month] = ticket.get('price')
                visits[year][month] = 1
        return {'visits': visits, 'sales': results, }