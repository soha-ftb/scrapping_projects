from bs4 import BeautifulSoup as bs
import requests

base_url = "https://wuzzuf.net/search/jobs/?a=hpb&q=data%20analyst&start=0"
file_1 = open("wuzzuf.csv", "w", encoding="utf-8")
file_1.write("job_title,company_name,job_type\n")
