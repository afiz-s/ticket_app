from .views import TicketViewSet
from django.urls import path

urlpatterns = [
    path('tickets', TicketViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('tickets/<str:pk>', TicketViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('analytics', TicketViewSet.as_view({
        'get': 'total_sale',
    }))
]
