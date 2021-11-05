import pandas as pd
import numpy as np
import scipy.stats as st


Data = pd.read_csv('titanic2.csv')
'''
H0 hypothesis Human socio-economic class has no effect on survival rates in the Titanic crash
HA hypothesis that people's socio-economic classes in the Titanic crash have no effect on survival rates.
'''
#merkezi limit teoremi ile 100 kişi üzerinden bir örneklem ediniyoruz.
'''
bu kıyaslamayı 'First' ve 'Third' Class'lar için yaparak bulabiliriz.
Merkezi limitleme teoremi ile 100 popülasyonluk bir datadan 20 puanlık bir sampling oluşturuyoruz.

'''
First_Class_Sample = np.array([np.mean(Data[Data["class"] =='First'].sample(20)["survived"].values) for i in range(100)])
third_Class_Sample = np.array([np.mean(Data[Data["class"] =='Third'].sample(20)["survived"].values) for i in range(100)])

#Bu sample lara ait mean'ler
mean_first_class_sample = round(np.mean(First_Class_Sample),4)
print("First Class mean: ",mean_first_class_sample)

mean_third_class_sample = round(np.mean(third_Class_Sample),4)
print("Second Class mean: ",mean_third_class_sample)

#Class'ların etkisi
effect_of_class = round(mean_first_class_sample - mean_third_class_sample,4)
print("Effect of Class: ",effect_of_class)

'''
Bu etkinin gerçek olup olmadığını (şans eseri veya rastgele olabilir) Z testi ile kontrol etmemiz gerekir.
Z-testi ve Z-score yapılacak.
Z-score ile bir değerin ortalamadan ne kadar bir standart sapma yaptığını gösterir.
'''
#Z-score hesaplama
'''
(first_class_mean - third_class_mean) / iki popülasyon arasındaki farkların dağılımının standard sapması
'''
# iki popülasyon arasındaki farkların dağılımının standard sapmasını hesaplama
'''
first class numune dağılımının standart sapmasının karesi/first class numune dağılım'ın uzunluğu ile
Third class numune dağılımının standart sapmasının karesi/third class numune dağılım'ın uzunluğu toplamının
karekökü
'''
# yani
sigma_first = np.std(First_Class_Sample)
sigma_third = np.std(third_Class_Sample)
sigma_difference = np.sqrt((sigma_first**2)/len(First_Class_Sample)  +  (sigma_third**2)/len(third_Class_Sample))
z_score = effect_of_class / sigma_difference
print("Z-score: ",round(z_score,2))

#P-value değerini bulma
'''
P-value değeri : scipy.stats.norm.sf(abs(z_score))
ile bulunur
'''
p_value = st.norm.sf(abs(z_score))*2
print("P_value :",p_value)

'''
p_value: 3.03e-190 çıkıyor.
significance level of 0.05 dan çok çok küçük bir değer olduğu için;
rejecting the Null hypothesis.
'''
