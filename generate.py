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
    Entry_Type = 1
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
    User_ID	= generate_user_id()
    Org_ID = generate_org_id()
    Date = generate_date()	
    Timestamp = generate_timestamp()		
    Entry_Type = 2 
    Region = generate_region()	
    Resource_ID = generate_resource_ID() 


'''generate3() 
'''
def generate3():  
    User_ID	= generate_user_id()
    Org_ID =  generate_org_id()
    Date = generate_date()	
    Timestamp = generate_timestamp()			
    Entry_Type = 3
    Region = generate_region()	
    Resource_ID	= generate_resource_ID() 
    Error_Code = generate_error_code() 


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

'''generate_region()
'''
def generate_region():
    pass

'''generate_useless_column()
'''
def generate_useless_column():
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
#print(df)

