import requests
r=requests.get("https://www.google.com.ar")
with open("index.html", "wb") as f:
	f.write(r.content)
r.close()



