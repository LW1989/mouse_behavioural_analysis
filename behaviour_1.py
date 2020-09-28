# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import pandas as pd

#load xls file with behavioural data
df= pd.read_excel('C:/Users/Lutz/Desktop/Data Science/Behavior_Analysis/Beispiel_Export_Noldus_OFT.xlsx')

#remove leading and ending spaces from "light conditions" in order to be able to filter them 
for i in range(0,len(df['Light Condition'])):
    #print(df['Light Condition'].iloc[i])
    df['Light Condition'].iloc[i]=df['Light Condition'].iloc[i].strip()
    
# Define filtering e.g. Optogenetics vs. Control and/or Light Off vs. Light On 
    
filter_injection_log=True #Set to True if you want to filter by injection type (e.g. control vs. ChR2)
filter_light_condition_log=False #Set to True if you want to filter by light condition type (e.g. On vs. Off)
filter_date_of_experiment_log=False #Set to True if you want to filter by date of experimente (i.e. same cohort of animals)

#For all filters, check if spelling is the same as in original xls file
if filter_injection_log==True:
    filter_injection_1='Virus'
    filter_injection_2='Control'
    
if filter_light_condition_log==True:
    filter_light_condition_1='light_off_1'
    filter_light_condition_2='light_on_1'
    filter_light_condition_3='light_off_2'
    filter_light_condition_4='light_on_2'

if filter_date_of_experiment_log==True:
    filter_date_of_experiment=''



if filter_injection_log==True and filter_light_condition_log==False and filter_date_of_experiment_log==False:
    bo_injection_1=df['Injection']==filter_injection_1
    bo_injection_2=df['Injection']==filter_injection_2
elif filter_injection_log==True and filter_light_condition_log==False and filter_date_of_experiment_log==True:
    bo_injection_1_date=df['Injection']==filter_injection_1 & (df['Date of Experiment']==filter_date_of_experiment)
    bo_injection_2_date=df['Injection']==filter_injection_2 & (df['Date of Experiment']==filter_date_of_experiment)
elif filter_injection_log==True and filter_light_condition_log==True and filter_date_of_experiment_log==False:
    bo_injection1_light1=(df['Injection']==filter_injection_1) & (df['Light Condition']==filter_light_condition_1)
    bo_injection1_light2=(df['Injection']==filter_injection_1) & (df['Light Condition']==filter_light_condition_2)
    bo_injection1_light3=(df['Injection']==filter_injection_1) & (df['Light Condition']==filter_light_condition_3)
    bo_injection1_light4=(df['Injection']==filter_injection_1) & (df['Light Condition']==filter_light_condition_4)
    bo_injection2_light1=(df['Injection']==filter_injection_2) & (df['Light Condition']==filter_light_condition_1)
    bo_injection2_light2=(df['Injection']==filter_injection_2) & (df['Light Condition']==filter_light_condition_2)
    bo_injection2_light3=(df['Injection']==filter_injection_2) & (df['Light Condition']==filter_light_condition_3)
    bo_injection2_light4=(df['Injection']==filter_injection_2) & (df['Light Condition']==filter_light_condition_4)
elif filter_injection_log==True and filter_light_condition_log==True and filter_date_of_experiment_log==True:
    bo_injection1_light1_date=(df['Injection']==filter_injection_1) & (df['Light Condition']==filter_light_condition_1) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_injection1_light2_date=(df['Injection']==filter_injection_1) & (df['Light Condition']==filter_light_condition_2) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_injection1_light3_date=(df['Injection']==filter_injection_1) & (df['Light Condition']==filter_light_condition_3) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_injection1_light4_date=(df['Injection']==filter_injection_1) & (df['Light Condition']==filter_light_condition_4) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_injection2_light1_date=(df['Injection']==filter_injection_2) & (df['Light Condition']==filter_light_condition_1) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_injection2_light2_date=(df['Injection']==filter_injection_2) & (df['Light Condition']==filter_light_condition_2) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_injection2_light3_date=(df['Injection']==filter_injection_2) & (df['Light Condition']==filter_light_condition_3) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_injection2_light4_date=(df['Injection']==filter_injection_2) & (df['Light Condition']==filter_light_condition_4) & (df['Date of Experiment']==filter_date_of_experiment)
elif filter_injection_log==False and filter_light_condition_log==True and filter_date_of_experiment_log==True:
    bo_light_condtiton_1_date=(df['Light Condition']==filter_light_condition_1) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_light_condtiton_2_date=(df['Light Condition']==filter_light_condition_2) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_light_condtiton_3_date=(df['Light Condition']==filter_light_condition_3) & (df['Date of Experiment']==filter_date_of_experiment)
    bo_light_condtiton_4_date=(df['Light Condition']==filter_light_condition_4) & (df['Date of Experiment']==filter_date_of_experiment)
else:
    bo_light_condtiton_1=(df['Light Condition']==filter_light_condition_1)
    bo_light_condtiton_2=(df['Light Condition']==filter_light_condition_2)
    bo_light_condtiton_3=(df['Light Condition']==filter_light_condition_3)
    bo_light_condtiton_4=(df['Light Condition']==filter_light_condition_4)
    
    
  
    
      # light_condition_off_1=(df['Light Condition']=='Light_off_1') & (df['Injection']=='Virus')
# light_condition_on_1=df['Light Condition']=='Light_on_1'
#light_condition_off_2=df['Light Condition']=='Light_off_2'
#light_condition_on_2=df['Light Condition']=='Light_on_2'

# test =df['In_Center_Duration'][light_condition_off_1].mean()
# test_1 =df['In_Center_Duration'][light_condition_on_1]
# print(test_1)

# type(test_1)
#print(light_condition_off_1)
#print(light_condition_off_2)
#print(light_condition_on_1)
# print(light_condition_on_2)