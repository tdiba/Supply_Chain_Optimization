#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel(r"C:\Users\USER\Documents\Chat GPT Projects\RAW DATA\Supply Chain Analysis\Supply_Chain_Dataset.xlsx")


# In[3]:


df.head()


# In[4]:


# Displaying the basic statistics of the dataset
df.describe()


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


# Setting the aesthetic style of the plots
sns.set_style("whitegrid")


# In[7]:


# Demand and Supply Analysis
# Comparing Demand, Order Quantity, and Safety Stock
plt.figure(figsize=(15, 5))


# In[8]:


# Demand
sns.kdeplot(df['Demand (units)'], color="blue", label="Demand", fill=True)


# In[9]:


# Order Quantity
sns.kdeplot(df['Order Quantity (units)'], color="green", label="Order Quantity", fill=True)


# In[10]:


# Safety Stock
sns.kdeplot(df['Safety Stock (units)'], color="red", label="Safety Stock", fill=True)


# In[12]:


# Demand
sns.kdeplot(df['Demand (units)'], color="blue", label="Demand", fill=True)

# Order Quantity
sns.kdeplot(df['Order Quantity (units)'], color="green", label="Order Quantity", fill=True)

# Safety Stock
sns.kdeplot(df['Safety Stock (units)'], color="red", label="Safety Stock", fill=True)

plt.title("Comparison of Demand, Order Quantity, and Safety Stock")
plt.xlabel("Units")
plt.ylabel("Density")
plt.legend()
plt.show()


# In[13]:


# Cost Analysis
# Analyzing Production and Logistics Costs
plt.figure(figsize=(15, 5))

# Production Cost
sns.kdeplot(df['Production Cost (USD)'], color="blue", label="Production Cost", fill=True)

# Logistics Cost
sns.kdeplot(df['Logistics Cost (USD)'], color="orange", label="Logistics Cost", fill=True)

plt.title("Comparison of Production and Logistics Costs")
plt.xlabel("Cost in USD")
plt.ylabel("Density")
plt.legend()
plt.show()


# In[14]:


# Lead Time Analysis
plt.figure(figsize=(10, 6))

# Plotting Lead Time Distribution
sns.histplot(df['Lead Time (days)'], bins=30, kde=True, color="purple")

plt.title("Distribution of Lead Times")
plt.xlabel("Lead Time (days)")
plt.ylabel("Frequency")
plt.show()


# In[15]:


# Identifying potential bottlenecks

# High Lead Time
high_lead_time_threshold = df['Lead Time (days)'].quantile(0.75)
high_lead_time_products = df[df['Lead Time (days)'] > high_lead_time_threshold]


# In[16]:


# High Production Cost
high_production_cost_threshold = df['Production Cost (USD)'].quantile(0.75)
high_production_cost_products = df[df['Production Cost (USD)'] > high_production_cost_threshold]


# In[17]:


# High Logistics Cost
high_logistics_cost_threshold = df['Logistics Cost (USD)'].quantile(0.75)
high_logistics_cost_products = df[df['Logistics Cost (USD)'] > high_logistics_cost_threshold]


# In[19]:


import numpy as np


# In[20]:


# Mismatch between Demand and Order Quantities (either overordering or underordering)
demand_order_mismatch = df[np.abs(df['Demand (units)'] - df['Order Quantity (units)']) > (df['Demand (units)'] * 0.2)]


# In[21]:


# Displaying the count of products identified in each bottleneck category
bottleneck_counts = {
    "High Lead Time Products": high_lead_time_products.shape[0],
    "High Production Cost Products": high_production_cost_products.shape[0],
    "High Logistics Cost Products": high_logistics_cost_products.shape[0],
    "Demand-Order Quantity Mismatch": demand_order_mismatch.shape[0]
}

bottleneck_counts


# In[22]:


# Scatter plot for products with high lead times and high costs
plt.figure(figsize=(12, 6))

# Plotting High Lead Time vs High Production Cost
sns.scatterplot(data=high_lead_time_products, x='Production Cost (USD)', y='Lead Time (days)', color='blue', label='High Lead Time')

# Highlighting products that also have high production costs
high_cost_and_lead_time = high_lead_time_products[high_lead_time_products['Production Cost (USD)'] > high_production_cost_threshold]
sns.scatterplot(data=high_cost_and_lead_time, x='Production Cost (USD)', y='Lead Time (days)', color='red', label='High Lead Time & High Production Cost')

plt.title("Products with High Lead Times and High Production Costs")
plt.xlabel("Production Cost (USD)")
plt.ylabel("Lead Time (days)")
plt.legend()
plt.show()


# In[ ]:




