import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
data=pd.read_csv(r"W:\techno_project\data\Customer_Churn.csv")
df=pd.DataFrame(data)

"""
#UNDERSTANDING DATA
#print(df.describe().to_string())
#print(df.columns)
#print(df.head(5).to_string())
#null=df['TotalCharges'].isnull().sum()                #Null values
#print(null)  
#print(df['TotalCharges'].isna() )
#(df.duplicated().sum())
#for i in df:
 #    print(i,type(i))
"""

#DATA CLEANING
df['SeniorCitizen']=pd.to_numeric(df['SeniorCitizen']) 
df['MonthlyCharges']=pd.to_numeric(df['MonthlyCharges'])
df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce') 
df['tenure']=pd.to_numeric(df['tenure']) 

#DATA VISUALISATION
font1 = {'family': 'serif','color':  'blue','size':15,'weight': 'bold'}
font2 = {'family': 'sans-serif','color':  'darkred','size':  10,'style': 'italic'}
font3 = {'family': 'monospace','color':  'black','size':  14,'weight': 'light'}
font4 = {'family': 'cursive','color':  'green','size':  16,'weight':'bold'}

#print(pd.crosstab(df['InternetService'],df['OnlineSecurity']))

#PLOT-1:
ax1=plt.subplot(1,3,1)
churn_gender=df.groupby('gender')['Churn'].value_counts(normalize=True).unstack()*100
churn_gender.plot(kind='bar',ax=ax1)
plt.title('Gender VS Churn',fontdict=font1)
plt.xlabel('Gender',fontdict=font2)
plt.ylabel('Churn(%)',fontdict=font2)
plt.legend(loc='upper right')

ax2=plt.subplot(1,3,2)
churn_citizen=df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack()*100
churn_citizen.plot(kind='bar',ax=ax2)
plt.title('Citizen Type VS Churn',fontdict=font1)
plt.xlabel('SeniorCitizen',fontdict=font2)
plt.ylabel('Churn(%)',fontdict=font2)

ax3=plt.subplot(1,3,3 )
churn_depend=df.groupby('Dependents')['Churn'].value_counts(normalize=True).unstack()*100
churn_depend.plot(kind='bar',ax=ax3)
plt.title('Family Dependency VS Churn',fontdict=font1)
plt.xlabel('Dependency',fontdict=font2)
plt.ylabel('Churn(%)',fontdict=font2)
plt.legend().remove()
plt.show()


#PLOT-2:
df['Churn']=df['Churn'].map({'Yes':1,'No':0})
tenure_churn=df.groupby('tenure')['Churn'].mean().reset_index()
fig,ax1 = plt.subplots(figsize=(12, 6))
ax1.hist(df['tenure'], bins=30,color= 'gray')
ax2 = ax1.twinx()
ax2.plot(tenure_churn['tenure'], tenure_churn['Churn'],color='green',marker='o')
plt.title('Tenure of Employee VS Churn',fontdict=font4)
ax1.set_xlabel('Tenure',fontdict=font3)
ax1.set_ylabel('Employes',fontdict=font3)
ax2.set_ylabel('Churn Rate',fontdict=font3)
plt.show()


#PLOT-3:
ax1=plt.subplot(2,2,1)
phone=df['PhoneService'].value_counts()
phone.plot(kind='pie',ax=ax1,autopct='%1.1f%%')
plt.title("Phone Service",loc='center',fontdict=font3)
plt.ylabel(' ')

ax2=plt.subplot(2,2,2)
phone=df['MultipleLines'].value_counts()
phone.plot(kind='pie',ax=ax2,autopct='%1.1f%%')
plt.title("Multiple Lines",loc='center',fontdict=font3)
plt.ylabel(' ')

ax3=plt.subplot(2,2,3)
churn_depend=df.groupby('InternetService')['Churn'].value_counts().unstack()
churn_depend.plot(kind='bar',ax=ax3)
plt.title("Internet Service",loc='center',fontdict=font4)
plt.xlabel('Service Type',fontdict=font2)
plt.ylabel('Users(Emplyes)',fontdict=font2)

ax4=plt.subplot(2,2,4)
phone=df['InternetService'].value_counts()
phone.plot(kind='pie',ax=ax4,autopct='%1.2f%%')
plt.title("Internet Service",loc='center',fontdict=font4)
plt.ylabel(' ')
plt.show()


#PLOT-4:
ax1=plt.subplot(2,3,1)
phone=df['InternetService'].value_counts()
phone.plot(kind='pie',ax=ax1,autopct='%1.2f%%')
plt.title("Internet Service",loc='center',fontdict=font4)
plt.ylabel(' ')

ax2=plt.subplot(2,3,2)
phone=df['OnlineSecurity'].value_counts()
phone.plot(kind='pie',ax=ax2,autopct='%1.2f%%')
plt.title("Security Service",loc='center',fontdict=font4)
plt.ylabel(' ')

ax3=plt.subplot(2,3,3)
phone=df['OnlineBackup'].value_counts()
phone.plot(kind='pie',ax=ax3,autopct='%1.2f%%')
plt.title("Backup Service",loc='center',fontdict=font4)
plt.ylabel(' ')

ax4=plt.subplot(2,3,4)
phone=df['DeviceProtection'].value_counts()
phone.plot(kind='pie',ax=ax4,autopct='%1.2f%%')
plt.title("Divice protection Service",loc='center',fontdict=font4)
plt.ylabel(' ')

ax5=plt.subplot(2,3,6)
col=df[['OnlineSecurity', 'OnlineBackup', 'DeviceProtection']]
new_data=col.melt(var_name='Services',value_name='Value')
sb.countplot(data=new_data,x='Services',hue='Value',ax=ax5)
plt.show()


#PLOT-5:
ax1=plt.subplot(1,2,1)
charges_churn=df.groupby('MonthlyCharges')['Churn'].mean().reset_index()
sb.kdeplot(data=df,x='MonthlyCharges',hue='Churn',fill=False,ax=ax1)
plt.title("Monthly charges",fontdict=font4)

ax2=plt.subplot(1,2,2)
charges_churn=df.groupby('MonthlyCharges')['Churn'].mean().reset_index
sb.kdeplot(data=df,x='TotalCharges',hue='Churn',fill=False,ax=ax2)
plt.title("Total charges",fontdict=font4)
plt.show()


#PLOT-6:
pivot_table = df.pivot_table(index='StreamingTV', columns='StreamingMovies', values='Churn', aggfunc='mean')
plt.title("Services provided vs Churn",fontdict=font4)
plt.xlabel("Streaming Movies",fontdict=font2)
plt.ylabel("Streaming TV",fontdict=font2)
sb.heatmap(pivot_table)
plt.show()