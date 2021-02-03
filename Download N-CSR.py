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
import re

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
for i in NCSR.index:
    ## 5. Download a N-CSR file
    filing = NCSR['Filename'][i]
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


# %% remove html and xbrl tags

# define a function
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# %% read in  a filing
file = open(r"C:\Edgar\filing\0001193125-20-067363.txt",'r')
str = file.read()

# %% clean it up
notag = remove_html_tags(str)

kw=re.findall("[^.]*Gamestop[^.]*\.",notag,re.IGNORECASE)

print(kw)
