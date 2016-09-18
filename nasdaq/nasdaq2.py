'''
Historical market data using NASDAQ Data-on-Demand API service.

Command Line Args:
(1) stock symbol
'''

import urllib
import urllib2
import xmltodict

from datetime import datetime, timedelta
import sys

market_data = []
url = 'http://ws.nasdaqdod.com/v1/NASDAQAnalytics.asmx/GetSummarizedTrades'

def nasdaq_date(datetime_obj):
	print '%d/%d/%d %d:%d:00.000' % (datetime_obj.month, datetime_obj.day, datetime_obj.year, datetime_obj.hour, datetime_obj.minute)
	return '%d/%d/%d %d:%d:00.000' % (datetime_obj.month, datetime_obj.day, datetime_obj.year, datetime_obj.hour, datetime_obj.minute)

def get_market_data(values):
	request_parameters = urllib.urlencode(values)
	request = urllib2.Request(url, request_parameters)

	# Execute HTTP Request
	response = urllib2.urlopen(request)
	
	# Retrieve response and convert to python dict
	data = xmltodict.parse(response.read())

	for i in range(len(data['ArrayOfSummarizedTradeCollection']['SummarizedTradeCollection']['SummarizedTrades']['SummarizedTrade'])):
		hourly_data = data['ArrayOfSummarizedTradeCollection']['SummarizedTradeCollection']['SummarizedTrades']['SummarizedTrade'][i]
		
		# Check validity
		if eval(hourly_data['First']) > 0 and eval(hourly_data['Last']) > 0:
			market_data.append([
				hourly_data['Time'],
				hourly_data['First'],
				hourly_data['Last']
			])

def main(symbol):

	# Collect all data from January 1st, 2008vi 
	eval_date = datetime(2008, 1, 1)

	while eval_date + timedelta(6, 0, 0, 0, 59, 23) < datetime.today():

		# Update request parameters
		values = {
			'_Token': '247F80E1279F451499B6D68857FA0A93',
			'Symbols' : symbol,
			'StartDateTime' : nasdaq_date(eval_date),
			'EndDateTime' : nasdaq_date(eval_date + timedelta(6, 0, 0, 0, 59, 23)),
			'MarketCenters': 'Q, B',
			'TradePrecision': 'Hour',
			'TradePeriod': '1'
		}
		
		get_market_data(values)
		eval_date = eval_date + timedelta(7)

	values = {
		'_Token': '247F80E1279F451499B6D68857FA0A93',
		'Symbols' : symbol,
		'StartDateTime' : nasdaq_date(eval_date),
		'EndDateTime' : nasdaq_date(datetime.today()),
		'MarketCenters': 'Q, B',
		'TradePrecision': 'Hour',
		'TradePeriod': '1'
	}

	get_market_data(values)

	# Write data to CSV file
	with open('%s.csv' % symbol, 'w+') as output:
		output.write('Time,First,Last\n')
		output.write('\n'.join([','.join(market_data[i]) for i in range(len(market_data))]) + '\n')

if __name__ == '__main__':
	symbol = sys.argv[1].upper()
	main(symbol)