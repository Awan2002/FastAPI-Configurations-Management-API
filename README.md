# FastAPI Configurations Management API

This project is a FastAPI-based API for managing configurations associated with countries. It uses SQLAlchemy for ORM (Object-Relational Mapping) and PostgreSQL as the database.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing with Postman](#testing-with-postman)

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Awan2002/FastAPI-Configurations-Management-API.git
2. **Create a virtual environment:**
    ```sh
    python -m venv venv
3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    or
    python3 -m pip install -r requirements.txt
## Configuration:

- Ensure PostgreSQL is running.
- Create a new database, e.g., db.
- Create a .env file and put your 
    ```sh 
    DATABASE_URL="postgresql://username:password@localhost/configurations_db"
- You can access this environment variable through
    ```sh
    from dotenv import load_dotenv
    load_dotenv()
    DATABASE_URL = os.getenv('DATABASE_URL')
- Configuration database.py

### Schema design

1. **Country:**
   ```sh
   id: Primary Key, Integer
   country_code: String, Unique (e.g., 'IN', 'US')
   country_name: String (e.g., 'India', 'United States')

2. **Configuration:**
   ```sh
   id: Primary Key, Integer
   field_name: String (e.g., 'Business Name', 'PAN', 'GSTIN')
   field_type: String (e.g., 'string', 'number', 'date')
   is_required: Boolean
   country_id: Foreign Key, references Country.id


## Running the Application

- You can the application by typing 
    ```sh
    uvicorn main:app --reload --port 5000
    or
    python3 -m uvicorn main:app --reload --port 5000
- This will start the server at localhost:5000

## Testing with Postman

- There are two Models present in here where configuration depends on country model. And In this project i have not added api for adding data to country Collection. So you have to do it Manually or using pgadmin4 by wrting queries as:
    ```sh
    INSERT INTO countries (name, code) VALUES ('CountryName', 'CountryCode');
- Replace CountryName and CountryCode with different values to create dummy data.
- After this You will have some dummy data in Country Collection.
- After this You can test api in Postman
- example for a PUT request:- 
    ```sh
    http://localhost:5000/create_configuration/
    {
        "country_id" : 2,
        "field_name": "field_name",
        "field_type": "String2",
        "is_required": true
    }
- Through this you can test all the APIs on Postman

This FastAPI project provides a simple API for managing configurations associated with countries using SQLAlchemy and PostgreSQL. Follow the steps in this README to set up, run, and test the application.
