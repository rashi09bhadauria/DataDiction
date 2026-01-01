
from bs4 import BeautifulSoup
import pandas as pd

with open("dataset.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

data = []
for row in rows:
    cols = row.find_all("td")
    if len(cols) == 0:
        continue
    data.append([float(c.text.strip()) for c in cols])

df = pd.DataFrame(data)
df.to_csv("addiction_data.csv", index=False)

print("Scraping completed")
