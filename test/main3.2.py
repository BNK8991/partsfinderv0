#4th example for getting infor from real-life sites
#this is where I pretified the output + put in some filters as well

from bs4 import BeautifulSoup
import requests #get info from sites

#Function for filtering
print(f'Input your wanted brand')
wanted_brand = input('>')
print(f'Finding {wanted_brand} card: ')

def find_card():
    html_text=requests.get('https://www.phucanh.vn/card-man-hinh.html').text #get the html elements
    soup = BeautifulSoup(html_text, 'lxml')
    cards = soup.find_all('li', class_ = 'p-item-group') # apparently this works with list but not div
    for card in cards:
        available = card.find('span', class_ = 'p-bottom').span.text.replace('Giỏ hàng', '') #this is for the filter
        if "✔ Có hàng" in available: #this is the filter too :D 
            card_name = card.find('h3', class_ = 'p-name').text #.text to get rid of unneeded elements
            price = card.find('span', class_ = 'p-price2').text.replace('Giá VNPAY:      ', '')
            more_info = card.div.a['href'] #Get the content within the <a> only, that's how I put it, right?
            
            if wanted_brand in card_name:

                print(f'Card name: {card_name.strip()} ')
                print(f'Card price: {price.strip()} ')
                print(f'Would you like to know more?: {more_info}')


if __name__ == '__main__':
    find_card()
     