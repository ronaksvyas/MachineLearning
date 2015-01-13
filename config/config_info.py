#all the constants and hard coded information is defined here
#imports
import os

config_data = {}
cwd = os.getcwd()
config_data['DATASETS_PATH'] = cwd+"/datasets"
config_data['CLASSES_PATH'] = cwd+"/classes"
config_data['CONFIG_PATH'] = cwd+"/config"
config_data['FUNCTIONS_PATH'] = cwd+"functions"
