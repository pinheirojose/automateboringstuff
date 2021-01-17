import bs4, requests

def getAmazonPrice(productUrl):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#price_inside_buybox')
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.es/Duracell-Ultra-Power-Alcalinas-paquete/dp/B0043ZUEPE/?_encoding=UTF8&pd_rd_w=0DD4L&pf_rd_p=b35a8fd4-9fcd-4f0d-9f21-463622f120b3&pf_rd_r=65RABRE0WZ25DVEWP9S3&pd_rd_r=7b499f78-656d-44fe-bfdf-0cd3b12aa852&pd_rd_wg=nzNa1&ref_=pd_gw_unk')

print('The price is ' + price)
