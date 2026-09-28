import pandas as pd
import seaborn as sn 
data  = pd.read_csv(r'PandaProjects\PandaProject1\winemag-data_first150k.csv')
country = data.loc[data['country'] == 'Italy']
variety = data.variety
sn.barplot(x=country,y=variety)
print(country.head())