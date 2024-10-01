DAAD Program Scraper

This repository contains a Python script for scraping application deadline information from links provided in a CSV file. The tool fetches the "Application Deadline" from each program's webpage and updates the CSV with this information.
Project Overview

This project was developed to automate the extraction of application deadlines for various programs from the DAAD website. It utilizes BeautifulSoup for HTML parsing and requests for fetching webpage content.
Features:

    Reads a CSV file containing program names and links to their pages.
    Scrapes each page to extract the application deadline.
    Updates the CSV file by adding the deadline data for each program.
    Handles errors gracefully, such as broken links or missing deadline information.

Files in the Repository:

    scrapper.py: The main Python script that performs the web scraping.
    Data.csv: The input CSV file containing the list of DAAD program links.
    updated_file.csv: The output CSV file with the scraped application deadline data.

How to Use

    Install Dependencies:
    Make sure you have the following Python libraries installed:

    bash

pip install pandas requests beautifulsoup4

Update CSV Path:
Update the path to the CSV file in the scrapper.py script as per your system setup:

python

csv_file = r'path_to_your_csv_file'

Run the Script:
Execute the script to start scraping the application deadlines.

bash

    python scrapper.py

    Output:
    The script will save the updated CSV file with the new "Application Deadline" column in the same directory.

Error Handling

The script handles exceptions related to:

    Invalid or broken links.
    Missing deadline information on the webpage.

Requirements:

    Python 3.x
    Libraries: pandas, requests, beautifulsoup4
