from abc import ABC, abstractproperty, abstractmethod
import pandas as pd
import numpy as np
import requests
import csv
import datadotworld as dw


class AbstractParser(ABC):
    
    @abstractproperty
    def num_of_features(self):
        pass
    
    @abstractproperty
    def col_indices_to_keep(self):
        pass
    
    @abstractproperty
    def data_generator(self):
        pass
    
    @abstractmethod
    def return_data_df(self):
        pass
  
  
  
class DataGenerator:
    
    def __init__(self, dataset, filename):
        self.dataset = dataset
        self.filename = filename
        self.csv_data = self._get_csv_data()
    

    def _get_csv_data(self):
        with dw.open_remote_file(self.dataset, self.filename, mode='r') as r:
            return csv.DictReader(r)        
        
        
    def next(self):
        # the key is actually the first row, so the first key-value pair needs special care; then simply yielding values witouht touching keys
        key, values = list(next(self.csv_data).items())[0]
        for val in key.split(' '):
            yield val
        for val in values.split(' '):
            yield val
        for entry in self.csv_data:
            for row in entry.values():
                for val in row.split(' '):
                    yield val
                        
  
    
class Parser(AbstractParser):
    
    def __init__(self, num_of_features, col_indices_to_keep, data_generator):
        self._num_of_features = num_of_features
        self._col_indices_to_keep = col_indices_to_keep
        self._data_generator = data_generator
        
    @property
    def num_of_features(self):
        return self._num_of_features
    
    @property
    def col_indices_to_keep(self):
        return self._col_indices_to_keep
    
    @property
    def data_generator(self):
        return self._data_generator
    
    def return_data_df(self):
        rows = []
        row = []
        counter = 0
        while True:
            try:
                for val in self.data_generator.next():
                    counter+=1
                    if counter < self.num_of_features:
                        if counter in self.col_indices_to_keep:
                            row.append(val)
                    else:
                        if counter in self.col_indices_to_keep:
                            row.append(val)
                        rows.append(row)
                        row = []
                        counter=0
            except:
                break
        return pd.DataFrame(rows, columns=self.col_indices_to_keep)
                         
    # def yield_rows(self):
    #     while True:
    #         row = []
    #         result = None
    #         counter = 0
    #         for val in self.data_generator.next():
    #             counter+=1
    #             if counter < self.num_of_features:
    #                 if counter in self.col_indices_to_keep:
    #                     row.append(val)
    #             else:
    #                 if counter in self.col_indices_to_keep:
    #                     row.append(val)
    #                 result = pd.Series(row, index = self.col_indices_to_keep)
    #                 counter = 0
    #                 row = []
    #                 yield result
         
                
def get_data(filenames):
    frames = []
    for filename in filenames:
        generator = DataGenerator('uci/heart-disease', filename)
        data_df = Parser(76, [3,4,13,14,15,17,18,33,58], generator).return_data_df()
        frames.append(data_df)
    df = pd.concat(frames)
    for col in df.columns:
        df[col] = df[col].astype(int)
    df = df.reset_index(drop=True)
    return df


def clean_data(df):
        
    df = df.replace(-9, np.nan)
    
    # fill missing entries in column 13 - smoking yes or no
    mismatched_df = df[(df[13].isnull())&(~df[14].isnull() | ~df[15].isnull())]
    for i in mismatched_df.index:
        if (df.loc[i, 14] > 0) or (df.loc[i, 15] > 0):
            df.loc[i, 13] = 1
        else:
            df.loc[i, 13] = 0
    
    # fill missing diabetes values
    mismatched_df = df[df[17].isnull()]        
    for i in mismatched_df.index:
        df.loc[i, 17] = 0

    # fill resting heart rate with average
    df[33] = df[33].apply(lambda x: df[33].mean() if x!=x else x)

    # fill 13 and 14 
    mismatched_df = df[(~df[13].isnull())&(df[14].isnull() & df[15].isnull())]
    for i in mismatched_df.index:
        if (df.loc[i, 13] == 0):
            df.loc[i, 14] = 0
            df.loc[i, 15] = 0
            
    # drop na
    df = df.dropna()
    
    df.reset_index(drop=True, inplace=True)
    return df



filenames = ['hungarian.data.csv', 'cleveland.data.csv', 'long-beach-va.data.csv', 'switzerland.data.csv']
df = get_data(filenames)
clean_df = clean_data(df)