import requests
from lxml import html



#################################################
# create payload with username password         #
# and auth_token, This auth_token can be        #
# found on site login page with diff-diff       #
# names e.g csrfmiddlewaretoken or csrf_token   #
# authentication_token etc with a value of      #
# token some random string                      #  
#                                               #
#  Add password in payload to this script to run#
#################################################

payload = {
	"username": "kmgh0692", 
	"password": "", 
	"csrfmiddlewaretoken": "oZTcp9kVJA/lPMtmsn9zkq6Iw0B6Jp5IWpl68ZLAVXeSQkGVKLmdn732MFgqX+Jw"
        "User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
}


session_requests = requests.session()
#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
###################################
# To remove ssl certificate error #
###################################
session_requests.verify = False

login_url = "https://self.sso.infra.ftgroup/AuthForm/redirect.jsp?RETURN=http%3A//portal-kod.sso.infra.ftgroup/login/login"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='SMAGENTNAME']/@value")))[0]

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

##############################
# scraping content           #
##############################

url = 'http://portal-kod.sso.infra.ftgroup/activite/index'
result = session_requests.get(
	url,
        allow_redirects=True,
	headers = dict(referer = url)
)

tree = html.fromstring(result.content)
#bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

print tree.text
print tree.xpath("//div[@class='innerCalendrier']")

#result.ok # Will tell us if the last request was ok
#result.status_code # Will give us the status from the last request
