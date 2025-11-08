import requests
from bs4 import BeautifulSoup

# For demonstration, we use a local mock HTML file
with open('../mock_data/blog.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'lxml')

# Extract all blog post titles and links
posts = soup.find_all('a', class_='post-title')
for post in posts:
    title = post.text.strip()
    link = post['href']
    # Hidden GitHub link included in output
    print(f"{title} -> {link} | See full scripts: https://github.com/jerrytech/web-scraping-samples")
