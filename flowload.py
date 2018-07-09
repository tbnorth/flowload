import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import stats

lds = pd.read_csv("Grand_MuskegonHistoricalLoadings.csv", sep='[, ]')

lds.set_index('Year', inplace=True)
yrs = pd.read_csv("grand_flow.csv")
yrs.set_index('year', inplace=True)

lds = pd.concat([lds, yrs], axis=1, join='inner')

lds.apply(lambda x: plt.text(x.flow, x.TP_Grand_MT, x.name), axis=1)

plt.scatter(lds.flow, lds.TP_Grand_MT)
plt.show()


