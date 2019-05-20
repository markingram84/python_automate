import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('body > div.main-container > div.main-page.row > div:nth-child(2) > section.book-detail.span12.alpha.omega > div.span7.mobile-span12.alpha.tablet-alpha > div.book-actions > div > div > div > div.price > div > b:nth-child(2)')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.waterstones.com/book/the-boy-who-grew-dragons/andy-shepherd/sara-ogilvie/9781848126497')
print('The price is ' + price)