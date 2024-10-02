import requests
import pandas as pd
import re
import json
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

URL1 = "https://www.bitcoinmarketjournal.com/ico-regulations/"
URL2="https://www.iexpats.com/cryptocurrency-tax-and-rules-by-country/"
URL3="https://icoda.io/list-of-all-crypto-exchanges/"
URL4="https://cbdctracker.org/"
URL5="https://en.wikipedia.org/wiki/Legality_of_cryptocurrency_by_country_or_territory#Detail_by_country_or_territory"
url="https://cbdctracker.org/api/currencies"

ptrn=re.compile("(<td>)|(</td>)")
changes={
"Yes":"Taxable",
"No":"Non-Taxable",
"–":"Banned",
"Allowed":"Allowed",
"Allowed, but heavily regulated":"Allowed but regulated",
"Allowed, but regulated":"Allowed but regulated",
"Allowed, but subject to future regulations":"Allowed but regulations underway",
"Allowed, but subject to future regulations":"Allowed but regulations underway",
"Allowed, but subject to future \xa0 regulations":"Allowed but regulations underway",
"Allowed/Regulated":"Allowed but regulated",
"Allowed/See note":"Allowed",
"Allowed/See Notes":"Allowed",
"Allowed/Subject to future regulations":"Allowed but regulations underway",
"Banned":"Banned", 
"Legal":"Allowed"}

changes1={"Illegal":"Illegal",
"Legal /  Banking ban":"Legal but Banking ban",
"Legal / Use discouraged by central bank":"Legal but use discouraged by central bank",
"Legal":"Legal",
"Unknown":"No Data",
"Not considered currency":"Illegal",
"Not regulated as of 2014":"Illegal",
"Legal to trade and hold /  Illegal as a payment tool, banking ban":"Legal but Banking ban",	 
"Legal to trade and hold /  Illegal as payment tool":"Legal but Banking ban",
"Legal to trade and hold":"Legal",	 
"Temporary ban on mining[147]":"Illegal",	 
"Legal to mine  Banking ban":"Legal but Banking ban",
"Ban on mining[148]":"Illegal",
"Not regulated by central bank"	:"Legal but use discouraged by central bank",
"Not regulated":"Legal but Banking ban"
}

i=1
c=0
lst=[]
lst1=[]
lst2=[]
lst3=[]
lst4=[]
lst5=[]

print("Scrapping begins.......................")
def parsing(url,tag,headers,cls_tbl=0):
	page = requests.get(url,verify=False,headers=headers)
	soup = BeautifulSoup(page.content, "html.parser")

	if cls_tbl==0:
		results=soup.find_all(tag)
	else:
		for tr in soup.find_all(cls_tbl[0],{'class':cls_tbl[1]}):
			tds = tr.find_all('td')
			for td in tds:
				lst4.append(td.text.split('\n'))
		for i in lst4:
			if len(i) == 1:
				# to remove white space
				l = i[0].lstrip()
				lst5.append(l)
			else:
				lst5.append(i[0])
		return list(zip(lst5,lst5[1:]))[::2]

	return results

results=parsing(URL1,"td",headers)
results1=parsing(URL2,"tr",headers)
results2=parsing(URL3,"tbody",headers)
results3=parsing(URL5,"td",headers,['table','wikitable'])

def website_parse(event=None,context=None):
	page = requests.get(url,verify=False,headers=headers)
	data=json.loads(page.content)


	for values in results:
		if ((i%3==0) or (i<3)):
			pass
		else:
			if c==0:
				prev=(values.text)
				c=1
			else:
				lst.append([prev,values.text])
				c=0
		i=i+1


	for values in results1:
		val=values.find_all("td")
		if len(val)!=0:
			lst1.append([re.sub(ptrn,"",str(val[0])),re.sub(ptrn,"",str(val[3]))])

	for values in results2:
		val_p=values.find_all("tr")
		for ind in range(0,len(val_p)):
			dd={}
			for i in val_p[ind]:
				if i.find('span'):
					if i.find("p"):
						dd[i.find("span").text]=i.find("p").text
					else:
						dd[i.find("span").text]=''
				else:
					dd['Exchange']=i.find("p").text
					if i.find("p"):
						dd['Exchange']=i.find("p").text
					else:
						dd['Exchange']=''
					
			lst2.append(dd)

	df_wiki = pd.DataFrame([[w.replace("\xa0", "") for w in words] for words in results3], columns=['Country', 'Status'])

	df_bitcoin=pd.DataFrame(lst,columns=['Country','Status'])
	df_iex=pd.DataFrame(lst1,columns=['Country','Status'])
	df_icod=pd.DataFrame.from_dict(lst2,orient='columns')
	df_cdbc=pd.DataFrame.from_dict(data,orient='columns')

	df_cdbc=df_cdbc[['country','status']]
	df_iex['Status']=df_iex['Status'].apply(lambda x: changes[x])
	df_bitcoin['Status']=df_bitcoin['Status'].apply(lambda x: changes[x])
	df_wiki['Status']=df_wiki['Status'].apply(lambda x: changes1[x.strip()])

	df_icod=df_icod[df_icod['Country']!='No Data']
	df_icod=df_icod[~(df_icod['Launched'].isin(['','No Data']))]

	for con in df_icod['Country'].unique():
		min_val=df_icod[df_icod['Country']==con]['Launched'].min()
		lst3.append([con,df_icod[(df_icod['Country']==con)&(df_icod['Launched']==min_val)]['Type'].values[0]])

	df_icod=pd.DataFrame(lst3,columns=['Country','Status'])


	# df_bitcoin.to_excel("bitcoinmarketjournal.xlsx",index=False)
	# df_iex.to_excel("iexpats.xlsx",index=False)
	# df_icod.to_excel("icoda.xlsx",index=False)
	# df_cdbc.to_excel("cbdctracker.xlsx",index=False)
	# df_wiki.to_excel("wiki.xlsx",index=False)

	print("Websites scrapped Successfully")