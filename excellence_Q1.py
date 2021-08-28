# import urllib library
from urllib.request import urlopen
  
# import json
import json
def func1():
  # store the URL in url as 
  # parameter for urlopen
  urlpost = "https://my-json-server.typicode.com/typicode/demo/posts"  
  # store the response of URL
  responsepost = urlopen(urlpost)  
  # storing the JSON response 
  # from url in data
  data_post_json = json.loads(responsepost.read())  
  # print the json response
  print(data_post_json)
  urlcomment = "https://my-json-server.typicode.com/typicode/demo/comments"  
  # store the response of URL
  responsecomment = urlopen(urlcomment)  
  # storing the JSON response 
  # from url in data
  data_comment_json = json.loads(responsecomment.read())  
  # print the json response
  print(data_comment_json)
  #nested for loop to check whether same ids exist and if exists, update dictionary 
  for item in data_post_json:
      for ii in data_comment_json:
          if item['id'] == ii['id']: 
              item.update(ii)
  #printing updated data after assigning the commnets to restpective posts
  #print(data_post_json)
  #returning json object
  return(json.dumps(data_post_json))

print(func1())


