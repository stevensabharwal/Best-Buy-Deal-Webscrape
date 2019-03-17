from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

pageToScrape = "https://www.bestbuy.ca/en-CA/sc-59069/wearable-tech-on-sale?icmp=wearablescategory_shopby_sale"
filename = "deals.csv"
headers = "Item Name, Current Price \n"

uClient = uReq(pageToScrape)  # opens up connection to the website
page_html = uClient.read()  # extracts the website's html
uClient.close()  # closes the url client since we just wanted the html
page_soup = soup(page_html, "html.parser")  # parse it as html using bs4
all_items = page_soup.findAll("div", {"class": "prod-info"})

f = open(filename, "w")
f.write(headers)

#
for item in all_items:
    name = str(item.h4.a)  # convert returned value to a string for splicing
    name = name[name.find(">") + 1:name.find("</a>")]  # splice the title of the item

    price_container = item.div.findAll("span", {"class": "amount"})  # extract price container
    current_price = price_container[0].text  # extract price from price container

    f.write(name.replace(",", " |") + "," + current_price.replace(",", ".") + "\n")  # write extracted info to file

f.close()
