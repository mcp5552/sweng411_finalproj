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
raw_path_dir = 'csv/'
raw_path = f"s3://{raw_s3_bucket}/{raw_path_dir}"

#list buckets (this works as a demo) 
#your_buckets = wr.s3.list_buckets(boto3_session=your_session)
#print(your_buckets)


raw_df = wr.s3.read_csv(path=raw_path, path_suffix=['.csv'],dataset=True,boto3_session=your_session)
print(raw_df.to_string())