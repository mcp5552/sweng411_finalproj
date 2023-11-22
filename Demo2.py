#!/usr/bin/env python3

import awswrangler as wr
import pandas as pd
import boto3
import warnings
warnings.filterwarnings('ignore')
import configparser

#reading the credentials securely
credents = configparser.ConfigParser()

#use read_file method
credents.read_file(open('credentials.cfg'))

#Reading in the credentials into Python Variables
aws_key = credents["AWS"]["key"]
aws_secret = credents["AWS"]["secret"]
region = credents["AWS"]["region"]

#creating the session
your_session = boto3.Session(aws_access_key_id=aws_key,aws_secret_access_key=aws_secret,region_name=region)

#define raw data path
raw_s3_bucket = 'sweng411'
csv_path_dir = 'csv/'
csv_path = f"s3://{raw_s3_bucket}/{csv_path_dir}"
parquet_path_dir = 'parquet/'
parquet_path = f"s3://{raw_s3_bucket}/{parquet_path_dir}"


#main method for demo purposes
def main():
    dh = DataHandler()
    raw_df = dh.getCsv()
    print(raw_df.to_string())

    '''
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
    '''

    #try to read/write to parquet s3 bucket (data warehouse)
    dh.load(raw_df)
    warehouse_data = dh.getParquet()
    warehouse_data = warehouse_data.tail(n=1)
    print(warehouse_data.to_string())


class DataHandler:
    #getCsv() reads a csv file in from s3 and returns a dataframe
    @staticmethod
    def getCsv():
        raw_df = wr.s3.read_csv(path = csv_path, path_suffix=['.csv'], dataset = True, boto3_session = your_session)
        return raw_df

    #sendCsv() writes a dataframe as a csv file to the s3 bucket for csv files 
    @staticmethod
    def sendCsv(data_in):
        #testing dataset=True 
        wr.s3.to_csv(df = data_in, path = csv_path, dataset = True, boto3_session = your_session)

    #load() writes a dataframe to the s3 bucket for parquet files 
    @staticmethod
    def load(data_in):
        wr.s3.to_parquet(df = df_in, path = parquet_path, dataset=True, boto3_session = your_session)

    #getParquet() reads a parquet file in the data warehouse and returns it as a CSV
    @staticmethod
    def getParquet():
        raw_df = wr.s3.read_parquet(path = parquet_path, path_suffix=['.parquet'], dataset = True, boto3_session = your_session)

if __name__== "__main__":
    main()