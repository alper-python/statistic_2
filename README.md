# statistic_2

## Seaborn kütüphanesi içerisinde bulunan titanic datasını kullanarak,
```
# pip install seaborn
# seaborn kutuphanesini ustteki kod ile yukluyoruz
import seaborn as sns
titanic= sns.load_dataset('titanic')
df = titanic.copy()
print(df.head())
#kodlar araciligi ile titanic datasini yukluyoruz
```

## Hipotez Testleri:
## Test 1
```
H0 hipotezi Titanik kazasında insanlarin sosyo ekonomik siniflari hayatta kalma oranlarına herhangi bir etkisi yoktur
HA hipotezi Titanik kazasında insanlarin sosyo ekonomik siniflari hayatta kalma oranlarına herhangi bir etkisi vardır.
```
## Test2 
```
Some new survey/research claims that the average age of passengers in Titanic who survived is greater than 28.
H0: Average age of passengers in Titanic is less than 28:μ0 <=28
HA : New research claims mean age is greater than 28: μ1 > 28
```
## Test 3
```
There is a difference in average age between the two genders who survived?
H0:No difference in mean age of male & female passengers who survived: μ_male =μ_female or μ_male-μ_female=0
HA:There is difference in mean age of male & female passengers who survived μ_male <> μ_female or μ_male-μ_female <> 0
```
## Test 4
```
Greater than 50% of passengers who survived in Titanic are in the age group of 20–40.
H0: p ≤ 0.5, Less than 50% of passengers who survived in Titanic are in the age group of 20–40
H1:p > 0.5 , Greater than 50% of passengers who survived in Titanic are in the age group of 20–40.
```
## Test 5
```
Greater than 50% of passengers in Titanic are in the age group of 20–40 ( including both survived and non-survived passengers)
```


Hipotez test asamalarinin tamamini yukarda önerilen hipotez icin uygulayınız ve sonucu yorumlayiniz.
