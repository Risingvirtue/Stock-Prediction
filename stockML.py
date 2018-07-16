import requests
class StockAPI:
	def __init__(self, apikey):
		self.apikey = apikey
	def __str__(self):
		return self.apikey
	def createText(self, file):
		return
	def apicall(self, file):
		resp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=amzn&outputsize=full&apikey=' + self.apikey).json()
		rsi = requests.get('https://www.alphavantage.co/query?function=RSI&symbol=AMZN&interval=daily&time_period=14&outputsize=full&series_type=close&apikey=' + self.apikey).json()
		resp = resp['Time Series (Daily)']
		rsi = rsi["Technical Analysis: RSI"]
		for day in rsi:
			if (day in resp):
				resp[day]["RSI"] = rsi[day]["RSI"]
		print(resp)
		'''
		f = open(file, 'w+')
		f.write(str(resp.json()))
		f.close()
		'''
	def inquiry(self, file):
		f = open(file, "r")
		info = f.read()
		return info
	def structureFile(self, dict):
		time = dict['Time Series (Daily)']
		timeArr = []
		for day in time:
			timeArr.append({"day": day, 
							"open": time[day]["1. open"], 
							"high": time[day]["2. high"], 
							"low": time[day]["3. low"], 
							"close": time[day]["4. close"], 
							"volume": time[day]["5. volume"] 
							})
							
			
api = StockAPI('WDY9UDH99K9I5MMI')
api.apicall('test')
##dict = eval(api.inquiry("amzn.txt"))
##api.structureFile(dict)
#api.apicall();
