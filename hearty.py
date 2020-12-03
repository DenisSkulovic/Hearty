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
        data_df = Parser(76, [1,3,4,13,14,15,17,18,33,48,58], generator).return_data_df()
        frames.append(data_df)
    df = pd.concat(frames)
    for col in df.columns:
        df[col] = df[col].astype(int)
    df = df.set_index(1, drop=True).sort_index()
    return df

filenames = ['hungarian.data.csv', 'cleveland.data.csv', 'long-beach-va.data.csv', 'switzerland.data.csv']
df = get_data(filenames)