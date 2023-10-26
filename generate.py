'''
# generate.py 
# SWENG 411 FA 2023
# Max Piazza 
# Quincy Nguyen 
'''

#!/usr/bin/env python3

import numpy as np 
import pandas as pd 
  
def main():
    generate()

if __name__ == "__main__":
    main()


""" generate()

"""
def generate: 
    r = random.randint(1, 3)
    if r = 1:
        generate1()
    if r = 2:
        generate2()
    if r = 3:
        generate3() 
    #generate 

'''generate1()
'''
def generate1():   
    User_ID	= generate_user_id()
    Org_I
    Date	
    Timestamp	
    Entry_Type	
    Region	
    <useless_column>	
    Category	
    Transaction_ID	
    Transaction_Code	
    Cart_ID	Billing_Street_1	
    Billing_Street_2	
    Billing_State	
    Billing_ZIP	
    Billing_Country	
    Credit_Card_Number	
    CVV_Number	
    Card_Type	
    Transaction_Amount

    df = pd.DataFrame(data = array, index = index_values, columns = column_values) 

'''generate2()
'''
def generate2():   

'''generate3()
'''
def generate3():   

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

