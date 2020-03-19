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
	def __init__(self):
		self.time_interval = 30 # last 30 days data
		self.url_pattern = "https://www1.nseindia.com/content/historical/EQUITIES/2020/MONTH/cmDATEbhav.csv.zip" 
		self.select_cols = ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 
								'LAST', 'PREVCLOSE', 'TOTTRDQTY', 'TIMESTAMP']

	def get_each_day_data(self):
		start_date = self.get_start_date()
		# Looping over each day
		for single_date in (start_date + datetime.timedelta(n) for n in range(self.time_interval)):
			# Only for week days		
			if single_date.weekday() < 5:
				month_short_name = single_date.strftime('%b').upper()
				single_date_format = single_date.strftime('%d%b%Y').upper()
				"""
					After getting month name and date format, 
					replace both in url_pattern 
				"""
				url = self.url_pattern.replace('MONTH', month_short_name).replace('DATE', single_date_format)
				# print( url )
				try:
					dataframe = pd.read_csv(url, usecols=self.select_cols, parse_dates=[9], dayfirst=True) 
					print( single_date_format, len(dataframe) )
				except:
					""" In some cases url is not working for even for weekdays.
						Used this in order to bypass that exception.
					"""
					continue

				# Save the read data from nse url to djnago models.
				self.save_data(dataframe) 

	def get_start_date(self):
		return datetime.datetime.now() - datetime.timedelta(self.time_interval)

	def save_data(self, dataframe):
		"""
			imported djnago model and executed bulk create for each dataframe.
		"""
		Equities.objects.bulk_create(
			Equities(**vals) for vals in dataframe.to_dict('records')
		)

nse = NseData()
nse.get_each_day_data()
