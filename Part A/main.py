import pandas as pd
from sodapy import Socrata

# popfile = '/Users/yanjunli/Desktop/DBRS/2010+Census+Population+By+Zipcode+(ZCTA).csv'
# data = pd.read_csv(popfile)

if __name__ == "__main__":
	"""
	Source: https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv
	""" 
	client = Socrata("data.cityofnewyork.us", None)

	# Filter down to the 2017 data using statement "created_date >= '2017-01-01T00:00:00.000"
	# This is intended to find all complaints on 2017
	results = client.get("fhrw-4uyv", where = " created_date >= '2017-01-01T00:00:00.000'")
	# Convert to pandas DataFrame
	results_df = pd.DataFrame.from_records(results)




	# Closed session when finished
	client.close()
