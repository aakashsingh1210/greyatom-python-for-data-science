# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census=np.concatenate((data,new_record))
age=census[:,0]
max_age=np.max(age)
min_age=np.min(age)
age_mean=(max_age+min_age)/2
age_std=np.std(age)
race=census[:,2]
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
if len_0==min(len_0,len_1,len_2,len_3,len_4):
    minority_race=0
elif len_1==min(len_0,len_1,len_2,len_3,len_4):
    minority_race=1
elif len_2==min(len_0,len_1,len_2,len_3,len_4):
    minority_race=2
elif len_3==min(len_0,len_1,len_2,len_3,len_4):
    minority_race=3
else:
    minority_race=4
senior_citizens=census[census[:,0]>60]#masking
working_hours_sum=sum(senior_citizens[:,6])
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=(high[:,7]).mean()
avg_pay_low=(low[:,7]).mean()
print(avg_pay_high)
print(avg_pay_low)


