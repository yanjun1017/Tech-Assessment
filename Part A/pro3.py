import pandas as pd
from sodapy import Socrata
import numpy as np

if __name__ == "__main__":
	"""
	-----------------------------------------------------------------------
	Source: https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv
	""" 
	client = Socrata("data.cityofnewyork.us", '71rC0NkzYXZrZlJ9svKwZ9pNb')
	# Example authenticated client (needed for non-public datasets):
	# client = Socrata(data.cityofnewyork.us,
	#                  MyAppToken,
	#                  userame="user@example.com",
	#                  password="AFakePassword")


	# Filter down to the 2017 data using statement "created_date >= '2017-01-01T00:00:00.000"
	# This is intended to find all complaints on 2017
	# "where =" clause is going to select the specific data that fits the "where=" clause
	# "limit" is used for getting the amount of data specify in the right hand side
	results = client.get("fhrw-4uyv", where = " created_date > '2016-12-31T23:59:59.999'", limit = 10000)
	# Convert to pandas DataFrame
	results_df = pd.DataFrame.from_records(results)
	"""
	Source: https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv 
	-----------------------------------------------------------------------
	"""

	"""
	-----------------------------------------------------------------------
	Question: Considering all complaint types. Which boroughs are the biggest "complainers" relative 
	to the size of the population in 2017? Meaning, calculate a complaint-index that adjusts for population 
	of the borough.
	"""
	pop = pd.read_csv("data/2010+Census+Population+By+Zipcode+(ZCTA).csv", iterator = True, chunksize = 10000)
	pop_data = pd.concat(pop, ignore_index = True)
	# grouped = pop_data.groupby("Borough").size().reset_index(name='count')
	grouped1 = results_df.groupby(['incident_zip', 'borough']).size().reset_index(name='count').sort_values('count', ascending=False)
	grouped1 = grouped1.loc[grouped1['borough'] != 'Unspecified']
	grouped1 = grouped1.loc[grouped1['incident_zip'] != 'NaN']
	# Convert the type of zip code in both grouped1 and pop_data to int64
	grouped1['incident_zip'] = grouped1['incident_zip'].apply(int)
	pop_data['Zip Code ZCTA'] = pop_data['Zip Code ZCTA'].apply(int)
	pop_data['2010 Census Population'] = pop_data['2010 Census Population'].apply(int)
	
	# Merge the two dataframe if they have the same zip code
	merge_data = grouped1.merge(pop_data, how = 'left', left_on = 'incident_zip', right_on = 'Zip Code ZCTA')
	# Delete the zip_code columns from merge_data
	merge_data.pop('Zip Code ZCTA')
	merge_data.pop('incident_zip')
	# Group the data by its borough and sum the complaints and population of the borough
	merge_data = merge_data.groupby(['borough']).sum()
	"""
	Complaint Index = (company complaints/company premium)/(industry-wide comlaints/industry-wide premium)
	"""
	# Calculate the total complaint and population of New York State
	total = merge_data.sum()
	# Calculate the complaint index
	merge_data['index'] = (merge_data['count']/merge_data['2010 Census Population'])/(total['count']/total['2010 Census Population'])
	# Print borough which is the biggest "complainer"
	print(merge_data.sort_values('index', ascending = False).head(1))
	# Print all boroughs 
	print(merge_data.sort_values('index', ascending = False))
	# Closed session when finished
	client.close()
