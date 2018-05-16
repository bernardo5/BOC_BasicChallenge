import requests
from requests.auth import HTTPBasicAuth
from StringIO import StringIO
from PIL import Image
import profile

def getImage(devId):
	response=requests.get('https://wad-challenge-2018.boc-cloud.com/rest/dev/models/'+devId, auth=('WeAreDevelopers', 'YesWeAre'), headers={'Authorization': 'TOK:aaa6195f-fa9b-42d9-af14-915abaec20e7'})
	print response
	return response

def createImage(response):
	if response.status_code == requests.codes.ok:
		myImage=Image.open(StringIO(response.content))
		myImage.save('basic.png')
	else:
		print 'error constructing image'

def sendCode(devId, codeToSend):
	response = requests.post("https://wad-challenge-2018.boc-cloud.com/rest/dev/developers/"+devId+"/codes", data={'code': codeToSend}, auth=('WeAreDevelopers', 'YesWeAre'), headers={'Authorization': 'TOK:aaa6195f-fa9b-42d9-af14-915abaec20e7'})
	if response.status_code==requests.codes.ok:
		print response.text


devId='aaa6195f-fa9b-42d9-af14-915abaec20e7'
option='1'
while option!='3':
	option = raw_input("type 1 to fetch image, the code or quit to quit the program: ")
	if option=='1':
		print '1'
		createImage(getImage(devId))
	elif option=='quit':
		print 'quit'
		exit(0)
	else:
		print 'other'
		sendCode(devId, option.strip())
	