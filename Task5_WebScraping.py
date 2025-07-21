import requests
from bs4 import BeautifulSoup
import csv

# The URL of the website we want to scrape
URL = 'http://quotes.toscrape.com'

# Send a request to get the HTML content of the page
try:
    response = requests.get(URL)
    response.raise_for_status()  # This will raise an exception for bad status codes (4xx or 5xx)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Create a list to store the scraped data
    quotes_data = []

    # Find all the quote containers on the page
    # Each quote is inside a 'div' with the class 'quote'
    quotes = soup.find_all('div', class_='quote')

    # Loop through each quote container to extract the information
    for quote in quotes:
        # Extract the quote text (from a 'span' with class 'text')
        text = quote.find('span', class_='text').get_text(strip=True)

        # Extract the author (from a 'small' with class 'author')
        author = quote.find('small', class_='author').get_text(strip=True)

        # Extract the tags (from 'a' tags with class 'tag')
        tag_elements = quote.find_all('a', class_='tag')
        tags = ', '.join([tag.get_text(strip=True) for tag in tag_elements])

        # Add the extracted data as a dictionary to our list
        quotes_data.append({
            'Quote': text,
            'Author': author,
            'Tags': tags
        })

    # Define the CSV file name
    csv_file = 'quotes.csv'

    # Save the data into a CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        # Define the column headers
        fieldnames = ['Quote', 'Author', 'Tags']
        
        # Create a writer object
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()
        
        # Write the quote data rows
        writer.writerows(quotes_data)

    print(f"✅ Success! Scraped {len(quotes_data)} quotes and saved them to '{csv_file}'.")

except requests.exceptions.RequestException as e:
    print(f"❌ Error: Could not retrieve the website. {e}")