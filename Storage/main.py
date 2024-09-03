import os,sqlite3,time
import pandas as pd

# Define the directory containing your CSV files
csv_directory = 'data\\bus_data\\8\\'
# Define the SQLite database file
sqlite_db = 'Storage\\bus_routes.db'
# Define the name of the table in SQLite
table_name = 'bus_routes'

try:
    # Create a connection to the SQLite database
    conn = sqlite3.connect(sqlite_db)

    # Loop through each file in the directory
    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            # Construct full file path
            file_path = os.path.join(csv_directory, filename)
            
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Insert the DataFrame into the SQLite table
            df.to_sql(table_name, conn, if_exists='append', index=False)
            time.sleep(1)
            
# Handle exceptions
except Exception as e:
    print(e)


conn.commit()
# Close the connection
conn.close()

print("Data imported successfully!")