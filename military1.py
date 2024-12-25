import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape Indian military aircraft data from wikpedia
def scrape_indian_military_aircraft():
    url = "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='wikitable')
    rows = table.find_all('tr')[1:]  # Skip header row

    aircraft = []
    roles = []
    origins = []
    in_service = []
    notes = []

    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 4:
            aircraft.append(cols[0].text.strip())
            roles.append(cols[1].text.strip())
            origins.append(cols[2].text.strip())
            in_service.append(cols[3].text.strip())
            notes.append(cols[4].text.strip() if len(cols) > 4 else "")

    aircraft_data = pd.DataFrame({
        "Aircraft": aircraft,
        "Role": roles,
        "Origin": origins,
        "In Service": in_service,
        "Notes": notes
    })
    return aircraft_data

# Main Script
if __name__ == "__main__":
    # Scrape Indian military aircraft data
    try:
        print("Scraping Indian military aircraft data...")
        aircraft_data = scrape_indian_military_aircraft()
        print(aircraft_data.head())

        # Save the data to a CSV file
        aircraft_data.to_csv("indian_military_aircraft.csv", index=False)
        print("Data saved successfully as 'indian_military_aircraft.csv'!")
    except Exception as e:
        print(f"Failed to scrape data: {e}")