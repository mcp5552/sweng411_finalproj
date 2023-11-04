#!/usr/bin/env python3

class DataHandler: 
    import awswrangler as wr
    import pandas as pd
    import boto3
    import warnings
    warnings.filterwarnings('ignore')
    import configparser


    #reading the credentials securely
    credents = configparser.ConfigParser()

    #user read_file method
    credents.read_file(open('credentials.config'))

    #Reading in the credentials into Python Variables
    aws_key = credents["AWS"]["KEY"]
    aws_secret = credents["AWS"]["SECRET"]
    region = credents["AWS"]["REGION"]

    #creating your session
    your_session = boto3.Session(aws_acces_key_id=aws_key,aws_secret_access_key=aws_secret,region_name=region)

    #define raw data path
    raw_s3_bucket='sweng411'
    raw_path_dir = 'csv/'
    raw_path = f"s3://{raw_s3_bucket}/{raw_path_dir}"

    def getCSV():
        raw_df = wr.ls3.read_csv(path=raw_path, path_suffix=['.csv.'],dataset=True)
        return raw_df

    raw_df = getCSV() 

    raw_df.head()