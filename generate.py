'''
# generate.py 
# SWENG 411 FA 2023
# Max Piazza 
# Quincy Nguyen 
'''

#!/usr/bin/env python3

import numpy as np 
import pandas as pd 
import random
  
def main():
    generate()

if __name__ == "__main__":
    main()


""" generate()
# The main generation method which 
"""
def generate(): 
    r = random.randint(1, 3)
    if r == 1:
        generate1()
    if r == 2:
        generate2()
    if r == 3:
        generate3() 

'''
generate1()
'''

def generate1():   
    User_ID	= generate_user_id()
    Org_ID = generate_org_id()
    Date = generate_date()	
    Timestamp = generate_timestamp()	
    Entry_Type = generate_entry_type()	
    Region = generate_region()	
    Useless_column = generate_useless_column()	
    Category = generate_category() 
    Transaction_ID = generate_transaction_id()
    Transaction_Code = generate_transaction_code()
    Cart_ID	= generate_card_id()
    Billing_Street_1 = generate_billing_street_1()
    Billing_Street_2 = generate_billing_street_2()
    Billing_State = generate_billing_state()
    Billing_ZIP	= generate_billing_zip()
    Billing_Country	 = generate_billing_country()
    Credit_Card_Number = generate_credit_card_number()
    CVV_Number = generate_cvv_number()
    Card_Type = generate_card_type()
    Transaction_Amount = generate_transaction_amount() 

    #df = pd.DataFrame(data = array, index = index_values, columns = column_values) 

'''generate2()
'''
def generate2(): 
    pass  

'''generate3()
'''
def generate3():  
    pass 

def generate_user_id():
    pass

def generate_org_id():
    pass

def generate_date():
    pass

def generate_timestamp():
    pass

def generate_entry_type():
    pass

def generate_region():
    pass

def generate_useless_column():
    pass

def generate_category():
    pass

def generate_transaction_id():
    pass 

def generate_transaction_code():
    pass 

def generate_card_id():
    pass 

def generate_billing_street_1():
    pass 

def generate_billing_street_2():
    pass 

def generate_billing_state():
    pass 

def generate_billing_zip():
    pass 

def generate_billing_country(): 
    pass 

def generate_credit_card_number():
    pass  

def generate_cvv_number(): 
    pass 

def generate_card_type(): 
    pass 

def generate_transaction_amount(): 
    pass 


''' numpy sample code 
# creating the Numpy array 
array = np.array([[1, 1, 1], [2, 4, 8], [3, 9, 27],  
                  [4, 16, 64], [5, 25, 125], [6, 36, 216],  
                  [7, 49, 343]]) 
  
# creating a list of index names 
index_values = ['first', 'second', 'third', 
                'fourth', 'fifth', 'sixth', 'seventh'] 
   
# creating a list of column names 
column_values = ['number', 'squares', 'cubes'] 
  
# creating the dataframe 
df = pd.DataFrame(data = array,  
                  index = index_values,  
                  columns = column_values) 
'''
  
# displaying the dataframe 
print(df)

