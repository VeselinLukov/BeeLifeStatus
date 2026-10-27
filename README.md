BeeLifeStatus
Overview

BeeLifeStatus is a Django-based web application designed to manage apiaries, beehives, inspections, and tasks related to the health of an apiary.

The project provides a way to organize beekeeping activities by managing apiaries and their beehives, recording inspections, assigning tags to inspections, and maintaining task lists associated with each tag.

Features

Apiary Management
Create apiaries.
Edit existing apiaries.
Delete apiaries.

Beehive Management
Create beehives.
Edit existing beehives.
Delete beehives.

Inspection Management
Create inspections.
Edit existing inspections.
Delete inspections.

Inspection Tag Management
Create tags associated with an inspection.
Edit existing tags.
Delete tags.

Task List Management
Create task lists associated with each tag.
Edit existing task lists.
Delete task lists.

Technology Stack
Backend: Django
Database: SQLite
Programming Language: Python
Installation and Setup

The installation instructions will be completed once the project structure and dependency management configuration are confirmed.

Usage

BeeLifeStatus is intended to help beekeepers organize apiaries and beehives, manage inspections, and keep track of tasks related to apiary health.

The application supports the management of apiaries, beehives, inspections, inspection tags, and their associated task lists.

Project Structure

The project is organized into the following directories:

BeeLifeStatus/
├── apiaries/       # Apiary management
├── beehives/       # Beehive management
├── beelifestatus/  # Main Django project configuration
├── inspections/    # Inspection management
├── static/         # Static assets
├── tags/           # Inspection tag management
├── tasks/          # Task management
├── templates/      # HTML templates
├── manage.py       # Django management utility
└── requirements.txt


Requirements
Before running the application, make sure you have:
Python installed.
pip available for installing Python packages.
A terminal or command-line interface.

Installation and Setup

1. Clone the Repository
Clone the repository and navigate to the project directory:

bash
git clone <repository-url>
cd BeeLifeStatus
Replace <repository-url> with the actual repository URL.

2. Create a Virtual Environment

bash
python -m venv venv
Activate the virtual environment.
Windows:

bash
venv\Scripts\activate
Linux / macOS:

bash
source venv/bin/activate

3. Install Dependencies

bash
pip install -r requirements.txt

4. Configure Environment Variables

The project includes python-dotenv as a dependency. If the application uses environment variables, configure them according to the project's settings.
Do not commit secret keys, passwords, or other sensitive configuration values to version control.

5. Apply Database Migrations

bash
python manage.py migrate

6. Start the Development Server

bash
python manage.py runserver

Open the local development address shown in the terminal in your web browser.

Database

BeeLifeStatus uses SQLite as its database.
Django migrations are used to apply database schema changes.

Usage

Use the application to manage apiaries, beehives, inspections, inspection tags, and task lists associated with those tags.
The available operations include creating, editing, and deleting these records.

Academic Project
BeeLifeStatus is a university project focused on organizing apiary management and inspection-related tasks through a Django web application.

License

No license has been specified yet.
