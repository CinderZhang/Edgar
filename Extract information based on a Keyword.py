# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:09:42 2021

@author: xz035
"""
import re

lines = '''<P style="TEXT-ALIGN: left"><FONT size=2 face=Arial>The energy sector also featured several detractors from performance. Global exploration and production company </FONT><B><FONT size=2 face=Arial>Occidental Petroleum </FONT></B><FONT size=2 face=Arial>fell sharply in March as the company was forced to slash its spending projections in the wake of the Saudi-Russian oil market share battle, which sent crude prices lower. The stock finished the year as a significant absolute and relative detractor, and we trimmed most of our position in recognition of the changing risk profile of the investment brought on by the pandemic. </FONT><B><FONT size=2 face=Arial>ExxonMobil </FONT></B><FONT size=2 face=Arial>suffered from operational headwinds related to the coronavirus pandemic, which adversely impacted the company&#8217;s near-term earnings power. However, our underweight in the name benefited relative returns for the year.</FONT></P>
    <P style="TEXT-ALIGN: left"><FONT size=2 face=Arial>Elsewhere in the portfolio, shares of </FONT><B><FONT size=2 face=Arial>Tyson Foods </FONT></B><FONT size=2 face=Arial>declined early in the period due to input cost inflation and broader market uncertainty stemming from the coronavirus pandemic, which hampered exports to China and shifted demand to residential use from food services. Industry-wide price-fixing allegations also pressured shares of chicken companies during the period. We are optimistic that improving chicken fundamentals will drive the stock higher over the near term. Shares of </FONT><B><FONT size=2 face=Arial>Boeing </FONT></B><FONT size=2 face=Arial>suffered amid delays in the 737 MAX recertification process and pressure on air travel from coronavirus fears. While we continue to find Boeing shares attractive, we are cognizant of the uncertain near-term recovery path of global air travel post-pandemic and, therefore, largely kept our position flat in the name throughout the year.</FONT></P>
    <P style="TEXT-ALIGN: left"><FONT size=2 face=Arial>Some of the portfolio&#8217;s largest absolute contributors came from the information technology sector. Shares of </FONT><B><FONT size=2 face=Arial>Qualcomm </FONT></B><FONT size=2 face=Arial>rebounded from the first-quarter sell-off, rising considerably for the one-year period due to the company&#8217;s strong position in 5G cellular technology. During the period, the company was able to resolve all its remaining licensing disputes, thereby stabilizing that business and leaving investors to focus on its earnings growth runway as 5G devices proliferate. Shares of </FONT><B><FONT size=2 face=Arial>Microsoft </FONT></B><FONT size=2 face=Arial>rose as the company reported robust growth within its Intelligent Cloud segment. Investors appeared to prioritize Microsoft&#8217;s solid fundamentals, defensible business model, and attractive growth potential. We trimmed both positions throughout the year on strength.</FONT></P>
'''
keyword = "optimistic"

sentences = re.split('(\<P|\<P\>)', lines)

#sentences_terminated = [a + b for a,b in zip(sentences[0::2], sentences[1::2])]

# print(sentences_terminated)

for line in sentences:
    if keyword in line:
        print(line)
