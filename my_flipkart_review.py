# coded by U.kiranvas Reddy

from StringIO import StringIO
import yaml
import pycurl



html = StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'https://www.flipkart.com/api/3/page/dynamic/product-reviews')
c.setopt(c.POSTFIELDS, '{"requestContext":{"productId":"ACCEHYGMDJHN7AXK"}}')
c.setopt(c.HTTPHEADER, ['User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0','Accept: */*','Accept-Language: en-GB,en;q=0.5','x-user-agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0 FKUA/website/41/website/Desktop','Content-Type: application/json','Connection: keep-alive'])
c.setopt(c.WRITEFUNCTION, html.write)
c.perform()
c.close()

data=html.getvalue()


data1 = yaml.load(data)



import csv

with open('data.csv','w') as file:
	for count in range(3):
		pp=data1["RESPONSE"]["data"]["product_review_page_default_1"]["data"][count]
		pp1=pp['value']['author']+", "+pp['value']['text']+"\n"
		file.write(str(pp1))
file.close



