from bs4 import BeautifulSoup
import requests as rq #get info from sites

#Function for filtering, this will be put in the ecom site later
print(f'Input your wanted brand')
wanted_brand = input('>')
print(f'Finding {wanted_brand} card: ')

#Functions to find CPU

#Functions to find Mother Board

#Functions to find GPU
#Scrapping from MicroCenter
def microCen_find_card():
    html_text=rq.get('https://www.microcenter.com/category/4294966937,519/video-cards').text #get the html elements
    soup = BeautifulSoup(html_text, 'lxml')
    cards = soup.find_all('li', class_ = 'product_wrapper') # apparently this works with list but not div
    for card in cards:
        available = card.find('span', class_ = 'availabilityTrunc').span.text.replace('', '') #this is for the filter
        if "Available" in available: #this is the filter too :D 
            card_name = card.find('h2', class_ = '').text #.text to get rid of unneeded elements
            price = card.find('span', itemprop_ = 'price')
            more_info = card.div.a['href'] #Get the content within the <a> only, that's how I put it, right?
            print(f'Card name: {card_name.strip()} ')
            print(f'Card price: {price.strip()} ')
            print(f'Would you like to know more?: {more_info}') #this should output the link

#Scrapping from Central Computer
def central_find_card():
    html_text=rq.get('https://www.centralcomputer.com/all-products/hardware/video-cards.html').text #get the html elements
    soup = BeautifulSoup(html_text, 'lxml')
    cards = soup.find_all('li', class_ = 'p-item-group') # apparently this works with list but not div
    for card in cards:
        available = card.find('span', class_ = 'p-bottom').span.text.replace('', '') #this is for the filter
        if "" in available: #this is the filter too :D 
            card_name = card.find('h3', class_ = 'p-name').text #.text to get rid of unneeded elements
            price = card.find('span', class_ = 'p-price2')
            more_info = card.div.a['href'] #Get the content within the <a> only, that's how I put it, right?
            print(f'Card name: {card_name.strip()} ')
            print(f'Card price: {price.strip()} ')
            print(f'Would you like to know more?: {more_info}')


#Functions to find Memory (RAM)

#Functions to find Storage (SSD)

#Functions to find Storage (HDD)

#Functions to find PSU

#Functions to find Air Cooler

#Functions to find AIO Cooler

#Functions to find Case



#Test the module by open this file in the terminal and put the function in
if __name__ == '__main__':
    print()