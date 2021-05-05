import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('fetched_data_v1.csv')
# print(df.columns)
df['Market Name'] = df['Market Name'].astype(object)

major_markets = df['Market Name'].value_counts()
major_markets.sort_values(inplace=True,ascending=False)
print(major_markets.head(10))

# The top 5 Markets in Agra based on the number of times they have been listed are 

# Achnera           280
# Fatehpur Sikri    265
# Agra              260
# Fatehabad         235
# Samsabad          168
# Jagnair           161
# Khairagarh        157
# Jarar             146


df['Price Date'] = pd.to_datetime(df['Price Date'])


# for i in df.groupby('Market Name'):
#     plt.plot(i[1]['Price Date'],i[1]['Max Price (Rs./Quintal)'],'-',label=i[0])

# plt.legend(loc='upper center',
#            bbox_to_anchor=(0.5, -0.2),
#            fancybox=True,
#            shadow=True,
#            ncol=4)
# plt.xlabel('date')
# plt.ylabel('price')
# plt.legend()
# plt.show()

# sns.displot(df, x="Max Price (Rs./Quintal)", hue="Market Name", kind="kde")

# plt.show()


# for i in df['Market Name'].unique():
#     plt.figure(figsize=(30,20))
#     temp = df[df['Market Name']==i]
#     sns.relplot(x="Price Date", y="Max Price (Rs./Quintal)", kind="line", data=temp);
#     file_name = './price_pattern/'+str(i)+'.png'
#     plt.savefig(file_name)
