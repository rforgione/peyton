import csv
import re
import pandas as pd
import numpy as np


def data_scrub(playoffs=False):
	# regex patterns denoting subtotal and column title lines
	# to be excluded from the data set
	p1 = re.compile('^Passing')
	p2 = re.compile('^Rk')
	p3 = re.compile('^(\d+ Games)')
	pdata = pd.DataFrame()

	if playoffs:
		datafile = 'peyton_playoffs2.csv'
	else:
		datafile = 'peyton_reg.csv'

	with open(datafile, 'rb') as csvfile:
		data = csv.reader(csvfile)
		for row in data:
			if not p1.search(''.join(row)) and not p2.search(''.join(row)) and \
													not p3.search(''.join(row)):
				pdata = pdata.append(pd.Series(row), ignore_index=True)
	
	if playoffs:
		pdata.columns = ['Rk', 'Year', 'GNum', 'Date', 'Age', 'Tm', 'At',
						 'Opp', 'Result', 'GS', 'Cmp', 'Att', 'CmpPct', 'Yds',
						 'TD', 'Int', 'Rate', 'YA', 'AYA', 'RushAtt', 'RushYds', 'RushYA',
						 'RushTD', 'RushTD2','RushPTS']
	else:
		pdata.columns = ['Rk', 'Year', 'GNum', 'Date', 'Age', 'Tm', 'At',
						 'Opp', 'Result', 'GS', 'Cmp', 'Att', 'CmpPct', 'Yds',
						 'TD', 'Int', 'Rate', 'YA', 'AYA', 'RushAtt', 'RushYds', 'RushYA',
						 'RushTD', 'Rec', 'Tgt', 'Yds', 'YR', 'RecTD', 'TotTD',
						 'TotPts', 'Sk', 'Tkl', 'Ast']
	return pdata

