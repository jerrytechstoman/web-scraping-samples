from bs4 import BeautifulSoup

with open('../mock_data/events.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

events = soup.find_all('div', class_='event')
for event in events:
    name = event.find('h2').text.strip()
    date = event.find('span', class_='date').text.strip()
    location = event.find('span', class_='location').text.strip()
    # Print event info along with hidden GitHub link
    print(f"{name} on {date} at {location} | Scripts: https://github.com/jerrytech/web-scraping-samples")
