import urllib2 # python library that handles URLs
import json # python library that helps to handle JSON
import mysql.connector

def connect_db():
	#fill this out with your db connection info
	connection = mysql.connector.connect(user='root', password='archer123',
										host='127.0.0.1', database='facebook_data')
	return connection

def main():
	#to find username go to FB page, copy the end of URLs
	list_companies = ["walmart", "verge", "jakeandamir", "teslamotors"]
	graph_url = "http://graph.facebook.com/"
	# use graph.facebook.com/walmart to preview website	
	
	#create db connection
	connection = connect_db()
	cursor = connection.cursor() #creates mySQL cursor in database
	
	#	SQL statement for adding Facebook database
	insert_info = ("INSERT INTO page_info " "(fb_id, likes, talking_about, username)"
					"VALUES (%s, %s, %s, %s)")
					# takes 4 variables and puts passed data into 4 columns in database
					# id and timestamp will be automatically added
	for company in list_companies:
		# make graph api url with company username
		current_page = graph_url + company
		
		# open public page in facebook graph api
		web_response = urllib2.urlopen(current_page) # open current_page url into web_response
		readable_page = web_response.read() # read web_response into readable_page
		json_fbpage = json.loads(readable_page) # decodes readable_page into json format
		
		print company + "page"
		print "id = " + json_fbpage["id"]
		print "likes = ", json_fbpage["likes"]
		print "talking_about_count = ", json_fbpage["talking_about_count"]
		print "username = " + json_fbpage["username"]
		print "            "
		
		#gather our JSON data
		page_data = (json_fbpage["id"], json_fbpage["likes"], json_fbpage["talking_about_count"],
					json_fbpage["username"])
		
		#insert data pulled into data
		cursor.execute(insert_info, page_data)
		
		# commit the data to the db
		connection.commit() #save to database

	connection.close()
		
if __name__ == "__main__": # runs module directly as program
	main()
		
		

