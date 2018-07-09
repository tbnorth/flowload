import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import stats

lds = pd.read_csv("Grand_MuskegonHistoricalLoadings.csv", sep='[, ]')

plt.scatter(lds.Year, lds.TP_Grand_MT)
plt.show()


