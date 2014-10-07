import csv
import re
import pandas as pd
import numpy as np


def data_scrub():
	pattern = re.compile('^,+')
	pdata = pd.DataFrame()

	with open('peyton_playoffs.csv', 'rb') as csvfile:
		data = csv.reader(csvfile)
		for row in data:
			if not pattern.search(' '.join(row)):
				pdata.append(row, ignore_index=True)
	return pdata

