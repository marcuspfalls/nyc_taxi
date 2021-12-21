import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

input = pd.read_csv('tlc_yellow_trips_2018_11_22_CLEAN.csv')

np.set_printoptions(threshold=sys.maxsize)
pd.set_option('display.max_columns', None)

input = input[input['tip_amount']>0]
input = input[input['payment_type']==1.]

input['total_notip'] = input['total_amount'] - input['tip_amount']
input['tip_ratio'] = input['tip_amount']*100/input['total_notip']

def remove_outliers(df, key):
    q1 = df[key].quantile(q=0.25)
    q3 = df[key].quantile(q=0.75)
    df = df[df[key] > (q1 - 3. * (q3 - q1))]
    df = df[df[key] < (q3 + 3. * (q3 - q1))]
    return df

input = remove_outliers(input,'tip_ratio')
input = remove_outliers(input,'tip_amount')

plt.scatter(input['total_notip'], input['tip_ratio'], s=1)
plt.ylabel('Tip to Cost Ratio (%)')
plt.xlabel('Total Cost Excluding Tips ($)')
plt.show()

plt.scatter(input['total_notip'], input['tip_amount'], s=1)
plt.ylabel('Tip Amount ($)')
plt.xlabel('Total Cost Excluding Tips ($)')
plt.show()
