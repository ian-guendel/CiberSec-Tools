import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://statistics.calpoly.edu/content/directory")
soup = BeautifulSoup(response.content, "html.parser")
tables = soup.find_all("table")

table = tables[1]
rows = []
for faculty in table.find_all("tr")[1:]:
    # Get all the cells in the row.
    cells = faculty.find_all("td")

    # The information we need is the text between tags.
    name_tag = cells[0].find("strong") or cells[0]
    name = name_tag.text

    link = cells[1].find("a")
    office = cells[1].text if link is None else link.text

    email_tag = cells[3].find("a") or cells[3]
    email = email_tag.text

    # Append this data.
    rows.append({
        "name": name,
        "office": office,
        "email": email
    })

    print(pd.DataFrame(rows))

#################### Second Page Scrapping  #######################
    
courses_catalog_page = requests.get("http://catalog.calpoly.edu/collegesandprograms/collegeofsciencemathematics/statistics/#courseinventory")
soup = BeautifulSoup(courses_catalog_page.content, "html.parser")
divs = soup.find_all("div", {"class": "courses"})
divs = divs[0]
rows = []
for div in divs.find_all("div", {"class": "courseblock"}):
    title = div.find("p").text
    rows.append({
        "title": title
    })
data = pd.DataFrame(rows)
data.to_csv("available_courses.csv")
