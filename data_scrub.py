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
						 'RushTD', 'SkillTD','SkillPts']

	else:
		pdata.columns = ['Rk', 'Year', 'GNum', 'Date', 'Age', 'Tm', 'At',
						 'Opp', 'Result', 'GS', 'Cmp', 'Att', 'CmpPct', 'Yds',
						 'TD', 'Int', 'Rate', 'PassYA', 'PassAYA', 'RushAtt', 'RushYds', 'RushYA',
						 'RushTD', 'Rec', 'Tgt', 'RecYds', 'YPRec', 'RecTD', 'SkillTD',
						 'SkillPts', 'Sk', 'Tkl', 'Ast']

	# coerce data fields to numerical data types
	pdata.Rk = pdata.Rk.astype(int)
	pdata.Year = pdata.Year.astype(int)
	pdata.GNum = pdata.GNum.astype(int)
	pdata.Cmp = pdata.Cmp.astype(int)
	pdata.Att = pdata.Att.astype(int)
	pdata.Yds = pdata.Yds.astype(int)
	pdata.TD = pdata.TD.astype(int)
	pdata.Int = pdata.Int.astype(int)
	pdata.Rate = pdata.Rate.astype(float)
	pdata.PassYA = pdata.PassYA.astype(float)
	pdata.PassAYA = pdata.PassAYA.astype(float)
	pdata.RushAtt = pdata.RushAtt.astype(int)
	pdata.RushYds = pdata.RushYds.astype(int)
	pdata.RushYA = pdata.RushYA.apply(lambda x: float(x) if x else 0)
	pdata.RushTD = pdata.RushTD.astype(int)
	pdata.SkillTD = pdata.SkillTD.astype(int)
	pdata.SkillPts = pdata.SkillPts.astype(int)
	
	return pdata

