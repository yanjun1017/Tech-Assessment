
import pandas as pd
from sodapy import Socrata
import numpy as np

# popfile = '/Users/yanjunli/Desktop/DBRS/2010+Census+Population+By+Zipcode+(ZCTA).csv'
# data = pd.read_csv(popfile)

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
	results = client.get("fhrw-4uyv", where = " created_date > '2016-12-31T23:59:59.999'", limit = 1000000)
	# Convert to pandas DataFrame
	results_df = pd.DataFrame.from_records(results)
	"""
	Source: https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv 
	-----------------------------------------------------------------------
	"""

	# Take the top 10 most common complaint types
	# "groupby" clause is used to group the data by the specific type ie. ['complaint_type']
	# "count" is the number of data with the same type 
	# sort_values is use to sort the data by type 'count'
	# "head" is used to get the top elements 
	grouped = results_df.groupby(['complaint_type']).size().reset_index(name='count').sort_values('count', ascending=False).head(10)
	"""
	-----------------------------------------------------------------------
	Question:  Consider only the 10 most common overall complaint types. For each borough, 
	how many of each of those 10 types were there in 2017?
	""" 
	# Filter out unspecified borough
	results_df = results_df.loc[results_df['borough'] != 'Unspecified']
	# Loop through the top 10 most common complaint types
	# "complaint_type" is one of the top 10 most common complaint types
	for complaint_type in grouped['complaint_type']:
		# "df" contains only data with the same type as "complaint_type"
		df = results_df[results_df['complaint_type'] == complaint_type]
		# This statement is used for grouping the variable with the same complaint type as "complaint_type" 
		# and borough; and calculate the amount of data that fits the critirie 
		temp = df.groupby(['borough', 'complaint_type']).size().reset_index(name='count')
		if len(temp) != 0:
			print(temp)

	"""
	-----------------------------------------------------------------------
	"""

	"""
	-----------------------------------------------------------------------
	Question:  Consider only the 10 most common overall complaint types.  
	For the 10 most populous zip codes, how many of each of those 10 types were there in 2017?
	""" 
	grouped1 = results_df.groupby(['incident_zip']).size().reset_index(name='count').sort_values('count', ascending=False).head(10)
	# Filter out unspecified borough
	results_df = results_df.loc[results_df['borough'] != 'Unspecified']
	# Loop through the top 10 most common zip code
	# "incident_zip" is one of the top 10 most common zip code
	for incident_zip in grouped1['incident_zip']:
		# Loop through the top 10 most common complaint types
		# "complaint_type" is one of the top 10 most common complaint types
		for complaint_type in grouped['complaint_type']:
			# print(complaint_type)
			# "df" contains only data with the same type as "complaint_type"
			df = results_df[(results_df['incident_zip'] == incident_zip) & (results_df['complaint_type'] == complaint_type)]
			# This statement is used for grouping the variable with the same complaint type as "complaint_type" 
			# and zip code; and calculate the amount of data that fits the critirie 
			temp = df.groupby(['incident_zip', 'complaint_type']).size().reset_index(name='count')
			# print(temp)
			if len(temp) != 0:
				print(temp)
			
	# For the 10 most common zip code, print the number of the 10 most common complaint types

	"""
	-----------------------------------------------------------------------
	"""
	# Closed session when finished
	client.close()
