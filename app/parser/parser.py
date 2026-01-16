page_html = driver.page_source
obj={}
l=[]
soup = BeautifulSoup(page_html,'html.parser')

allData = soup.find("div",{"class":"dURPMd"}).find_all("div",{"class":"Ww4FFb"})
print(len(allData))
for i in range(0,len(allData)):
    try:
        obj["title"]=allData[i].find("h3").text
    except:
        obj["title"]=None

    try:
        obj["link"]=allData[i].find("a").get('href')
    except:
        obj["link"]=None

    try:
        obj["description"]=allData[i].find("div",{"class":"VwiC3b"}).text
    except:
        obj["description"]=None

    l.append(obj)
    obj={}



print(l)