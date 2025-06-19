<div align="center">

# 🚌Redbus Project🚌

![GitHub repo size](https://img.shields.io/github/repo-size/Avijit-Jana/RedBus-Data-Scraper-Dashboard?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/Avijit-Jana/RedBus-Data-Scraper-Dashboard?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/Avijit-Jana/cnn-architectures-benchmark?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/Avijit-Jana/RedBus-Data-Scraper-Dashboard?color=red&style=plastic)

</div>

## Table of Contents

- [📖**Project Description**](#project-description)
- [🧑‍💼**Business Use Cases**](#business-use-cases)
- [📁**Data Set Explanation**](#data-set-explanation)
- [📊**Project Evaluation Metrics**](#project-evaluation-metrics)
- [🚩**How to Approach this Project**](#Approach)

## 📖Project Description
The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry. 

## 🧑‍💼Business Use Cases
The solution can be applied to various business scenarios including: 
- **Travel Aggregators:** Providing real-time bus schedules and seat availability for 
customers. 
- **Market Analysis:** Analyzing travel patterns and preferences for market 
research. 
- **Customer Service:** Enhancing user experience by offering customized travel 
options based on data insights. 
- **Competitor Analysis:** Comparing pricing and service levels with competitors. 

## 📁Data Set Explanation
- **Source:** Data will be scraped from the Redbus website. **Link-** https://www.redbus.in/ 
- **Format:** The scraped data will be stored in a SQL database. 
- **Required Fields:** Bus routes Link,Bus route Name, Bus name, Bus Type(Sleeper/Seater),  Departing Time, Duration, Reaching_Time, Star-rating, Price, Seat_availability

## 📊Project Evaluation Metrics
- **Data Scraping Accuracy:** Completeness and correctness of the scraped data.
- **Application Usability:** User experience and ease of use of the Streamlit application.
- **Filter Functionality:** Effectiveness and responsiveness of data filters.
- **Code Quality:** Adherence to coding standards and best practices.

## 🚩Approach:
1. **Data Scraping:**
    - Use Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.
2. **Data Storage:**
    - Store the scraped data in a SQL database.
3. **Streamlit Application:**
    - Develop a Streamlit application to display and filter the scraped data.
    - Implement various filters such as bustype, route, price range, star rating, availability.
4. **Data Analysis/Filtering using Streamlit:**
    - Use SQL queries to retrieve and filter data based on user inputs.
    - Use Streamlit to allow users to interact with and filter the data through the application.
    - Use Streamlit to display the filtered data in a user-friendly format.


```bash
pip install selenium pandas streamlit
```

<div align="middle">

![Badge](https://img.shields.io/badge/Developed%20By-Avijit_Jana-blueviolet?style=for-the-badge)

</div>
