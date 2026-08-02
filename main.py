import numpy as np
import pandas as pd
from scipy import stats


complete_dataset = pd.read_csv('data/complete_dataset.csv')

cities_with_most_incidents = complete_dataset[complete_dataset['Anno']==2020][complete_dataset['DATA_TYPE']=='ROADACC']
cities_with_most_incidents.sort_values(by=['OBS_VALUE'], ascending=False)

# fit a simple linear regression manually
slope, intercept, r, p, se = stats.linregress(
    cities_with_most_incidents['Popolazione legale'],
    cities_with_most_incidents['OBS_VALUE']
)

predicted = slope * cities_with_most_incidents['Popolazione legale'] + intercept
residuals = cities_with_most_incidents['OBS_VALUE'] - predicted

# grab the 6 with the largest absolute residual
outliers = cities_with_most_incidents.reindex(
    residuals.abs().sort_values(ascending=False).index
).head(6)

print(outliers)