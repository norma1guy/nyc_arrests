import requests,bs4,csv



def scrape():
    url = 'https://ypdcrime.com/penallawlist.php'
    headers = {'User-Agent' : 'Mozilla/5.0'}
    response = requests.get(url,headers=headers)
    pretty = bs4.BeautifulSoup(response.text,'html.parser')

    with open('penal.csv','w',newline='') as csvfile :
        penal = csv.writer(csvfile)
        for row in pretty.find_all('tr'):
            cols = row.find_all(['td','th'])
            cols = [col.text.strip() for col in cols]
            penal.writerow(cols)

if __name__ == '__main__' :
    scrape()