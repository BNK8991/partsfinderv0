#2nd example for getting infor from real-life sites

from bs4 import BeautifulSoup
import requests as rq #get info from sites

#Function for filtering
print(f'Input your wanted brand')
wanted_brand = input('>')
print(f'Finding {wanted_brand} card: ')

def microCen_find_card():
    html_text=rq.get('https://www.microcenter.com/category/4294966937,519/video-cards').text #get the html elements
    soup = BeautifulSoup(html_text, 'lxml')
    cards = soup.find_all('li', class_ = 'product_wrapper') # apparently this works with list but not div
    for card in cards:
        available = card.find('span', class_ = 'availabilityTrunc')
        if "Available" in available: #this is the filter too :D 
            card_name = card.find('h2', class_ = '').text #.text to get rid of unneeded elements
            price = card.find('span', itemprop_ = 'price')
            more_info = card.div.a['href'] #Get the content within the <a> only, that's how I put it, right?
            print(f'Card name: {card_name.strip()} ')
            print(f'Card price: {price.strip()} ')
            print(f'Would you like to know more?: {more_info}') #this should output the link


if __name__ == '__main__':
    microCen_find_card()


