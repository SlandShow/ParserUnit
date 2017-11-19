# Web-page (https://www.weblancer.net/) parser

import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("div", class_="container-fluid cols_table show_visited")

    projects = []

    for row in table.find_all("div")[1:]:
        cols = row.find_all("div")

        if cols != None:
            projects.append({
                "title" : row.find("h2")
            })

        #print(cols)
        #print("----------------------------------")
    for project in projects:
        print(project)


def main():
    parse(get_html("https://www.weblancer.net/projects/"))

if __name__ == "__main__":
    main()