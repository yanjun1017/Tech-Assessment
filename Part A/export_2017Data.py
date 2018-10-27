
import xlrd 
import os

if __name__ == "__main__":
	
	filename = "311_Service_Requests_from_2010_to_Present.csv"
	outfilename = "311-2017.csv"
	path = "data/"

	outfile = os.path.join(path, outfilename)

	ifile = open(filename, "r")
	ofile = open(outfile, "a+")
	header = ifile.readline()
	ofile.write(header)
	while True:
		line = ifile.readline()
		if line.strip() == 0:
			break
		# If 2017 is in created date of the current line
		# Write it to the file
		if "2017" in line.split(",")[1]:
			ofile.write(line)