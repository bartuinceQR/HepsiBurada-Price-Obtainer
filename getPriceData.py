import requests
import sys
import bs4

fetchurl = sys.argv[1]
page = requests.get(fetchurl)
soup = bs4.BeautifulSoup(page.content, 'lxml')

pricearea = soup.find('span', attrs={'id' : 'offering-price'})

#Technically I could just get the content of the pricearea for the price itself, but getting each attribute
#separately feels safer.
pricemain = pricearea.find('span', attrs={'data-bind' : 'markupText:\'currentPriceBeforePoint\''}).text
pricesub = pricearea.find('span', attrs={'data-bind' : 'markupText:\'currentPriceAfterPoint\''}).text
currency = pricearea.find('span', attrs={'itemprop' : 'priceCurrency'}).text #alternatively, use .get('content') for TRY.

print(pricemain + ','+ pricesub + ' ' + currency)