# Development Setup

This document explains how to run the Coda project locally.

## Backend

The backend is built using Django.

Steps:

1. Navigate to the backend folder
2. Create a virtual environment
3. Install dependencies
4. Run the development server

### Create virtual environment

python -m venv .venv

### Activate environment

Windows:
.venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

### Start the server

python manage.py runserver