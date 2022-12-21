import json
import urllib.request
import string
import random 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

count = 50
i = 0
ids = []
API_KEY = 'key goes here'
randomhash = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,randomhash)
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
results = json.loads(data.decode(encoding))

for data in results['items']:
    videoId = (data['id']['videoId'])
    ids.append(videoId)
    i = i + 1

#print(ids)
#print(i)

while True:
    flag = "Maybe"
    number = random.randint(0,50)
    flag = input("Would you like a random youtube video?(Yes,No) ")
    if flag == "Yes":
        youtubeURL = "https://www.youtube.com/watch?v={}".format(ids[number])
        #print(youtubeURL)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(youtubeURL)
    if flag == "No":
        print("Enjoy your day!")
        break


