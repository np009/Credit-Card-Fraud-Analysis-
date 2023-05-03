# Importing libraries and 
# Setting options for plots.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Reading the data using pandas
data = pd.read_csv("creditcard.csv")
data.head()
#printing basic info of the dataset
print("Shape: ",data.shape)
print("-+-"*15)
print("Dataset info: ",data.info())
 # describe shows basic stats of data
data.describe()
# identifying the count of each class labels
valuecounts = data['Class'].value_counts()
percentage = round(valuecounts*100/valuecounts.sum(),1)
df = pd.DataFrame(data = {'Value_counts':valuecounts,'Percent':percentage})
print(df)
# plotting the percentage of each class label using pie chart
plt.pie(data['Class'].value_counts(),labels=['Legit','Fraud'],
        autopct='%1.1f%%', startangle=50)
plt.legend()
plt.show()
# Now let us see how all the columns are distributed
data.hist(figsize = (15,15))
plt.show()
# separating the dataset based on class labels and assigning them to different vaiables.
legit = data[data.Class == 0]
fraud = data[data.Class == 1]
# Plotting to see how time column is distributed accross two class labels
plt.figure(figsize = (15,8))
plt.suptitle("Distribution of time across all the transactions",
             size = '17',weight = 'bold')
plt.subplot(1,2,1)
# for legit transactions
sns.histplot(legit.Time,kde = True)
plt.title('Legit')

plt.subplot(1,2,2)
# for fraudulent transactions
sns.histplot(fraud.Time,kde = True)
plt.title('Fraud')
plt.show()
# plotting box plot to find if there is any difference across how the transactions
# took place based on Time.
print(data.groupby('Class')['Time'].describe())
sns.boxplot(y = data.Time,x = data.Class)
plt.show()
# plotting box plot to find if there is any difference across how the transactions
# took place based on Amount. 
print(data.groupby('Class')['Amount'].describe())
print('\n')
sns.boxplot(y = data.Amount,x = data.Class)
plt.show()
# function to dectect the range on which above or below outliers may exist
# it is done based on the metrics of boxplot
def outliers(arr):
    per25,per75 = np.percentile(arr,[25,75])
    mean = np.mean(arr)
    iqr = per75 - per25
    upper_fence = mean + 1.5*iqr
    lower_fence = mean - 1.5*iqr
    outliers_count = ((arr > upper_fence) | (arr < lower_fence)).sum()
    return upper_fence,lower_fence,outliers_count
# to find the ouliers in both Genuine & fraudulent transactions
print("Number of outliers in Legit amount transactions: ",outliers(legit.Amount)[2])
print("Number of outliers in fraud amount transactions: ",outliers(fraud.Amount)[2])
# using outlier func to get the range for oulier detection
genamnt_outliers = outliers(legit.Amount)
frdamnt_outliers = outliers(fraud.Amount)
l_out = legit[legit.Amount <= genamnt_outliers[0]]# removing outliers
f_out = fraud[fraud.Amount <= frdamnt_outliers[0]]# removing outliers
print("legit:\n upper fence:{} lower fence:{} ouliers count:{}"
     .format(genamnt_outliers[0],genamnt_outliers[1],genamnt_outliers[2]))
print("fradulent:\n upper fence:{} lower fence:{} ouliers count:{}"
     .format(frdamnt_outliers[0],frdamnt_outliers[1],frdamnt_outliers[2]))

# concatenating the dataframe of both genuine & fradulent datasets after outliers removal
df_aft_outliers = pd.concat([l_out,f_out])
df_aft_outliers.shape
# Scatter plot for time vs amount
plt.figure(figsize=(15,7)) # adding fig size
plt.suptitle("Scatter plot of Time vs Amount before and after removing outliers",
             size = 15,weight = 'bold')
plt.subplot(1,2,1)
sns.scatterplot(data,y = data.Amount,x = data.Time,hue = data.Class)# including outliers
plt.title('Before removing outliers')

plt.subplot(1,2,2)
sns.scatterplot(df_aft_outliers,y = df_aft_outliers.Amount,x = df_aft_outliers.Time,
               hue = df_aft_outliers.Class)
# removing outliers
plt.title("After removing outliers")
plt.show()

# Box plot of amount column
plt.figure(figsize = (15,7))
plt.suptitle("Box plot of transactional Amount before and after removing outliers ",
             size = 15,weight = 'bold')
plt.subplot(1,2,1)
sns.boxplot(y = data.Amount,x = data.Class)# including outliers
plt.title('Before removing ouliers')

plt.subplot(1,2,2)
sns.boxplot(y = df_aft_outliers.Amount,x = df_aft_outliers.Class)# after removing outliers
plt.title('After removing ouliers')
plt.show()

#Correlation
data.corr()['Class']
plt.figure(figsize=(25,25))
sns.heatmap(round(data.corr(),3),annot = True,cmap = 'coolwarm',
            linewidths = 0.5 ,linecolor='black')
plt.show()