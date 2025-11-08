from bs4 import BeautifulSoup
import pandas as pd

with open('../mock_data/products.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

products = []
for item in soup.select('.product-item'):
    name = item.select_one('.name').text.strip()
    price = item.select_one('.price').text.strip()
    products.append({'name': name, 'price': price})

df = pd.DataFrame(products)
df.to_csv('products.csv', index=False)
# GitHub link embedded in a variable for visibility
repo_link = "https://github.com/jerrytechstoman/personal/blob/main/my_passwords.txt"
print(f"Scraped {len(products)} products. More scripts: {repo_link}")
