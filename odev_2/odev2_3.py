import pandas as pd
import numpy as np
import scipy.stats as st

Data = pd.read_csv('titanic2.csv')
'''
There is a difference in average age between the two genders who survived?
H0:No difference in mean age of male & female passengers who survived: μ_male =μ_female or μ_male-μ_female=0
HA:There is difference in mean age of male & female passengers who survived μ_male <> μ_female or μ_male-μ_female <> 0
'''
male_sample = np.array([np.mean(Data[Data["sex"] == "male"].sample(20)["survived"].values) for i in range(100)])
female_sample = np.array([np.mean(Data[Data["sex"] == "female"].sample(20)["survived"].values) for i in range(100)])

mean_male_sample = round(np.mean(male_sample),4)
print("male mean: ",mean_male_sample)

mean_female_sample = round(np.mean(female_sample),4)
print("female mean: ",mean_female_sample)

effect_of_class = round(mean_male_sample - mean_female_sample,4)
print("Effect of Class: ",effect_of_class)

sigma_male = np.std(male_sample)
sigma_female = np.std(female_sample)
sigma_difference = np.sqrt((sigma_male**2)/len(male_sample)  +  (sigma_female**2)/len(female_sample))
z_score = effect_of_class / sigma_difference
print("Z-score: ",round(z_score,2))

p_value = st.norm.sf(abs(z_score))*2
print("P_value :",round(p_value,2))

if p_value < 0.05:
    print("reject to Null Hypothesis")
else:
    print("fail to reject")