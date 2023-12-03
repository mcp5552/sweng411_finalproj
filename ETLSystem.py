''' ETLSystem.py
# SWENG 411 FA 2023
# Max Piazza 
# Quincy Nguyen 
#
# This file contains the Feature and DataHandler class definitions 
'''

import awswrangler as wr
import pandas as pd
import boto3
import warnings
warnings.filterwarnings('ignore')
import configparser

#main method for demo purposes
def main():
    '''
    dh = DataHandler()
    raw_df = dh.getCsv()
    print(raw_df.to_string())
    # try editing the df by dropping an element
    new_df = raw_df.drop(columns=['<useless_column>'])
    new_df = new_df.head(n=1) #just keep 1 entry
    print("\n New df with no useless column:\n " + new_df.to_string())
    
    # try sending the new dataframe to s3
    dh.sendCsv(new_df) #this appends to the existing csv as of now 

    #try getting the new dataframe FROM s3 (to demo getCsv())
    df2 = dh.getCsv()
    df2 = df2.tail(n=1) #just use the last line of the modified csv 
    print('\nNew csv file:' + df2.to_string()) 


    #try to read/write to parquet s3 bucket (data warehouse)
    #dh.load(raw_df)

    warehouse_data = dh.getParquet()
    warehouse_data = warehouse_data.tail(n=1)
    print('Warehouse data tail n=1 :' + warehouse_data.to_string())
    '''

''' class Feature
# This class provides for future extensibility, anything that is desired to be 
# common amongst all features can be included in this class
'''
class Feature:
    pass 

''' class DataHandler
# This class contains all methods for sending and retrieving data to AWS s3. 
# It also handles the conversion to/from CSV and Parquet file formats. 
'''
class DataHandler(Feature):
    #credents, aws_key, aws_secret, region, boto3_session, parquet_path  = None 
    
    # Class constructor 
    # Initializes a boto3 session and sets up the buckets 
    def __init__(self):
        # Read the aws credentials file securely
        # First instantiate a configParser
        self.credents = configparser.ConfigParser()

        # Use read_file method from the configparser class 
        self.credents.read_file(open('credentials.cfg'))

        # Read the credentials data into Python variables
        self.aws_key = self.credents["AWS"]["key"]
        self.aws_secret = self.credents["AWS"]["secret"]
        self.region = self.credents["AWS"]["region"]

        # Create the boto3 session
        self.boto3_session = boto3.Session(aws_access_key_id=self.aws_key, aws_secret_access_key=self.aws_secret, region_name=self.region)

        # define the paths for the csv and parquet data buckets 
        self.raw_s3_bucket = 'sweng411'
        self.csv_path_dir = 'csv/'
        self.csv_path = f"s3://{self.raw_s3_bucket}/{self.csv_path_dir}"
        self.parquet_path_dir = 'parquet/'
        self.parquet_path = f"s3://{self.raw_s3_bucket}/{self.parquet_path_dir}"
        
    #getCsv() reads a csv file in from s3 and returns a dataframe
    def getCsv(self):
        raw_df = wr.s3.read_csv(path = self.csv_path, path_suffix=['.csv'], dataset = True, boto3_session = self.boto3_session)
        return raw_df

    #sendCsv() writes a dataframe as a csv file to the s3 bucket for csv files 
    def sendCsv(self, df_in):
        #testing dataset=True 
        wr.s3.to_csv(df = df_in, path = self.csv_path, dataset = True, boto3_session = self.boto3_session)

    #load() writes a dataframe to the s3 bucket for parquet files 
    def load(self, df_in):
        wr.s3.to_parquet(df = df_in, path = self.parquet_path, dataset=True, boto3_session = self.boto3_session)

    #getParquet() reads a parquet file in the data warehouse and returns it as a CSV
    def getParquet(self):
        raw_df = wr.s3.read_parquet(path = self.parquet_path, path_suffix=['.parquet'], dataset = True, boto3_session = self.boto3_session)
        return raw_df

if __name__== "__main__":
    main()