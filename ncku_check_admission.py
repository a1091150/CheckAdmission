from re import S
from termios import CSIZE
from tokenize import String
import requests
from bs4 import BeautifulSoup

def getAdmissionList(group_no:String):
    csie_url = "https://nbk.acad.ncku.edu.tw/netcheckin/index.php"

    params = {"c": "quall_rwd", "m" : "qu"}
    data = {"exam_id": "2", "group_no" : group_no}
    req = requests.post(csie_url, params= params, data = data)

    soup = BeautifulSoup(req.text, "html.parser" )
    # print(soup.prettify())

    admission_list = []
    wait_list = []

    table = soup.find("table", attrs={"class": "table table-striped"})
    table_body = table.find("tbody")
    rows = table_body.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        content = cols[1].text + " " + cols[3].text + "|" + cols[0].text
        if "備取" in cols[0].text:
            wait_list.append(content)
            break


        # if "備取" in cols[0].text:
            # wait_list.append(content)
            # ()
        # else:
            # admission_list.append("\033[0;33m" + content + "\033[0m")
            # ()

    title = soup.find("div", attrs={"class": "page-header"}).text.replace("\n","")
    print("\033[1;31m" + title + "\033[0m")
    for cc in admission_list:
        print(cc)
#    print("")
    for cc in wait_list:
        print(cc)


getAdmissionList("690") # CSIE
getAdmissionList("070") # CSIE AI
