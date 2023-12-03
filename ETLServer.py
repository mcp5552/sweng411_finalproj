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

'''main() 
# Creates an ETL Server class instance and runs the
# serve() method from that class 
'''
def main():
    #create an instance of the ETL server class
    ETL_server = ETLServer()

    # constantly perform the serve() method
    while True:
        ETL_server.serve() # attempt to find new data and extract, transform, and load it
        time.sleep(5) # wait 5 seconds before trying again 

''' class ETLServer
# This class 
'''
class ETLServer:
    def __init__(self):
        # Instantiate the dataHandler to be used by this class object
        self.dh = DataHandler()

    ''' serve()
    # This method 
    '''
    def serve(self):
        #read in a csv file as a pandas dataframe
        df = self.dh.getCsv() 
        print(df.to_string()) 

        #verify CSV data has been retrieved successfully 
        #VerifyData.verifyInData()

        #sanitize the data 
        sanitizer = Sanitize()
        df = sanitizer.sanitize(df)

        #load the data        
        #self.dh.load(df) 

        #verify that parquet data has been sent successfully 
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
    '''sanitize()
    # This method determines the appropriate sanitize method to call
    # Based on the entry type and calls the appropriate sanitize sub-method
    '''
    def sanitize(self, df):
        # read the entry type and call the appropriate sanitization sub-method
        if  df.iloc[0]['Entry_Type'] == 1:
            print("Sanitizing data of type 1...")
            self.sanitize1(df)
        if df.iloc[0]['Entry_Type'] == 2:
            print("Sanitizing data of type 2...")
            self.sanitize2(df)
        if df.iloc[0]['Entry_Type'] == 3:
            print("Sanitizing data of type 3...")
            self.sanitize3(df)

    '''sanitize1()
    # This is the sanitizer for entry type 1
    '''
    def sanitize1(self, df):
        print("Sanitization Completed Sucessfully.")
    
    '''sanitize2()
    # This is the sanitizer for entry type 2
    '''
    def sanitize2(self, df):
        print("Sanitization Completed Sucessfully.")

    '''sanitize2()
    # This is the sanitizer for entry type 3
    '''
    def sanitize3(self, df):
        print("Sanitization Completed Sucessfully.")

    '''sanitize_user_id()
    # This is the sanitizer for invalid user IDs 
    '''
    def sanitize_user_id():
        pass

    '''sanitize_org_id()
    # This is the sanitizer for invalid organization IDs
    '''
    def sanitize_org_id():
        pass

    '''sanitize_date()
    # This is the sanitizer for invalid dates
    '''
    def sanitize_date(): 
        pass

    '''sanitize_timestamp()
    # This is the sanitizer for timestamps
    '''
    def sanitize_timestamp():
        pass

    '''sanitize_useless_column()
    # This is the sanitizer for the useless column
    '''
    def sanitize_useless_column(): 
        pass

    '''sanitize_category()
    # This is the sanitizer for invalid categories
    '''
    def sanitize_category() : 
        pass

    '''sanitize_transaction_id()
    # This is the sanitizer for invalid transaction IDs
    '''
    def sanitize_transaction_id(): 
        pass

    '''sanitize_transaction_code() 
    # This is the sanitizer for invalid transaction codes
    '''
    def sanitize_transaction_code(): 
        pass

    '''sanitize_cart_id()
    # This is the sanitizer for invalid cart IDs
    '''
    def sanitize_cart_id() : 
        pass

    '''sanitize_billing_street_1()
    # This is the sanitizer for invalid billing street 1 fields
    '''
    def sanitize_billing_street_1() : 
        pass

    '''sanitize_billing_street_2()
    # This is the sanitizer for invalid billing street 2 fields
    '''
    def sanitize_billing_street_2() : 
        pass

    '''sanitize_billing_state_2()
    # This is the sanitizer for invalid billing states
    '''
    def sanitize_billing_state() : 
        pass

    '''sanitize_billing_zip()
    # This is the sanitizer for invalid billing ZIPs
    '''
    def sanitize_billing_zip() : 
        pass

    '''sanitize_credit_card_number()
    # This is the sanitizer for invalid credit card numbers
    '''
    def sanitize_credit_card_number() : 
        pass

    '''sanitize_cvv_number()
    # This is the sanitizer for invalid CVV numbers
    '''
    def sanitize_cvv_number() : 
        pass

    '''sanitize_cvv_type()
    # This is the sanitizer for invalid CVV types
    '''
    def sanitize_card_type() : 
        pass

    '''sanitize_transaction_amount()
    # This is the sanitizer for invalid transaction amounts
    '''
    def sanitize_transaction_amount() : 
        pass

    '''sanitize_resource_ID()
    # This is the sanitizer for invalid resource IDs
    '''
    def sanitize_resource_ID() : 
        pass

    '''sanitize_error_code()
    # This is the sanitizer for invalid error codes 
    '''
    def sanitize_error_code( ) : 
        pass
 
if __name__== "__main__":
    main()