## 3. Condensing the Class Size Data Set ##

class_size = data["class_size"]
class_size = class_size[class_size["GRADE "] == "09-12"]
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]
print(class_size.head())

## 5. Computing Average Class Sizes ##

import numpy
class_size= class_size.groupby("DBN").agg(numpy.mean)

class_size.reset_index(inplace=True)

data["class_size"] =class_size 
 
print(data["class_size"].head())

## 7. Condensing the Demographics Data Set ##

demographics = data["demographics"]
demographics= demographics[demographics["schoolyear"]==20112012]
data["demographics"] = demographics
print( data["demographics"].head())

## 9. Condensing the Graduation Data Set ##

graduation= data["graduation"]

graduation = graduation[graduation["Cohort"]=='2006']
graduation = graduation[graduation["Demographic"]=="Total Cohort"]
data["graduation"]  = graduation

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

ap_2010  = data["ap_2010"]

for i in cols:
    ap_2010[i] = pd.to_numeric(ap_2010[i], errors="coerce")
    
ap_2010[cols].dtypes 

## 12. Performing the Left Joins ##

combined = data["sat_results"]
ap_2010= data["ap_2010"]

combined = combined.merge(ap_2010 , on="DBN" , how="left")

graduation = data["graduation"]

combined = combined.merge(graduation , on="DBN" , how="left")

combined.shape

## 13. Performing the Inner Joins ##

class_size =data["class_size"]
demographics =data["demographics"]
survey =data["survey"]
hs_directory  =data["hs_directory"]
combined  = combined.merge(class_size,how="inner",on="DBN")
combined  = combined.merge(demographics,how="inner",on="DBN")
combined  = combined.merge(survey,how="inner",on="DBN")
combined  = combined.merge(hs_directory,how="inner",on="DBN")

combined.shape

## 15. Filling in Missing Values ##

combined_mean = combined.mean()
combined= combined .fillna(combined_mean)
combined= combined .fillna(0)

combined.head(5)

## 16. Adding a School District Column for Mapping ##

def exttwo(x):
    return x[0:2]

combined["school_dist"] = combined["DBN"].apply(exttwo)
combined["school_dist"] 
