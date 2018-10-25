import pandas as pd
from sodapy import Socrata
import numpy as np

if __name__ == "__main__":

	path = "data/311-2017.csv"
	# Read csv file
	results = pd.DataFrame(pd.read_csv(path, dtype='unicode', low_memory=False))
	# Change [results] to DataFrame
	results_df = pd.concat([results])
	"""
	-----------------------------------------------------------------------
	Question: Considering all complaint types. Which Boroughs are the biggest "complainers" relative 
	to the size of the population in 2017? Meaning, calculate a complaint-index that adjusts for population 
	of the Borough.
	"""
	pop = pd.read_csv("data/2010+Census+Population+By+Zipcode+(ZCTA).csv", dtype='unicode', low_memory=False)
	pop_data = pd.concat([pop], ignore_index = True)
	# grouped = pop_data.groupby("Borough").size().reset_index(name='count')
	grouped1 = results_df.groupby(['Incident Zip', 'Borough']).size().reset_index(name='count').sort_values('count', ascending=False)
	grouped1 = grouped1.loc[grouped1['Borough'] != 'Unspecified']
	grouped1 = grouped1.dropna(subset = ['Incident Zip'])
	grouped1 = grouped1.loc[grouped1['Incident Zip'] != 'UNKNOWN']
	grouped1 = grouped1.loc[grouped1['Incident Zip'] != '.']

	# Convert the type of zip code in both grouped1 and pop_data to int64
	grouped1['Incident Zip'] = grouped1['Incident Zip'].apply(int)
	pop_data['Zip Code ZCTA'] = pop_data['Zip Code ZCTA'].apply(int)
	pop_data['2010 Census Population'] = pop_data['2010 Census Population'].apply(int)
	# Merge the two dataframe if they have the same zip code
	merge_data = grouped1.merge(pop_data, how = 'left', left_on = 'Incident Zip', right_on = 'Zip Code ZCTA')
	# Delete the zip_code columns from merge_data
	merge_data.pop('Zip Code ZCTA')
	merge_data.pop('Incident Zip')
	# Group the data by its Borough and sum the complaints and population of the Borough
	merge_data = merge_data.groupby(['Borough']).sum()
	"""
	Complaint Index = (company complaints/company premium)/(industry-wide comlaints/industry-wide premium)
	"""
	# Calculate the total complaint and population of New York State
	total = merge_data.sum()
	# Calculate the complaint index
	merge_data['index'] = (merge_data['count']/merge_data['2010 Census Population'])/(total['count']/total['2010 Census Population'])
	# Print Borough which is the biggest "complainer"
	print(merge_data.sort_values('index', ascending = False).head(1))
	# Print all Boroughs 
	print(merge_data.sort_values('index', ascending = False))
