# Python PostgreSQL & REST API Integration

A Python application that connects to a PostgreSQL database and consumes data from an HTTP REST API.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (version X.X or higher)
- PostgreSQL Database (running and accessible)
- Internet connection to consume the REST API
- Install python - https://www.python.org/downloads/
- Setup environment variable for python and pip
- Run ``pip install requests psycopg2`` from command line

## Getting Started

1. Clone this repository to your local machine.

```shell
git clone https://github.com/yourusername/python-postgres-rest-app.git
```
2. Configure your PostgreSQL and REST API settings.

Update the PostgreSQL database connection details in ``config.py``. 

3. Run the [users.sql](users.sql) into database.

4. Run the application. ``python main.py``

## Project Structure
- main.py: The main Python script for database connection and API consumption.
- config.py: Configuration file for database and API settings.
- users.sql: SQL create table script
