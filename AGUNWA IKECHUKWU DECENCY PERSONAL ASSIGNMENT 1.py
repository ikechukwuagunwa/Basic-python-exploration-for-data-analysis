#!/usr/bin/env python
# coding: utf-8

#  1. Create a Python dictionary containing the following data for 8 students

# In[224]:


import pandas as pd
import matplotlib.pyplot as plt


# In[140]:


student_data = {'student_id':[1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008],
     'student_name':['john', 'mark', 'joy', 'david', 'kim', 'favour', 'josh', 'mitchelle'],
     'sex':['male', 'male', 'female', 'male', 'female', 'female', 'male', 'female'],
     'math_score':[30, 90, 20, 55, 74, 84, 60, 40],
     'science_score':[65, 80, 40, 75, 85, 70, 35,55],
     'english_score':[80, 30, 25, 70, 95, 45, 85, 70],
     'history_score':[20, 30, 40, 50, 60, 70, 80, 90],
     'geography_score':[90, 80, 70, 60, 50, 40, 30, 20]
     }


# In[141]:


df = pd.DataFrame(student_data)


# In[142]:


student_data = tabulate(student_data, headers="keys", tablefmt="pretty")
print(student_data)


# 2. After creating the DataFrame, conduct the following data checks

# In[143]:


#Check the shape of the DataFrame (number of rows and columns).

shape = df.shape
print("Shape of the DataFrame:", shape)


# In[144]:


#Check for missing values in each column and report the count of missing values. 

missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)


# In[145]:


# Check for duplicates in the dataset and report the count of duplicates. 

duplicate_count = df.duplicated().sum()
print("Count of duplicates:", duplicate_count)


# 3. Calculate and add a new column to the DataFrame for the "Average Score," which is the average of scores in all subjects for each student. 

# In[153]:


# Calculate and print the following statistics for each subject: 

#Mean (average) Score

math_score = df["math_score"].mean()
print("Mean Math Score:", math_score)
science_score = df["science_score"].mean()
print("Mean Science Score:", science_score)
english_score = df["english_score"].mean()
print("Mean English Score:", english_score)
history_score = df["history_score"].mean()
print("Mean History Score:", history_score)
geography_score = df["geography_score"].mean()
print("Mean Geography Score:", geography_score)


# In[151]:


#Maximum Score 

math_score = df["math_score"].max()
print("Maximum Math Score:", math_score)
science_score = df["science_score"].max()
print("Maximum Science Score:", science_score)
english_score = df["english_score"].max()
print("Maximum English Score:", english_score)
history_score = df["history_score"].max()
print("Maximum History Score:", history_score)
geography_score = df["geography_score"].max()
print("Maximum Geography Score:", geography_score)


# In[152]:


#Minimum Score

math_score = df["math_score"].min()
print("Minimum Math Score:", math_score)
science_score = df["science_score"].min()
print("Minimum Science Score:", science_score)
english_score = df["english_score"].min()
print("Minimum English Score:", english_score)
history_score = df["history_score"].min()
print("Minimum History Score:", history_score)
geography_score = df["geography_score"].min()
print("Minimum Geography Score:", geography_score)


# In[162]:


#Calculate and print the overall mean (average) score for all subjects for each gender category (Male and Female).


score_columns = ["math_score", "science_score", "english_score", "history_score", "geography_score"]
gender_mean_scores = df.groupby("sex")[score_columns].mean()
print("Overall Mean Scores by Gender:")
print(gender_mean_scores)


# 4. Data Visualization: 
# - Create visualizations for the following: 

# In[223]:


#A bar chart to visualize the average scores of students for each subject, grouped by gender. 

ax = gender_mean_scores.plot(kind="bar", figsize=(10, 6))
plt.title("Average Scores by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.xticks(rotation=0) 
plt.legend(title="Subjects", bbox_to_anchor=(1, 1))
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', fontsize=10, color='black', xytext=(0, 5), textcoords='offset points')



# In[ ]:




