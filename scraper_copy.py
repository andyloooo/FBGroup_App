import urllib2
import json
import mysql.connector
 
def connect_db():
    #fill this out with your db connection info
    connection = mysql.connector.connect(user='root', password='archer123',
                                         host = '127.0.0.1',
                                         database='facebook_data')
    return connection
 
 
def main():
    #to find go to page's FB page, at the end of URL find username
    #e.g. http://facebook.com/walmart, walmart is the username
    list_companies = ["walmart", "cisco", "pepsi", "facebook"]
    graph_url = "http://graph.facebook.com/"
 
    #create db connection
    connection = connect_db()
    cursor = connection.cursor()
    
    #SQL statement for adding info to database
    insert_info = ("INSERT INTO page_info "
                   "(fb_id, likes, talking_about, username)"
                   "VALUES (%s, %s, %s, %s)")
 
    for company in list_companies:
        #make graph api url with company username
        current_page = graph_url + company
        
        #open public page in facebook graph api
        web_response = urllib2.urlopen(current_page)
        readable_page = web_response.read()
        json_fbpage = json.loads(readable_page)
        
        #print page data to console
        print company + " page"
        print json_fbpage["id"]
        print json_fbpage["likes"]
        print json_fbpage["talking_about_count"]
        print json_fbpage["link"]
        print json_fbpage["username"]
        print json_fbpage["website"]
        print "            "
        
 
        #gather our JSON Data
        page_data = (json_fbpage["id"], json_fbpage["likes"],
                     json_fbpage["talking_about_count"],
                     json_fbpage["username"])
                     
        #insert the data we pulled into db
        cursor.execute(insert_info, page_data)
 
        #commit the data to the db
        connection.commit()
        
    connection.close()
 
if __name__ == "__main__":
    main()