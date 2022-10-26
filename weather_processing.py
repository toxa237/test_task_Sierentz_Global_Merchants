# TODO Import the necessary libraries
import re
import numpy as np
import pandas as pd


# TODO Import the dataset 

path = r'data/weather_dataset.csv'
df = pd.read_csv(path, sep=', ', engine='python')

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index

df.rename(columns={'Yr': 'year', 'Mo': 'month', 'Dy': 'day'}, inplace=True)
df['year'] = 1900 + df['year']
df['date'] = pd.to_datetime(df[df.columns[:3]])
df.index = df['date']
df.drop(columns=df.columns[:3], inplace=True)
df.drop(columns='date', inplace=True)

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them


def check(x):
    try:
        return float(re.sub(',', '.', x))
    except:
        return np.nan


df = df.applymap(lambda x: check(x), na_action='ignore')

# TODO Write a function in order to fix date (this relate only to the year info) and apply it

# Я зробив це раніше)))


# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]

# це теж)))

# TODO Compute how many values are missing for each location over the entire record

print(df.isna().sum(), '\n')

# TODO Compute how many non-missing values there are in total

print('кількість не пропущених значень',
      np.unique(df.isna().values.flatten(), return_counts=True)[1][0])

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times

c = df.values.flatten()[~np.isnan(df.values.flatten())]
print(f'середнє значення = {np.mean(c)}',
      f'там в даних за 76-5-31, реально, є число 9999999999999999, якщо обчислити без нього то вийде:'
      f' {np.mean(c[c < 1e10])}', '\n',
      sep='\n')


# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations
#  of the windspeeds at each location over all the days

loc_stats = pd.DataFrame(df.max(axis=0), columns=['max'])
loc_stats['min'] = df.min(axis=0)
loc_stats['mean'] = df.mean(axis=0)
loc_stats['std'] = df.std(axis=0)
loc_stats['var'] = df.var(axis=0)
print(loc_stats)

# TODO Find the average windspeed in January for each location

print('\nсередня шидкість вітру в січні\n', df.loc[df.index.month == 1].mean(), sep='')

# TODO Downsample the record to a yearly frequency for each location

print('\n', df.resample('Y').mean())

# TODO Downsample the record to a monthly frequency for each location

print('\n', df.resample('M').mean())

# TODO Downsample the record to a weekly frequency for each location

print('\n', df.resample('W').mean())

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all
#  locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks

print('\n')
df2 = df.resample('W').mean()
df2 = df2.loc[df2.index.year > 1961].iloc[:21]
loc_stats2 = pd.DataFrame(df2.max(axis=0), columns=['max'])
loc_stats2['min'] = df2.min(axis=0)
loc_stats2['mean'] = df2.mean(axis=0)
loc_stats2['std'] = df2.std(axis=0)
loc_stats2['var'] = df2.var(axis=0)
print(loc_stats2)
