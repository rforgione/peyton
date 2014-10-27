from nose.tools import *
import data_scrub as ds
import numpy as np

def test_reg_dataframe_rows():
	g = ds.data_scrub()
	assert_equal(g.shape[0], 247)

def test_reg_dataframe_cols():
	g = ds.data_scrub()
	assert_equal(g.shape[1], 33)

def test_playoff_rows():
	pass

def test_playoff_cols():
	pass

def test_Rk_type():
	g = ds.data_scrub()
	assert_equal(type(g.Rk[0]), np.int64)

