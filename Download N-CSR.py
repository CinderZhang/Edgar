# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Data Source
# ## Edgar
# ### Master index
# * [Detailed instruction](sec.gov/edgar/searchedgar/accessing-edgar-data.htm)
# * [Current year Master file .txt file](https://www.sec.gov/Archives/edgar/full-index/master.idx)
# * [Current Year for crawler-difference between master and crawler: *crawler shows full link .html*](https://www.sec.gov/Archives/edgar/full-index/crawler.idx)
# * [Historical](https://www.sec.gov/Archives/edgar/full-index/)
# 
# [log file](https://www.sec.gov/dera/data/edgar-log-file-data-set.html)
# 
# [Accessing Edgar Data](https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm)
# 
# [WRDS SEC Analytics Suite](https://wrds-web.wharton.upenn.edu/wrds/tools/variable.cfm?library_id=124)
# 
# [Norte Dame-Linux Setting](https://sraf.nd.edu/textual-analysis/) 
# 
# [MIT OpenEDGAR--Cloud Setting--A great overview of Edgar system](https://law.mit.edu/pub/openedgar/release/1)
# 
# * * Edgar filing plain textual
# * * textual analysis code
# 
# ### Packages
# * [edgar package](https://github.com/joeyism/py-edgar)
# * * [Need to download C++ development tools--Make sure to check C++ during the installation](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)
# 
# * [Edgar official site Developer Resources](https://www.sec.gov/developer)
# 
# * [py-sec-edgar- ** A Better documented package **]
# * * [Website](https://py-sec-edgar.readthedocs.io/en/latest/)
# * * [Github link](https://github.com/ryansmccoy/py-sec-edgar)
# 
# * [sec-api.io- **Cross platform package: Python, Google Sheet and HTTP**](https://sec-api.io/docs#stream-python)
# 
# * University hosted
# * * [MIT OpenEDGAR--A great overview of Edgar system](https://law.mit.edu/pub/openedgar/release/1) 
# * * [Norte Dame-Code and Data](https://sraf.nd.edu/textual-analysis/)
# 
# ### Examples
# 
# * [Mutual fund NSAR-Note that CIK maps to multiple tickers](https://www.sec.gov/Archives/edgar/data/1040612/000120928620000203/0001209286-20-000203-index.htm)
# 
# 
# 
# 
# ## IP Address
# 
# [IP mapping-Paid Subscription](https://github.com/ipinfo/python)
# 
# [Link Table-Free](https://iptoasn.com/)
# 
# [Super informative article and information](https://securitytrails.com/blog/asn-lookup)
# 

# %%
# old fashion example
## import Python packages
from io import BytesIO
import os
from os import path
from zipfile import ZipFile
import pandas as pd
import numpy as np
import requests
import sqlite3
from sqlite3 import Error
import urllib3


# %%
#Set up working folder
WorkingDir="c:\\Edgar\\"


# %%
# download the crawler.Inx from Edgar
## 1. feed crawler.Idx URL
master_url="https://www.sec.gov/Archives/edgar/full-index/master.idx"
master=pd.read_csv(master_url, skiprows=10, names=['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename'], sep='|', engine='python', parse_dates=True)
print(master.head())


# %%
## 2. take care of the error
master = master[-master['CIK'].str.contains("---")]
print(master.head())


# %%
## 3. drop rows with missing value
master = master.dropna(axis=0,subset=['CIK','Form Type','Filename'])


# %%
## 3. Filter out the N-CSR... forms
NCSR=master[master['Form Type'].str.contains("N-CSR")]
NCSR.reset_index(inplace=True,drop=True)
print(NCSR.head())


# %%
## 4. Save the N-CSR list file as excel
outfile=WorkingDir+"data\\NCSR.xlsx"
NCSR.to_excel(outfile,sheet_name='N-CSR',index=False)


# %%
## 5. Download a N-CSR file
filing = NCSR['Filename'][0]
print(filing)


# %%
## 6. Full url
filingURL="https://www.sec.gov/Archives/"+filing
print(filingURL)


# %%
#7. Download the file
http=urllib3.PoolManager()
filingText=http.request('GET',filingURL)
#filingText.data


# %%
# 8. Save the filing
filename=filingURL.rsplit('/', 1)[-1]
outfiling = WorkingDir+"filing\\"+filename
print(outfiling)
open(outfiling,'wb').write(filingText.data)

""" 
# %%
filingURL.rsplit('/', 1)[-1]


# %%
### Cannot install edgar package without C++...

from edgar import Company
company = Company("Oracle Corp", "0001341439")
tree = company.get_all_filings(filing_type = "10-K")
docs = Company.get_documents(tree, no_of_documents=5)
tree


# %%
docs


# %%
## SEC API . IO
##########################
# Python 3.x Example
##########################

# package used to execute HTTP POST request to the API
import json
import urllib.request

# API Key
TOKEN = "4940b22a39296c21b420ebc6fadfd036c64971142eb0e2340210a1fc61ef5650" # replace YOUR_API_KEY with the API key you got from sec-api.io after sign up
# API endpoint
API = "https://api.sec-api.io?token=" + TOKEN

# define the filter parameters you want to send to the API 
payload = {
  "query": { "query_string": { "query": "cik:320193 AND filedAt:{2016-01-01 TO 2016-12-31} AND formType:\"10-Q\"" } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

# format your payload to JSON bytes
jsondata = json.dumps(payload)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes

# instantiate the request 
req = urllib.request.Request(API)

# set the correct HTTP header: Content-Type = application/json
req.add_header('Content-Type', 'application/json; charset=utf-8')
# set the correct length of your request
req.add_header('Content-Length', len(jsondataasbytes))

# send the request to the API
response = urllib.request.urlopen(req, jsondataasbytes)

# read the response 
res_body = response.read()
# transform the response into JSON
filings = json.loads(res_body.decode("utf-8"))

# print JSON 
print(filings)


# %%



 """