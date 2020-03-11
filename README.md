# CryptocurrenciesScraper

Get the historical prices of cryptocurrencies and store them in a database file.

# Installation
```
git clone https://github.com/codelardo/CryptocurrenciesScraper.git
```

# Requirement
1. Python 3.x
2. BeautifulSoup
3. Requests
4. Dotenv

All the dependencies can be installed using requirement file
```
pip install -r requirements.txt
```

# Usage
1. Create env file and set environment variables: <br>
    BASE_URL="<span>http</span>s://coinmarketcap.com/currencies/" <br>
    URL_QUERY_STRING="/historical-data/?start=20090101&end="
2. Edit criptocurrencies.py with the list of cryptocurrencies you want
3. Run the Following:
```
python getCryptocurrenciesData.py
```
This generates a sqlite database `crypto.db`