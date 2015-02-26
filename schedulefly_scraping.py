#!/usr/bin/python
from BeautifulSoup import BeautifulSoup 
 

def read_ScheduleFlyHTML():
	# read the whole file in one go, as a string
	f = open('/home/batmanreborn/Downloads/WebCrawl The Row/ScheduleFlyContact_Book.html')
	myfilecontents = f.read()
	f.close()
	return myfilecontents

def schFLY_PrintOutPretty():
	"""The prettify method adds strategic newlines and spacing to make the structure of the document obvious. It also strips out text nodes that 		contain only whitespace."""
	html = read_ScheduleFlyHTML()
	soup = BeautifulSoup(''.join(html))
	print soup.prettify()

def schFLY_TableScraping():
	
	# extracts the text from the td tags	
	html = read_ScheduleFlyHTML()
	soup = BeautifulSoup(html)
	table = soup.find("table", style = "width:100%")
	
	"""It uses Beautiful Soup's findAll() method to put all of the tr tags (which is the HTML equivalent of a row) into a list. 
	The [1:] modifier at the end instructs the loop to skip the first item """
	for row in table.findAll('tr')[1:]:
        	col = row.findAll('td')
        	rank = col[0].string
        	artist = col[1].string
        	album = col[2].string
        	record = (rank, artist, album)
		print "|".join(record)

def main():
	read_ScheduleFlyHTML();
	schFLY_PrintOutPretty();
	schFLY_TableScraping();
	

if __name__ == "__main__":

	main();
