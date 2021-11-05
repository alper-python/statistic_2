import pandas as pd
import numpy as np
import scipy.stats as st

Data = pd.read_csv('titanic2.csv')

'''
Some new survey/research claims that the average age of passengers in Titanic who survived is greater than 28.
H0: Average age of passengers in Titanic is less than 28:μ0 <=28
HA : New research claims mean age is greater than 28: μ1 > 28
'''
younger_20_sample = np.array([np.mean(Data[Data["age"] <= int('28')].sample(20)["survived"].values) for i in range(100)])
older_20_sample = np.array([np.mean(Data[Data["age"] > int('28')].sample(20)["survived"].values) for i in range(100)])

mean_younger_20 = round(np.mean(younger_20_sample),4)
print("younger_20 mean: ",mean_younger_20)

mean_older_20 = round(np.mean(older_20_sample),4)
print("older_20 mean: ",mean_older_20)

effect_of_class = round(mean_younger_20 - mean_older_20,4)
print("Effect of Class: ",effect_of_class)

sigma_younger = np.std(younger_20_sample)
sigma_older = np.std(older_20_sample)
sigma_difference = np.sqrt((sigma_younger**2)/len(younger_20_sample)  +  (sigma_older**2)/len(older_20_sample))
z_score = effect_of_class / sigma_difference
print("Z-score: ",round(z_score,2))

p_value = st.norm.sf(abs(z_score))*2
print("P_value :",round(p_value,2))

'''
* Eğer p-value > 0.01(level of significance) fail to reject
'''
if p_value < 0.05:
    print("reject to Null Hypothesis")
else:
    print("fail to reject")