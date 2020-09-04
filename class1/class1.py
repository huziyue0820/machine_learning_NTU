import sys
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv', encoding = 'big5')

print(type(data))