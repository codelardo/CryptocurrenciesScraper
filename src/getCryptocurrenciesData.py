import requests, datetime, time
import database as db
import settings as settings
from bs4 import BeautifulSoup
from criptocurrencies import cryptocurrencies

def get_coins_links(coins):
	print('Get historical urls')
	coin_links = []
	for coin in coins:
		link = settings.BASE_URL + coin + settings.URL_QUERY_STRING
		coin_link = (coin, link)
		coin_links.append(coin_link)

	return coin_links

def get_history_table(coin, con):
	coin_table = coin[0].replace("-", "_")
	print('Get ' + coin_table + ' history')
	db.create_table(coin[0], con)

	site = requests.get(coin[1])
	historical = BeautifulSoup(site.content, 'html.parser')
	table = historical.find_all('table')[2]

	data = []
	rows = table.find_all('tr')
	for row in rows:
	    items = []
	    counted_rows = row.find_all('td')
	    for element in counted_rows:	    	
	    	items.append(element.text.strip())
	    
	    if items:	        
	        date = items[0]
	        date = time.mktime(datetime.datetime.strptime(date, '%b %d, %Y').timetuple())
	        price = items[3].replace("$", "")
	        price = price.replace(",", "")
	        price = float(price)
	        ratio = (date, price)
	        data.append(ratio)
	
	data.reverse()
	return data

def get_history(coins, con):
	data_coins = {}
	for coin in coins:
		data_coins[coin[0]] = get_history_table(coin, con)

	return data_coins

@settings.timer
def main():
	connection = db.db_connection('crypto.db')
	coins = get_coins_links(cryptocurrencies)
	data_coin = get_history(coins, connection)
	db.data_record(data_coin, connection)
	connection.commit()
	connection.close()
		
if __name__ == '__main__':
    main()
