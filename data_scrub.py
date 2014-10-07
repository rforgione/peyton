import csv
import re
import pandas as pd
import numpy as np


def data_scrub():
	p1 = re.compile('^Passing')
	p2 = re.compile('^Rk')
	pdata = pd.DataFrame()

	with open('peyton_playoffs2.csv', 'rb') as csvfile:
		data = csv.reader(csvfile)
		for row in data:
			if not p1.search(''.join(row)) and not p2.search(''.join(row)):
				pdata = pdata.append(pd.Series(row), ignore_index=True)

	pdata.columns = ['Rk', 'Year', 'GNum', 'Date', 'Age', 'Tm', 'At',
					 'Opp', 'Result', 'GS', 'Cmp', 'Att', 'CmpPct', 'Yds',
					 'TD', 'Int', 'Rate', 'YA', 'AYA', 'RushAtt', 'RushYds', 'RushYA',
					 'RushTD', 'RushTD2','RushPTS']
	return pdata

