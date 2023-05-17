# importing libraries
import pandas as pd
from pprint import pprint

data = pd.read_csv('./sample_data.csv')
pprint(data)
pprint(dict(zip(data.C, {data.W1,data.W2,data.W3,data.W4})))