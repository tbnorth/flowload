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

slope, intercept, r_value, p_value, std_err = stats.linregress(lds.flow, lds.TP_Grand_MT)

site = '04119000'
lds.sort_values('flow', inplace=True)

plt.title("Site: %s r2: %s p: %s" % (site, round(r_value**2, 2), round(p_value, 2)))
plt.xlabel("Mean daily cfs")
plt.ylabel("Total P MT (annual load)")
plt.scatter(lds['flow'], lds['TP_Grand_MT'])
plt.plot(
    [lds['flow'].values[0], lds['flow'].values[len(lds)-1]],
    [lds['flow'].values[0]*slope+intercept, lds['flow'].values[len(lds)-1]*slope+intercept],
)

for i in range(2010, 2016):
    flow = yrs.loc[i]['flow']
    load = intercept+slope*flow
    plt.scatter(flow, load, c='C1')
    plt.text(flow, load, '%s  '%i, horizontalalignment='right')

plt.show()


