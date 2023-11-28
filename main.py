import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_Name=[]
Prices=[]
Description=[]
Reviews = []

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+ str(i)
    r = requests.get(url)
    #print(r)

    soup= BeautifulSoup(r.text, 'lxml')
    box= soup.find("div",class_ = "_1YokD2 _3Mn1Gg")
    names = box.find_all("div",class_ = "_2kHMtA" )


    for i in names:
        name= i.text
        Product_Name.append(name)

        #print(len(Product_Name))
        prices = box.find_all("div",class_="_3tbKJL")

    for i in prices:
        name=i.text
        Prices.append(name)

            #print(Prices)

        desc = box.find_all('ul',class_ = "_1xgFaf")

    for i in desc:
        name = i .text
        Description.append(name)

                #print(Description)

        reviews= box.find_all("div",class_ = "_3LWZlK")

    for i in reviews:
        name= i.text
        Reviews.append(name)


#print(Reviews))

df = pd.DataFrame({"Product Name":Product_Name,"Prices":Prices,"Description":Description, "Reviews":Reviews})
print(df)

#df.to_csv("E:/Machine learning project/New folder/Flipkart_mobiles_under_50000.csv")












    #print(soup)
    #while True:
    #np=soup.find("a", class_ = "_1LKTO3").get('href')
    #cnp="https://www.flipkart.com" + np
    #print(cnp)


    #url = cnp
    #r= requests.get(url)
    #soup = BeautifulSoup(r.text,"lxml")
