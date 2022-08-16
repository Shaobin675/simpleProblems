# Use pandas to read from: https://www.fhfa.gov/DataTools/Downloads/Documents/HPI/HPI_AT_state.csv

# File has header: state,year,quarter,hpi

# - Calculate the mean by state,year and just state
# - Add a column to calculate the running mean for each state

# use: https://trinket.io/python3
import pandas as pd


def solution():
    data = pd.read_csv('https://www.fhfa.gov/DataTools/Downloads/Documents/HPI/HPI_AT_state.csv',
                       names=['state','year','quarter','hpi'])
    #print(data.head())                
    state_year_mean = data.groupby(by=['state', 'year']).mean()['hpi']
    print("Calculate the mean by state,year", state_year_mean.head())
    
    state_mean = data.groupby(by=['state']).mean()[['hpi']]
    print("Calculate the mean by state", state_mean.head())
    
    data['state_mean'] = data['state'].apply(lambda state: state_mean.loc[state])
    print("Add a column to calculate the running mean for each state", data.head())


solution()
