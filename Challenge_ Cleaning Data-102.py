## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = avengers[avengers['Year'] > 1959]

true_avengers['Year'].hist()

## 5. Consolidating Deaths ##

def countd(row):
    count=0
    if row['Death1'] =="YES":
        count = count+1
    if row['Death2'] =="YES":
        count = count+1
        
    if row['Death3'] =="YES":
        count = count+1
        
    if row['Death4'] =="YES":
        count = count+1
     
    if row['Death5'] =="YES":
        count = count+1
        
    return count 


true_avengers['Deaths'] = true_avengers.apply(countd, axis=1)
        

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)