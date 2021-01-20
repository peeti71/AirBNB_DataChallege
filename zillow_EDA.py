import pandas as pd

#import dataset
zillow = pd.read_csv('data/Zip_Zhvi_2bedroom.csv')

#filter for only NY state
#fill missing values with 0
#rename RegionName to Zipcode

zillow_NYC = zillow[zillow['City'] == 'New York']
zillow_NYC.reset_index(drop=True, inplace=True)
Z_NYC = zillow_NYC.fillna(0)
Z_NYC.rename(columns={"RegionName":"ZipCode"}, inplace=True)

# transpose data column to row
#date column 7,262
nyc_data = []
for col_nm in range(7,262):
    new = Z_NYC.loc[:,Z_NYC.columns[col_nm]]
    new = pd.DataFrame(new)
    new['Date'] = Z_NYC.columns[col_nm]
    new['ZipCode'] = Z_NYC['ZipCode']
    new['Size']  = Z_NYC['SizeRank']
    new.columns = ['Value', 'Date', 'Zip', 'Rank']
    nyc_data.append(new)
nyc_data = pd.concat(nyc_data)
nyc_data.reset_index(drop=True, inplace=True)

