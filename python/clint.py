import requests,json

postdata = json.dumps({'name':'rerererererere'})
print(postdata)
r = requests.Session().post("http://127.0.0.1:9601",data=postdata.encode("utf-8"), headers={'Content-Type': 'application/x-www-form-urlencoded'})
print(r)
print(r.text)
