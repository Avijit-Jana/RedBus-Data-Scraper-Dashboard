import streamlit as st


def main():
    st.markdown("# About The Project")
    st.balloons()

    st.write("## Problem Statement:")
    st.write('''
        The "Redbus Data Scraping and Filtering with Streamlit Application" aims to
        revolutionize the transportation industry by providing a comprehensive solution for
        collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web
        scraping, this project automates the extraction of detailed information from Redbus,
        including bus routes, schedules, prices, and seat availability. By streamlining data
        collection and providing powerful tools for data-driven decision-making, this project
        can significantly improve operational efficiency and strategic planning in the
        transportation industry''')

    st.write("## Business Use Cases:")
    st.write('''
        The solution can be applied to various business scenarios including:\n
        ● Travel Aggregators: Providing real-time bus schedules and seat availability for
        customers.\n
        ● Market Analysis: Analyzing travel patterns and preferences for market
        research.\n
        ● Customer Service: Enhancing user experience by offering customized travel
        options based on data insights.\n
        ● Competitor Analysis: Comparing pricing and service levels with competitors.''')
    
    
if __name__=='__main__':
    main()