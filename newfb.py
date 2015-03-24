import facebook
import json
import urllib2

def render_to_json(graph_url):
    #render graph url call to JSON
    web_response = urllib2.urlopen(graph_url)
    readable_page = web_response.read()
    json_data = json.loads(readable_page)
    
    return json_data

def print_posts(group_posts):
	count = 0
	for post in group_posts:
		count+=1
		try:
			#try to print out data
			print post["from"]["name"]
			print post["message"] + "\n"        
		except Exception:
			print "Error"
	return count

def turn_page(json_fbpage, page_turns):
	i = 0
	total_count = 0
	for x in range (0, page_turns):
		json_fbposts = json_fbpage["data"]
		total_count += print_posts(json_fbposts) #	print out page of posts and count number of posts
		
		
		paging = json_fbpage["paging"]		# turn page
		next = paging["next"]
		json_fbpage = render_to_json(next)
	
	return total_count
	
token = "CAACEdEose0cBACi8HInNpgvSZBF6WKGtMZCot4SEHsZBq7qUlZBpUmHNQ9qc9hWHuv0gzPIEpoJyv1y63UvCZA4sAbYPiQ4MjETyzUmoMMTA9yyQUhzDqUGZAoLLRXHGXXZCcab7ZCPDqoUOUHVzRo6drinGLLeZCqyMs9jzZABQgvkF7u9TxZBf0J2GD6WQqqZBmh9N1besIiExZCh9bTn4rf6oV0UJfbMAtZC1QZD" 
graph = facebook.GraphAPI(token)
freeforsale = "331733603546959"
graph_url = "https://graph.facebook.com/"
page_turns = 2

go_to = graph_url + freeforsale + "/feed?limit=25" + "/?key=value&access_token=" + token
json_fbpage = render_to_json(go_to)

total_count = turn_page(json_fbpage, page_turns)

print "count = ", total_count

