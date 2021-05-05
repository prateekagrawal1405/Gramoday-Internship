import pandas as pd 
from tqdm import tqdm
data = []
month_day_dict = {
    'Jan':31,
    'Feb':29,
    'Mar':31,
    'Apr':30,
    'May':31,
    'Jun':30,
    'Jul':31,
    'Aug':31,
    'Sep':30,
    'Oct':31,
    'Nov':30,
    'Mar':31,
}
for k,v in month_day_dict.items():
    for i in tqdm(range(1,month_day_dict[k]+1)):
        url = 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market=0&DateFrom='+str(i)+'-'+str(k)+'-'+'2020&DateTo='+str(i)+'-'+str(k)+'-'+'2020&Fr_Date='+str(i)+'-'+str(k)+'-'+'2020&To_Date='+str(i)+'-'+str(k)+'-'+'2020&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead=--Select--'
        # print(url)
        try:
            values = pd.read_html(url)
            temp = values[0]
            # print(temp.values)
            # print(temp.head())
            for x in temp.values :
              data.append(x)
            # data.append(temp.values)
            # print(data)
        except:
            print(url)


# Debugging Error
# for i in range(len(data)):
#       if np.shape(data[i])[0]!=10:
#     print(np.shape(data[i]),data[i],i)

# The data for July 12,2020 is not available and hence causing issue. Manually removing it fixes the error.

data.pop(1201)
cols = ['Sl. No','District Name','Market Name','Commodity','Variety','Grade','Min Price (Rs./Quintal)','Max Price (Rs./Quintal)','Modal Price (Rs./Quintal)','Price Date']
df = pd.DataFrame(temp,columns=cols)
df.to_csv('fetched_data_v1.csv',index=False)