import requests

if __name__=='__main__':
   response = requests.get("https://foofish.net")
   print response.ststus_code
