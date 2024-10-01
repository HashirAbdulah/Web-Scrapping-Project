import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the CSV file
csv_file = r'C:\Users\M.Hashir Abdullah\Desktop\DAADProgram\Data.csv'  # Use raw string to avoid unicode escape issues
df = pd.read_csv(csv_file)

# Add a new column for the Application Deadline
df['Application Deadline'] = None

# Iterate over each link in the DataFrame
for index, row in df.iterrows():
    link = row['Link']
    
    try:
        # Make a GET request to the URL
        response = requests.get(link)
        response.raise_for_status()  # Ensure the request was successful

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the "Application deadline" in the page
        description_list = soup.find('dl', class_='c-description-list')
        if description_list:
            items = description_list.find_all('dt', class_='c-description-list__content')
            for item in items:
                if 'Application deadline' in item.get_text():
                    deadline_content = item.find_next_sibling('dd').get_text(strip=True)
                    df.at[index, 'Application Deadline'] = deadline_content
                    break

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data for URL {link}: {e}")
    except Exception as e:
        print(f"An error occurred while processing URL {link}: {e}")

# Save the updated DataFrame back to the CSV file
df.to_csv('updated_file.csv', index=False)
