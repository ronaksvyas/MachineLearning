#this file has all the random functions needed on the go

#imports
import os
from config_info import *
global config_data

#function to get the datasets folder path
def get_datasets_path():
	return config_data["DATASETS_PATH"]

#function to insert or update the config data
def update_config_data(key , value):
	config_data[key] = value

#get config data
def get_config_data():
	return config_data
