
from dataclasses import dataclass
import pandas as pd
import numpy as np


@dataclass
class Dataset:
  name: str
  df: pd.DataFrame
  
  def get_name(self):
    """
    Return filename of loaded dataset
    """
    return None

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    return None

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    return None

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    return None

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    return None

  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return None

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    return None

  def get_head(self, n=5):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return None

  def get_tail(self, n=5):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return None

  def get_sample(self, n=5):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return None

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
    """
    # numerics = [i for i in self.columns if (self.dtypes[i] == np.float_ | self.dtypes[i] == np.int_)]
    # return numerics
    return none

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    # texts = [i for i in self.columns if self.dtypes[i] == np.str_]
    # return texts
    return none

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    dates = [i for i in self.columns if self.dtypes[i] == np.datetime64]
    return dates
