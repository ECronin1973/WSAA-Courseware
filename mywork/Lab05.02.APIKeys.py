import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://en.wikipedia.org"

apiKey = cfg["htmltopdfkey"]
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl, 'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl + "?" + parsedparams

try:
    response = requests.get(requestUrl)
    response.raise_for_status()  # Raise an error for bad status codes
    print(response.status_code)
    
    result = response.content
    with open("document.pdf", "wb") as handler:
        handler.write(result)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except IOError as e:
    print(f"File operation failed: {e}")