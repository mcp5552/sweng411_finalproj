''' DataGenerator.py 
# SWENG 411 FA 2023
# Max Piazza 
# Quincy Nguyen 
#
# This file contains the DataGenerator class definition 
# This file has a main method which instantiates a DataGenerator
# and runs the generate() method 
'''

import numpy as np 
import pandas as pd 
import random
from ETLSystem import Feature
from ETLSystem import DataHandler
  
''' main()
# Calls the generate() method one time to generate random data 
# then sends that data to an S3 bucket for processing 
'''
def main():
    #get some data by using the generate() method
    data = DataGenerator.generate()

    # Create a DataHandler instance 
    dh = DataHandler() 

    # call the sendCSV method on the data   
    dh.sendCsv(data) 

''' class DataGenerator
# contains the definition of the generate() method and all the sub-methods
# needed to generate demo data 
'''
class DataGenerator:
    """ generate()
    # The main generation method which randomly generates one of 
    # 3 types of data
    """
    def generate(self, Feature): 
        r = random.randint(1, 3)
        if r == 1:
            data = self.generate1()
        if r == 2:
            data = self.generate2()
        if r == 3:
            data = self.generate3() 
        return data 

    ''' generate1()
    # the generator method for data of type 1
    '''
    def generate1(self):   
        User_ID	= self.generate_user_id()
        Org_ID = self.generate_org_id()
        Date = self.generate_date()	
        Timestamp = self.generate_timestamp()	
        Entry_Type = 1
        Region = self.generate_region()	
        Category = self.generate_category() 
        Transaction_ID = self.generate_transaction_id()
        Transaction_Code = self.generate_transaction_code()
        Cart_ID	= self.generate_card_id()
        Billing_Street_1 = self.generate_billing_street_1()
        Billing_Street_2 = self.generate_billing_street_2()
        Billing_State = self.generate_billing_state()
        Billing_ZIP	= self.generate_billing_zip()
        Billing_Country	 = self.generate_billing_country()
        Credit_Card_Number = self.generate_credit_card_number()
        CVV_Number = self.generate_cvv_number()
        Card_Type = self.generate_card_type()
        Transaction_Amount = self.generate_transaction_amount() 

        #define list of data values 
        data_values = [User_ID, Org_ID, Date, Timestamp, Entry_Type, Region, None, Category, Transaction_ID, Transaction_Code,
                Cart_ID, Billing_Street_1,Billing_Street_2, Billing_State,	Billing_ZIP,	Billing_Country,	Credit_Card_Number,
                        CVV_Number,	Card_Type,	Transaction_Amount]

        #define column names
        column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", "Region", 
                        "<useless_column>", "Category", "Transaction_ID" , "Transaction_Code", 
                        "Cart_ID", "Billing_Street_1", "Billing_Street_2", "Billing_State", "Billing_ZIP",
                        "Billing_Country", "Credit_Card_Number", "CVV_Number", "Card_Type", "Transaction_Amount"]

        #create pandas DataFrame out of specified data and column values 
        df = pd.DataFrame(data = data_values, columns = column_values) 
        return df 

    '''generate2()
    # the generator method for data of type 2
    '''
    def generate2(self): 	
        User_ID	= self.generate_user_id()
        Org_ID = self.generate_org_id()
        Date = self.generate_date()	
        Timestamp = self.generate_timestamp()		
        Entry_Type = 2 
        Region = self.generate_region()	
        Resource_ID = self.generate_resource_ID() 

        #define list of data values 
        data_values = [User_ID, Org_ID, Date, Timestamp, Entry_Type, Region, None, Resource_ID]

        #define column names
        column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", "Region", 
                        "<useless_column>", "Resource_ID"]

        #create pandas DataFrame out of specified data and column values 
        df = pd.DataFrame(data = data_values, columns = column_values) 
        return df 

    '''generate3()
    # the generator method for data of type 3 
    '''
    def generate3(self):  
        User_ID	= self.generate_user_id()
        Org_ID =  self.generate_org_id()
        Date = self.generate_date()	
        Timestamp = self.generate_timestamp()			
        Entry_Type = 3
        Region = self.generate_region()	
        Resource_ID	= self.generate_resource_ID() 
        Error_Code = self.generate_error_code() 

        #define list of data values 
        data_values = [User_ID, Org_ID, Date, Timestamp, Entry_Type, Region, None, Resource_ID, Error_Code]

        #define column names
        column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", "Region", 
                        "<useless_column>", "Resource_ID", "Error_Code"]

        #create pandas DataFrame out of specified data and column values 
        df = pd.DataFrame(data = data_values, columns = column_values) 
        return df 

    '''generate_user_id() 
    '''
    def generate_user_id():
        pass

    '''generate_org_id()
    '''
    def generate_org_id():
        pass

    '''generate_date()
    '''
    def generate_date():
        pass

    '''generate_timestamp()
    '''
    def generate_timestamp():
        pass

    # I think we should delete generate_region and just do US for simplicity
    '''generate_region()
    '''
    def generate_region():
        pass

    '''generate_category()
    '''
    def generate_category():
        pass

    '''generate_transaction_id()
    '''
    def generate_transaction_id():
        pass 

    '''generate_transaction_code()
    '''
    def generate_transaction_code():
        pass 

    '''generate_card_id()
    '''
    def generate_card_id():
        pass 

    '''generate_billing_street_1()
    '''
    def generate_billing_street_1():
        pass 

    '''generate_billing_street_2()
    '''
    def generate_billing_street_2():
        pass 

    '''generate_billing_state()
    '''
    def generate_billing_state():
        pass 

    '''generate_billing_zip()
    '''
    def generate_billing_zip():
        pass 

    '''generate_billing_country()
    '''
    def generate_billing_country(): 
        pass 

    '''generate_credit_card_number()
    '''
    def generate_credit_card_number():
        pass  

    '''generate_cvv_number()
    '''
    def generate_cvv_number(): 
        pass 

    '''generate_card_type()
    '''
    def generate_card_type(): 
        pass 

    '''generate_transaction_amount()
    '''
    def generate_transaction_amount(): 
        pass 

    '''generate_resource_ID()
    '''
    def generate_resource_ID(): 
        pass

    ''' generate_error_code() 
    '''
    def generate_error_code():
        pass 

''' 
# definition of main method for demo / dev purposes 
'''
if __name__ == "__main__":
    main()