import os 
import sys 

import numpy as np 
import dill 
import yaml 
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging


# We have to read
# input => file path 
# output => read the data inside the file and return it
# If file path is invalid or nothing inside file then raise exception
def read_yaml(file_path:str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    

# We have to write
# input => file path, content, replace(either yes or no default is no)
# output => write the content inside the file
def write_yaml_file(file_path:str, content:object, replace:bool=False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
            
    except Exception as e:
        raise USvisaException(e, sys) from e
    

# input => file path
# output => read the data inside the file and return it    
def load_object(file_path:str) -> object:
    logging.info("Enter the load_object method of utils")
    try:
        with open(file_path, 'rb') as file:
            obj = dill.load(file)
            logging.info("Exited the load_object method of utils")
        return obj
    except Exception as e:
        raise USvisaException(e, sys) from e
    
# input => file path, object and create file path 
# output => write the object inside the file
def save_numpy_array_data(file_path:str, data:np.array):
    """
    Save numpy array data to file 
    file_path: str location of file to save 
    array: np.array data to save"""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            np.save(file, data)
            
    except Exception as e:
        raise USvisaException(e, sys) from e
    
# input = file path
# output = read the data inside the file and return it
def load_numpy_array_data(file_path:str) -> np.array:
    """
    Load numpy array data from file 
    file_path: str location of file to load 
    return: np.array data from file"""
    try:
        with open(file_path, 'rb') as file:
            return np.load(file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    

# input => file path, data frame if file not exist create it and write the data frame inside it
# output => write the data frame inside the file
def save_object(file_path:str, obj:object):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    
def drop_columns(data:DataFrame, columns:list) -> DataFrame:
    """
    Drop columns from data frame
    data: DataFrame data frame to drop columns from
    columns: list columns to drop from data frame
    return: DataFrame data frame with columns dropped"""
    logging.info("Enter the drop_columns method of utils")
    try:
        data = data.drop(columns=columns)
        logging.info("Exited the drop_columns method of utils")
        return data 
    except Exception as e:
        raise USvisaException(e, sys) from e