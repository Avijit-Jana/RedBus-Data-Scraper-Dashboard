# import the necessary libraries
import time,re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Function to extract bus information
def extract_bus_info(name,url):

    # Intialize the service with the executable_path
    service = Service(executable_path="chromedriver-win64//chromedriver.exe")
    # Initialize WebDriver
    driver = webdriver.Chrome(service=service)
    # create an WebDriverWait object
    wait = WebDriverWait(driver,20)
    # opening the website
    driver.get(url)
    # wait until bus item is present
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'bus-item')]")))
    # Scroll to the bottom of the page and load all bus listings
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for the page to load
        time.sleep(1)  
        # Check if more buses have loaded by comparing scroll heights
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # After scrolling, collect all bus details
    bus_list = driver.find_elements(By.XPATH, "//div[contains(@class, 'bus-item')]")

    # Check how many bus containers were found
    print(f"Number of bus containers found: {len(bus_list)}")
    # Create an empty list to store bus details
    buses = []
    for bus in bus_list:
        try:
            # Extract bus name
            bname = bus.find_element(By.XPATH, ".//div[contains(@class, 'travels lh-24 f-bold d-color')]").text
            # Extract bus type
            btype = bus.find_element(By.XPATH, ".//div[contains(@class, 'bus-type f-12 m-top-16 l-color evBus')]").text
            # Extract departure time
            departure_time = bus.find_element(By.XPATH, ".//div[contains(@class, 'dp-time f-19 d-color f-bold')]").text
            # Extract duration
            duration = bus.find_element(By.XPATH, ".//div[contains(@class, 'dur l-color lh-24')]").text           
            # Extract arrival time
            arrival_time = bus.find_element(By.XPATH, ".//div[contains(@class, 'bp-time f-19 d-color disp-Inline')]").text
            # Extract star rating
            star = bus.find_element(By.XPATH, ".//span[contains(@class, '')]").text           
            # Extract fare
            try:
                fare = bus.find_element(By.XPATH, ".//span[contains(@class, 'f-bold f-19')]").text
            except:
                fare = bus.find_element(By.XPATH, ".//span[contains(@class, 'f-19 f-bold')]").text
            # Extract seat availability
            seat = bus.find_element(By.XPATH, ".//div[contains(@class, 'column-eight w-15 fl')]").text
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Append the bus details to the list
            buses.append({
                'bus_route_name' : name,
                'bus_route_link' : url,
                'bus_name': bname,
                'bus_type': btype,
                'departing_time': departure_time,
                'duration': duration,
                'reaching_time': arrival_time,
                'star_rating':star,
                'price': fare,
                'seat_availability': re.search(r'\d+', seat).group()
            })
        except Exception as e:
            print(f"Error extracting bus details: {e}")

    # Create a DataFrame from the list of buses
    df = pd.DataFrame(buses)
    # Drop duplicates
    df = df.drop_duplicates()
    # Save to CSV
    df.to_csv(f'data//bus_data//8//{name}.csv', index=False)

    time.sleep(3)
    # Close the browser
    driver.quit()

if __name__=="__main__":

    # d1 = pd.read_csv(f'data//route_data//bus_routes_1.csv')
    # d2 = pd.read_csv(f'data//route_data//bus_routes_2.csv')
    # d3 = pd.read_csv(f'data//route_data//bus_routes_3.csv')
    # d4 = pd.read_csv(f'data//route_data//bus_routes_4.csv')
    # d5 = pd.read_csv(f'data//route_data//bus_routes_5.csv')
    # d6 = pd.read_csv(f'data//route_data//bus_routes_6.csv')
    # d7 = pd.read_csv(f'data//route_data//bus_routes_7.csv')
    d8 = pd.read_csv(f'data//route_data//bus_routes_8.csv')
    # d9 = pd.read_csv(f'data//route_data//bus_routes_9.csv')
    # d10 = pd.read_csv(f'data//route_data//bus_routes_10.csv')
    # print(d1[1])

    # converting csv file to a list of dictionaries
    x = d8.to_dict(orient='records')
    # extracting the route name and route link
    routename = [i['routename'] for i in x]
    routelink = [i['routelink'] for i in x]
    # extracting the bus information
    for i in range(len(routename)):
        extract_bus_info(routename[i],routelink[i])
