# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:47:48 2021

@author: cinde
"""
# %% set up NLTK package
#!python -m nltk.downloader popular
#import nltk

#nltk.download('punkt')


from nltk.tokenize import sent_tokenize
import os
import pandas as pd

# %% 

# %% Set up working folder and test its existence
# For better examples: https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html

folder='c:\\users\\cinde\\Documents'
exist=os.path.exists(folder)
print(exist)

# %% Load the text file to a string variable
file=open(folder+"/AAPL7A.txt",'r')
text=file.read()

print(text[0:500])

# %% Tokenize 

sentences = sent_tokenize(text)

# %% Save the processed file
df=pd.DataFrame(sentences)

df.to_csv(folder+"//aapl7a_processed.csv")