import requests
from lxml import html



#################################################
# create payload with username password         #
# and auth_token, This auth_token can be        #
# found on site login page with diff-diff       #
# names e.g csrfmiddlewaretoken or csrf_token   #
# authentication_token etc with a value of      #
# token some random string                      #
#################################################

payload = {
	"username": "<USER NAME>", 
	"password": "<PASSWORD>", 
	"csrfmiddlewaretoken": "<CSRF_TOKEN>"
}


session_requests = requests.session()

###################################
# To remove ssl certificate error #
###################################
session_requests.verify = False

login_url = "https://bitbucket.org/account/signin/?next=/"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

##############################
# scraping content           #
##############################

url = 'https://bitbucket.org/dashboard/overview'
result = session_requests.get(
	url, 
	headers = dict(referer = url)
)

tree = html.fromstring(result.content)
bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

print(bucket_names)

result.ok # Will tell us if the last request was ok
result.status_code # Will give us the status from the last request
