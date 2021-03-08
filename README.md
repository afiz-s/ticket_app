# Ticket Control Panel

Django REST Framework based backend for Ticket Control Panel. 

## Technical Stack
1. Python, Django, Django Rest Framework
2. Mysql for database
3. Docker for containerization
## Steps to run the application
1. Install Docker (>=20.10.2)
2. Install docker-compose (>=1.27.4)
3. Change working directory to `ticketcontrol` (`cd ticketcontrol`) 
4. Run `docker-compose up --build` 
5. That's it. REST API will be running at http://localhost:8000/api/tickets 

## Generating demo data
This project contains a script for generating demo data. https://github.com/afiz-s/ticket_app/blob/main/ticketcontrol/tickets/utils/fake_data_generator.py

This script can be executed from inside the backend container. 

## End points
1. List all the tickets: http://localhost:8000/api/tickets
2. Create a new ticket: http://localhost:8000/api/tickets (POST)
3. Update and Delete using http://localhost:8000/api/tickets/<id>
4. Analytics: http://localhost:8000/api/analytics?method=algorithm&start_date=2021-03-01&end_date=2022-03-31 or http://localhost:8000/api/analytics?method=aggregation&start_date=2021-03-01&end_date=2022-03-31

## screenshots