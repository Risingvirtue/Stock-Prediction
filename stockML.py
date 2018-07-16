import requests
class StockAPI:
	def __init__(self, apikey):
		self.apikey = apikey
	def __str__(self):
		return self.apikey
	def apicall(self):
		resp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=amzn&apikey=]' + self.apikey)
		print(resp.json())
		
api = StockAPI('WDY9UDH99K9I5MMI')

api.apicall();
