# import the necessary libraries
import streamlit as st
import pandas as pd
import datetime,sqlite3


# Function to get the route names
def get_route_name():
    # Connect to the SQLite database
    conn = sqlite3.connect("Storage//bus_routes.db") 
    # Query the data
    query = "SELECT bus_route_name FROM bus_routes;"
    # Read the data into a DataFrame   
    df = pd.read_sql_query(query, conn)
    # Drop duplicates
    df = df.drop_duplicates()
    # Close the database connection
    conn.close()
    # Return the DataFrame
    return df


# Function to generate time ranges with 30-minute intervals
def generate_time_ranges():
    time_ranges = []
    # Loop through the hours
    for i in range(24):
        if i+2>23:
            break
        x = datetime.time(i)
        y = datetime.time(i+2)
        time_ranges.append(f"{x.strftime('%H:%M')} - {y.strftime('%H:%M')}")
    # Return the time ranges
    return time_ranges


# Function to get the data based on user selections
def get_data(d):
    # Connect to the SQLite database
    conn = sqlite3.connect("Storage//bus_routes.db") 
    # Construct the search patterns based on user selections
    ac_pattern = f"%{d[1]}%"
    seating_pattern = f"%{d[2]}%"
    star = d[3]
    t = d[4]
    # Query the data
    query = f"""SELECT * FROM bus_routes WHERE bus_route_name = ? 
                AND bus_type LIKE ? 
                AND bus_type LIKE ?
                AND star_rating BETWEEN ? AND ?
                AND departing_time BETWEEN ? AND ?
                AND price <= ?"""  
    df = pd.read_sql_query(query, conn, params=(d[0],seating_pattern,ac_pattern,star[0],star[5],t[:5],t[8:],d[5],))
    # Close the database connection
    conn.close()
    # Return the DataFrame
    return df


# Main function
def main():
    # Set the title
    st.title("Fill Bus Details")
    # Get the route names
    route_name = get_route_name()
    # Create  first set of columns 
    c1,c2,c3 = st.columns(3,gap='medium')
    route_names = c1.selectbox("Select the Route", route_name)
    seat_type = c2.selectbox("Select the Seat Type", ["Sleeper", "Seater"])
    ac_type = c3.selectbox("Select the AC Type", ["A/C", "Non A/C"])

    # Create second set of columns
    c4,c5,c6 = st.columns(3,gap='medium')
    # create rating filter
    rating_filter = c4.selectbox("Select the Ratings", ["1 to 2", "2 to 3", "3 to 4", "4 to 5"])  
    # create time filter
    time_range = generate_time_ranges()
    time_filter = c5.selectbox("Select Time Range", time_range)
    # create fare filter
    f1 = [i for i in range(100,1001,100)]
    fare_filter = c6.selectbox('Select Fare Upto',options=f1)
    
    st.write('## Data from SQLite Database')
    # Get the data based on user selections
    data = [route_names,seat_type,ac_type,rating_filter,time_filter,fare_filter]
    # call the function to get the data
    df = get_data(data)
    # Clean the star_rating column
    df['star_rating'] = pd.to_numeric(df['star_rating'], errors='coerce')
    # Drop rows with missing star_rating values
    df = df.dropna(subset=['star_rating'])
    # Convert the star_rating column to float
    df['star_rating'] = df['star_rating'].astype(float)
    # Use st.dataframe for a scrollable, sortable table
    st.dataframe(df)
 

# Call the main function
if __name__=='__main__':
    main()


