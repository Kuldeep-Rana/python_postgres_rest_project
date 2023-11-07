# main.py

# Run the users.sql script first 

import psycopg2
import requests
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, API_URL

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

    cursor = connection.cursor()
    print("Connected to the PostgreSQL database")

    # Consume the REST API and insert data into the database
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        data_entries = data.get("data", [])
        for entry in data_entries:
            id = entry.get("id")
            email = entry.get("email", "")
            first_name = entry.get("first_name", "")
            last_name = entry.get("last_name", "")
            avatar = entry.get("avatar", "")
            user_name = first_name+"_"+last_name  #small transformation
            insert_query = "INSERT INTO userdetails (id, email, user_name, avatar) VALUES (%s, %s, %s, %s);"
            cursor.execute(insert_query, (id, email, user_name, avatar))
        connection.commit()
        print("Data from the API inserted into the database")
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")

except (Exception, psycopg2.Error) as error:
    print(f"Error while connecting to PostgreSQL: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Database connection closed")
