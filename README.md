![image](https://github.com/user-attachments/assets/cd98f738-9d7a-4669-a9d7-a0a1a9dbf439)
![image](https://github.com/user-attachments/assets/8b3f0daa-15d9-4f8e-a344-6f40b6cf3d28)
![image](https://github.com/user-attachments/assets/598526c1-a759-4d95-a912-d5244f746921)
![image](https://github.com/user-attachments/assets/09ad4fba-17d2-48fe-a9c2-30c9bfa3e779)
![image](https://github.com/user-attachments/assets/16e07462-50c2-4f13-9291-bb21a2bbe278)
Backend for Incident Reporting and Hauberge Management System
This backend provides robust REST APIs for two main systems:

Incident Reporting System:

Designed for managing and analyzing various types of incidents reported by users.
Handles traffic, environmental, and public transport-related reports.
Hauberge Management System:

Focused on accommodations management, including reservations, resident tracking, and blacklist enforcement.
Includes powerful analytics for decision-making.
Features
Incident Reporting System
Report Types:
Traffic Accidents
Road Damage
Public Transport Issues
Environmental Hazards
Traffic Flow Issues
Custom Data: Each report type has tailored fields for its specific data.
Permissions: User-based reporting and authentication using JWT.
Validation: Ensures completeness and correctness of report data.
Hauberge Management System
Accommodations:
Manage Hauberge (houses/camps) with real-time capacity tracking.
Reservations:
Prevent overlaps and handle cost calculations.
Resident Management:
Parental permission validation for minors.
Blacklist:
Ensures restricted access for specific individuals.
Technologies Used
Framework: Django Rest Framework (DRF)
Database: PostgreSQL (or SQLite for development)
Authentication: JWT (JSON Web Tokens)
API Documentation: Swagger and ReDoc
Installation
Prerequisites
Python: 3.9+
Database: PostgreSQL or SQLite
Steps
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd backend-system
Set Up the Backend:

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
Configure Environment Variables: Create a .env file:

env
Copy code
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/yourdbname
Apply Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser:

bash
Copy code
python manage.py createsuperuser
Run the Server:

bash
Copy code
python manage.py runserver
API Endpoints
Incident Reporting System
Traffic Accidents:

GET /api/traffic_accident_reports/
POST /api/traffic_accident_reports/
PUT /api/traffic_accident_reports/{id}/
DELETE /api/traffic_accident_reports/{id}/
Road Damage Reports:

GET /api/road_damage_reports/
POST /api/road_damage_reports/
Public Transport Issues:

GET /api/public_transport_issue_reports/
POST /api/public_transport_issue_reports/
Environmental Hazards:

GET /api/environmental_hazard_reports/
POST /api/environmental_hazard_reports/
Traffic Flow Issues:

GET /api/traffic_flow_issue_reports/
POST /api/traffic_flow_issue_reports/
Hauberge Management System
Hauberge:

GET /api/hauberges/
POST /api/hauberges/
Residents:

GET /api/residents/
POST /api/residents/
Reservations:

GET /api/reservations/
POST /api/reservations/
Blacklist:

GET /api/blacklist/
POST /api/blacklist/
Validation Rules
Incident Reporting
Traffic Accidents:
Severity and involved vehicle data must be provided.
Road Damage:
Validates damage type and size.
Public Transport Issues:
Requires affected line and transport type.
Environmental Hazards:
Ensures hazard type and area are specified.
Traffic Flow Issues:
Validates speed, direction, and estimated clear time.
Hauberge Management
Hauberge:
Automatically updates availability based on capacity.
Reservations:
Prevents overlapping bookings and invalid dates.
Residents:
Checks parental permission for minors.
Blacklist:
Validates unique identity entries.
Testing
Run Tests:

bash
Copy code
python manage.py test
Postman Collection: Use the provided Postman collection for testing API endpoints.

