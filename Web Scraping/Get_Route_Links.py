# import the necessary libraries
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Function to get route links
def get_route_links(url):

    # Intialize the service with the executable_path
    service = Service(executable_path="chromedriver-win64//chromedriver.exe")
    # Initialize WebDriver
    driver = webdriver.Chrome(service=service)
    # create an WebDriverWait object
    wait = WebDriverWait(driver,20)
    # opening the website
    driver.get(url)
    # wait until bus item is present
    pages = driver.find_elements(By.CLASS_NAME,'DC_117_pageTabs ')
    data = []
    # Check if there are multiple pages
    if pages:
        for i in range(len(pages)):
            # wait until route container is present
            routescontainer = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "route")))
            # loop through the routes container

            for route in routescontainer:
                # get the route name
                route_name = route.text
                # get the route link
                route_link = route.get_attribute('href')
                data.append({'routename' : route_name, 'routelink' : route_link})
            # check if it is not the last page
            if i > 0:
                # click on the next page
                page_tabs = driver.find_elements(By.CLASS_NAME, "DC_117_pageTabs ")[i]
                driver.execute_script("arguments[0].click();", page_tabs)
                time.sleep(1)
    else:
        # wait until route container is present
        routescontainer = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "route")))

        # loop through the routes container
        for route in routescontainer:
            route_name = route.text
            route_link = route.get_attribute('href')
            data.append({'routename' : route_name, 'routelink' : route_link})
            time.sleep(1)

    # wait for 4 seconds
    time.sleep(4)
    # close the browser
    driver.quit()
    # return the data
    return data


# main function
def main():
    # 10 Government State Bus Transport Site urls
    urls = ['https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile','https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile','https://www.redbus.in/online-booking/astc/?utm_source=rtchometile','https://www.redbus.in/online-booking/chandigarh-transport-undertaking-ctu','https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile','https://www.redbus.in/online-booking/jksrtc','https://www.redbus.in/online-booking/west-bengal-transport-corporation?utm_source=rtchometile','https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile','https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile','https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile']
    
    # get the route links
    d1 = get_route_links(urls[9])
    # Create a DataFrame
    df = pd.DataFrame(d1)
    # Save to CSV
    df.to_csv('data//route_data//bus_routes_10.csv', index=False)
    
    # Loop through the URLs inside the list of URLs
    for i in range(1,11):
        # Read the CSV file
        df = pd.read_csv(f'data//route_data//bus_routes_{i}.csv')
        print(len(df))
        # Remove duplicate rows
        df_no_duplicates = df.drop_duplicates()
        print(len(df_no_duplicates))
        # Write the cleaned data back to a new CSV file
        df_no_duplicates.to_csv(f'data//route_data//bus_routes_{i}.csv', index=False)
        print()

# Call the main function
if __name__=="__main__":
    main()
