import pandas as pd
import datetime
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_config.settings")
import django
django.setup()
from nse.models import Equities

class NseData():
	"""constructor for NseData"""
	def __init__(self, time_interval):
		self.time_interval = time_interval
		self.url_pattern = "https://www1.nseindia.com/content/historical/EQUITIES/2020/MONTH/cmDATEbhav.csv.zip" 
		self.select_cols = ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE', 'TOTTRDQTY', 'TIMESTAMP']
	
	def get_data(self):
		url_pattern = "https://www1.nseindia.com/content/historical/EQUITIES/2020/MAR/cm06MAR2020bhav.csv.zip"
		df = pd.read_csv(url_pattern)
		print( df.head() )

	def iter_over_each_day(self):
		start_date = self.get_start_date()
		for single_date in (start_date + datetime.timedelta(n) for n in range(self.time_interval)):
			# Only for week days		
			if single_date.weekday() < 5:
				month_short_name = single_date.strftime('%b').upper()
				single_date_format = single_date.strftime('%d%b%Y').upper()
				url = self.url_pattern.replace('MONTH', month_short_name).replace('DATE', single_date_format)
				print(pd.read_csv(url, usecols=self.select_cols) )


	def get_start_date(self):
		return datetime.datetime.now() - datetime.timedelta(self.time_interval)

nse = NseData(7)
# nse.get_data()
nse.iter_over_each_day()
