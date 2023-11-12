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

class DataHandler:
    #getCsv() reads a csv file in from s3 and returns a dataframe
    @staticmethod
    def getCsv():
        raw_df = wr.s3.read_csv(path = csv_path, path_suffix=['.csv'], dataset = True, boto3_session = your_session)
        return raw_df

    #sendCsv() writes a dataframe as a csv file to the s3 bucket for csv files 
    def sendCsv(data_in):
        wr.s3.to_csv(df = data_in, path = csv_path, boto3_session = your_session)

    #load() writes a dataframe to the s3 bucket for parquet files 
    def load(data_in):
        wr.s3.to_parquet(df = df_in, path = parquet_path, boto3_session = your_session)

if __name__== "__main__":
    main()