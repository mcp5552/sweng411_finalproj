''' ETLServer.py
# SWENG 411 FA 2023
# Max Piazza 
# Quincy Nguyen 
# 
# This file contains the definition of the ETLServer class 
# And the VerifyData, Logger, and Transform classes 
'''

from ETLSystem import DataHandler
from ETLSystem import Feature
import time
import numpy as np
import pandas as pd
import datetime

''' main() 
# Creates an ETL Server class instance and runs the
# serve() method from that class 
'''
def main():
    ETL_Server = ETLServer() # Create an instance of the ETLServer class

    # While loop for constantly performing the serve() method
    while True:
        try: # scan for input data and serve it if found
            ETL_Server.serve() # attempt to find new data and extract, transform, and load it
        except: # if no data is found
            print("Waiting for data...")
        time.sleep(1.5) # wait 1.5 seconds before trying again 
    

''' class ETLServer
# This class contains the serve() method that is used to serve data ETL requests.
'''
class ETLServer:
    def __init__(self):
        self.dh = DataHandler() # Instantiate the dataHandler to be used by this class object

    ''' serve()
    # This method gets input data, instantiates a sanitizer, calls the sanitize() method
    # on the data to get output data, then loads the output data to S3 in parquet format 
    '''
    def serve(self):
        # Read in a .csv file as a pandas dataframe
        df = self.dh.getCsv() 
        print("Raw Data: " + df.to_string()) 

        # Verify csv data has been retrieved successfully (this was not implemented)
        # VerifyData.verifyInData()

        #sanitize the data 
        sanitizer = Sanitize()
        out_df = sanitizer.sanitize(df)

        print("Sanitized dataframe:")
        print(out_df.to_string())

        # load the data      
        print("Loading Data...")  
        self.dh.load(out_df) 
        print("Data Loaded to Warehouse Sucessfully!")

        # Verify that parquet data has been sent successfully (this was not implemented)
        #VerifyData.verifyOutData() 

''' class VerifyData
# This class verifies that the data in s3 matches the dataframe passed into its methods 
'''
class VerifyData(Feature):
    def verifyInData(df):
        return True
    def verifyOutData(df):
        return True

''' class Logger
# This class writes input strings from to a log file 
'''
class Logger(Feature):
    def writeToLog(input):
        pass 

''' class Sanitize
# This class contains all the methods for handling
# the sanitization of data 
'''
class Sanitize(Feature):
    ''' sanitize()
    # This method determines the appropriate sanitize method to call
    # Based on the entry type and calls the appropriate sanitize sub-method
    '''
    def sanitize(self, df):
        # read the entry type and call the appropriate sanitization sub-method
        if  df.iloc[0]['Entry_Type'] == 1:
            print("Sanitizing data of type 1...")
            df2 = self.sanitize1(df)
        if df.iloc[0]['Entry_Type'] == 2:
            print("Sanitizing data of type 2...")
            df2 = self.sanitize2(df)
        if df.iloc[0]['Entry_Type'] == 3:
            print("Sanitizing data of type 3...")
            df2 = self.sanitize3(df)
        return df2 

    ''' sanitize1()
    # This is the sanitizer for entry type 1
    '''
    def sanitize1(self, df):
        User_ID	= df.iloc[0]['User_ID']
        Org_ID = df.iloc[0]['Org_ID']
        Date = df.iloc[0]['Date']
        Timestamp = df.iloc[0]['Timestamp']

        # Update fields by calling sanitizer methods 
        User_ID = self.sanitize_user_id(User_ID)
        Org_ID = self.sanitize_org_id(Org_ID)
        Date = self.sanitize_date(Date)
        Timestamp = self.sanitize_timestamp(Timestamp)

        Entry_Type = 1
        #Region = df.iloc[0]['Region'] #This field got omitted 
        Category = df.iloc[0]['Category']
        Transaction_ID = df.iloc[0]['Transaction_ID']
        Transaction_Code = df.iloc[0]['Transaction_Code']
        Cart_ID	= df.iloc[0]['Cart_ID']
        Billing_Street_1 = df.iloc[0]['Billing_Street_1']
        Billing_Street_2 = df.iloc[0]['Billing_Street_2']
        Billing_City = df.iloc[0]['Billing_City']
        Billing_State = df.iloc[0]['Billing_State']
        Billing_ZIP	= df.iloc[0]['Billing_ZIP']
        Billing_Country	 = df.iloc[0]['Billing_Country']
        Credit_Card_Number = df.iloc[0]['Credit_Card_Number']
        CVV_Number = df.iloc[0]['CVV_Number']
        Card_Type = df.iloc[0]['Card_Type']
        Transaction_Amount = df.iloc[0]['Transaction_Amount']

        # define list of data values 
        data_values = np.array([[User_ID, Org_ID, Date, Timestamp, Entry_Type, 
                                Category, Transaction_ID, Transaction_Code, Cart_ID, Billing_Street_1, 
                                Billing_Street_2, Billing_City, Billing_State, Billing_ZIP, Billing_Country, 
                                Credit_Card_Number, CVV_Number, Card_Type, Transaction_Amount]])

        # define column names
        column_names = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", "Category", 
                        "Transaction_ID" , "Transaction_Code", "Cart_ID", "Billing_Street_1", "Billing_Street_2", 
                        "Billing_City", "Billing_State", "Billing_ZIP", "Billing_Country", "Credit_Card_Number", 
                        "CVV_Number", "Card_Type", "Transaction_Amount"]
        
        # create pandas DataFrame out of specified data and column values 
        df2 = pd.DataFrame(data = data_values, columns = column_names) 
        return df2 
    
    ''' sanitize2()
    # This is the sanitizer for entry type 2
    '''
    def sanitize2(self, df):
        User_ID	= df.iloc[0]['User_ID']
        Org_ID = df.iloc[0]['Org_ID']
        Date = df.iloc[0]['Date']
        Timestamp = df.iloc[0]['Timestamp']
        Entry_Type = 2

        # Update fields by calling sanitizer methods 
        User_ID = self.sanitize_user_id(User_ID)
        Org_ID = self.sanitize_org_id(Org_ID)
        Date = self.sanitize_date(Date)
        Timestamp = self.sanitize_timestamp(Timestamp)
        print("Sanitization Completed Sucessfully.")

        Resource_ID = df.iloc[0]['Resource_ID'] 
        # define list of data values 
        data_values = np.array([[User_ID, Org_ID, Date, Timestamp, Entry_Type, Resource_ID]])

        # define column names
        column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", "Resource_ID"]

        # create pandas DataFrame out of specified data and column values 
        df2 = pd.DataFrame(data = data_values, columns = column_values) 
        return df2 

    ''' sanitize3()
    # This is the sanitizer for entry type 3
    '''
    def sanitize3(self, df):
        User_ID	= df.iloc[0]['User_ID']
        Org_ID = df.iloc[0]['Org_ID']
        Date = df.iloc[0]['Date']
        Timestamp = df.iloc[0]['Timestamp']

        # Update fields by calling sanitizer methods 
        User_ID = self.sanitize_user_id(User_ID)
        Org_ID = self.sanitize_org_id(Org_ID)
        Date = self.sanitize_date(Date)
        Time = self.sanitize_timestamp(Timestamp)
        print("Sanitization Completed Sucessfully.")

        Entry_Type = 2
        Resource_ID = df.iloc[0]['Resource_ID']
        Error_Code = df.iloc[0]['Error_Code']

        # define list of data values 
        data_values = np.array([[User_ID, Org_ID, Date, Timestamp, Entry_Type, Resource_ID, Error_Code]])

        # define column names
        column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", "Resource_ID", "Error_Code"]

        # create pandas DataFrame out of specified data and column values 
        df2 = pd.DataFrame(data = data_values, columns = column_values) 
        return df2

    ''' sanitize_user_id()
    # This is the sanitizer for invalid user IDs 
    # Pads invalid user IDs with a 0 on the right side
    '''
    def sanitize_user_id(self, User_ID):
        if len(str(User_ID)) < 9:
            User_ID = str(User_ID) + "0"
            User_ID = int(User_ID)
            return User_ID
        else : 
            return User_ID
        

    ''' sanitize_org_id()
    # This is the sanitizer for invalid organization IDs
    '''
    def sanitize_org_id(self, Org_ID):
        if len(Org_ID) < 12:
            Org_ID = "0000" + Org_ID
            return Org_ID
        else : 
            return Org_ID

    ''' sanitize_date()
    # This is the sanitizer for invalid dates
    '''
    def sanitize_date(self, Date): 
        current_date = datetime.datetime.now()
        month = current_date.strftime("%m")
        data_date_part1 = Date[0] + Date[1]
        if data_date_part1 != month: 
            # This works by re-generating the date in the correct format 
            # For now this only works when sanitizing on the same day that the data was generated 
            output = current_date.strftime("%m") + "/" + current_date.strftime("%d") + "/" + current_date.strftime("%Y")
            return output
        else:
            return Date

    ''' sanitize_timestamp()
    # This is the sanitizer for timestamps
    '''
    def sanitize_timestamp(self, Timestamp):
        return Timestamp

    ''' sanitize_useless_column()
    # This is the sanitizer for the useless column
    '''
    def sanitize_useless_column(self): 
        pass

    ''' sanitize_category()
    # This is the sanitizer for invalid categories
    '''
    def sanitize_category(self) : 
        pass

    ''' sanitize_transaction_id()
    # This is the sanitizer for invalid transaction IDs
    '''
    def sanitize_transaction_id(self): 
        pass

    ''' sanitize_transaction_code() 
    # This is the sanitizer for invalid transaction codes
    '''
    def sanitize_transaction_code(self): 
        pass

    ''' sanitize_cart_id()
    # This is the sanitizer for invalid cart IDs
    '''
    def sanitize_cart_id(self) : 
        pass

    ''' sanitize_billing_street_1()
    # This is the sanitizer for invalid billing street 1 fields
    '''
    def sanitize_billing_street_1(self) : 
        pass

    ''' sanitize_billing_street_2()
    # This is the sanitizer for invalid billing street 2 fields
    '''
    def sanitize_billing_street_2(self) : 
        pass

    ''' sanitize_billing_state_2()
    # This is the sanitizer for invalid billing states
    '''
    def sanitize_billing_state(self) : 
        pass

    ''' sanitize_billing_zip()
    # This is the sanitizer for invalid billing ZIPs
    '''
    def sanitize_billing_zip(self) : 
        pass

    ''' sanitize_credit_card_number()
    # This is the sanitizer for invalid credit card numbers
    '''
    def sanitize_credit_card_number(self) : 
        pass

    ''' sanitize_cvv_number()
    # This is the sanitizer for invalid CVV numbers
    '''
    def sanitize_cvv_number(self) : 
        pass

    ''' sanitize_cvv_type()
    # This is the sanitizer for invalid CVV types
    '''
    def sanitize_card_type(self) : 
        pass

    ''' sanitize_transaction_amount()
    # This is the sanitizer for invalid transaction amounts
    '''
    def sanitize_transaction_amount(self) : 
        pass

    ''' sanitize_resource_ID()
    # This is the sanitizer for invalid resource IDs
    '''
    def sanitize_resource_ID(self) : 
        pass

    ''' sanitize_error_code()
    # This is the sanitizer for invalid error codes 
    '''
    def sanitize_error_code(self) : 
        pass
 
if __name__== "__main__":
    main()