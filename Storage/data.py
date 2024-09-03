import sqlite3

# Function to create a database and table
def create_db():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('storage//bus_routes.db')
    cursor = conn.cursor()

    # Create a table with the required fields
    create_table_query = """
        CREATE TABLE IF NOT EXISTS bus_routes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bus_route_name TEXT,
            bus_route_link TEXT,
            bus_name TEXT,
            bus_type TEXT,
            departing_time TEXT,
            duration TEXT,
            reaching_time TEXT,
            star_rating FLOAT,
            price REAL,
            seat_availability INTEGER
        )
    """
    # Execute the query
    cursor.execute(create_table_query)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Database and table created successfully.")

# Function to insert data into the table
def insert(data):
    # Connect to SQLite database (or create it if it doesn't exist)
    create_db()
    conn = sqlite3.connect('storage//bus_routes.db')
    cursor = conn.cursor()

    # Insert data into the table
    query = f"""
        INSERT INTO bus_routes (bus_route_link, bus_route_name, bus_name, bus_type, departing_time, duration, reaching_time, star_rating, price, seat_availability)
        VALUES ({data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}, {data[7]}, {data[8]}, {data[9]})
        """

    cursor.execute(query)
    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

# Function to fetch data from the table
def fetch_data(query):
    conn = sqlite3.connect('storage//bus_routes.db')
    cursor = conn.cursor()
    cursor.execute(query)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()


if __name__=='__main__':
    # Call the function to create the database and table
    create_db()
