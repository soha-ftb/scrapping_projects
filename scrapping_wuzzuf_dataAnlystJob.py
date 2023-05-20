from bs4 import BeautifulSoup as bs
import requests

base_url = "https://wuzzuf.net/search/jobs/?a=hpb&q=data%20analyst&start=0"
file_1 = open("wuzzuf.csv", "w", encoding="utf-8")
file_1.write("job_title,company_name,job_type\n")

for page in range(1, 12):
    url = base_url + str(page)
    client = requests.get(url)
    html = client.content
    soup = bs(html, "html.parser")
    client.close()
    containers = soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
    for container in containers:
        j_title = container.find("h2", {"class": "css-m604qf"}).text.strip()
        c_name = container.find("a", {"class": "css-17s97q8"}).text.strip()
        j_type = container.find("a", {"class": "css-n2jc4m"}).text.strip()
        file_1.write(j_title + "," + c_name + "," + j_type + "\n")
