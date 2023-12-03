'''
# generate.py 
# SWENG 411 FA 2023
# Max Piazza 
# Quincy Nguyen 
'''

import datetime
import string
import numpy as np 
import pandas as pd 
import random
#from random_address import real_random_address
  
def main():
    #generate()
    print("1. User ID: " + generate_user_id()) 
    print("2. Org ID: " + generate_org_id())   
    print("3. Date: " + generate_date())
    print("4. Timestamp: " + generate_timestamp())
    print("5. Category: " + str(generate_category()))
    print("6. Transaction ID: " + generate_transaction_id())
    print("7. Transaction code: " + str(generate_transaction_code()))
    print("8. Cart ID: " + str(generate_cart_id()))
    print("9. Billing street 1: " + str(generate_billing_street_1()))
    print("10. Billing street 2: " + str(generate_billing_street_2()))
    print("11. City: " + generate_billing_city())
    print("12. Billing state: " + str(generate_billing_state()))
    print("13. Billing zip: " + generate_billing_zip())
    print("14. Billing country: " + generate_billing_country())
    print("15. Credit card number: " + generate_credit_card_number())
    print("16. Card type: " + generate_card_type())
    print("17. CVV number: " + generate_cvv_number())
    print("18. Transacton amount: " + str(generate_transaction_amount()))
    print("19. Resource ID: " + generate_resource_ID())
    print("20. Error code: " + str(generate_error_code()))
    

""" generate()
# The main generation method which 
"""
def generate(): 
    r = random.randint(1, 3)
    if r == 1:
        data = generate1()
    if r == 2:
        data = generate2()
    if r == 3:
        data = generate3() 

'''
generate1()
'''
def generate1():   
    User_ID	= generate_user_id()
    Org_ID = generate_org_id()
    Date = generate_date()	
    Timestamp = generate_timestamp()	
    Entry_Type = 1
    #Region = generate_region()	
    Category = generate_category() 
    Transaction_ID = generate_transaction_id()
    Transaction_Code = generate_transaction_code()
    Cart_ID	= generate_cart_id()
    Billing_Street_1 = generate_billing_street_1()
    Billing_Street_2 = generate_billing_street_2()
    Billing_City = generate_billing_city()
    Billing_State = generate_billing_state()
    Billing_ZIP	= generate_billing_zip()
    Billing_Country	 = "USA"
    Credit_Card_Number = generate_credit_card_number()
    CVV_Number = generate_cvv_number()
    Card_Type = generate_card_type()
    Transaction_Amount = generate_transaction_amount() 

    #define list of data values 
    data_values = [User_ID, Org_ID, Date, Timestamp, Entry_Type, None, Category, Transaction_ID, Transaction_Code,
            Cart_ID, Billing_Street_1, Billing_Street_2, Billing_State,	Billing_City, Billing_ZIP,	Billing_Country, Credit_Card_Number,
                	CVV_Number,	Card_Type,	Transaction_Amount]

    #define column names
    column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type",
                     "<useless_column>", "Category", "Transaction_ID" , "Transaction_Code", 
                     "Cart_ID", "Billing_Street_1", "Billing_Street_2", "Billing_City", "Billing_State", "Billing_ZIP",
                     "Billing_Country", "Credit_Card_Number", "CVV_Number", "Card_Type", "Transaction_Amount"]

    #create pandas DataFrame out of specified data and column values 
    df = pd.DataFrame(data = data_values, columns = column_values) 
    return df 

'''generate2()
'''
def generate2(): 	
    User_ID	= generate_user_id()
    Org_ID = generate_org_id()
    Date = generate_date()	
    Timestamp = generate_timestamp()		
    Entry_Type = 2 
    #Region = generate_region()	
    Resource_ID = generate_resource_ID() 

    #define list of data values 
    data_values = [User_ID, Org_ID, Date, Timestamp, Entry_Type,None, Resource_ID]

    #define column names
    column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", 
                     "<useless_column>", "Resource_ID"]

    #create pandas DataFrame out of specified data and column values 
    df = pd.DataFrame(data = data_values, columns = column_values) 
    return df 

'''generate3() 
'''
def generate3():  
    User_ID	= generate_user_id()
    Org_ID =  generate_org_id()
    Date = generate_date()	
    Timestamp = generate_timestamp()			
    Entry_Type = 3
    #Region = generate_region()	
    Resource_ID	= generate_resource_ID() 
    Error_Code = generate_error_code() 

    #define list of data values 
    data_values = [User_ID, Org_ID, Date, Timestamp, Entry_Type, None, Resource_ID, Error_Code]

    #define column names
    column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", 
                     "<useless_column>", "Resource_ID", "Error_Code"]

    #create pandas DataFrame out of specified data and column values 
    df = pd.DataFrame(data = data_values, columns = column_values) 
    return df 

'''generate_user_id() 
# Generates a random 9-digit user id
# Valid data case: 9 random digits
# Invalid data case: 8 random digits 
'''
def generate_user_id():
    # randomly generate either valid data (1) or invalid data (2)
    output = ""
    r = random.randint(1, 2)
    if r == 1: #generate valid data 
        for i in range(9): #generate a sequence of 9 random integers 
            random_number = random.randint(0, 9)
            output = output + str(random_number)
        return output
    if r == 2: #generate invalid data 
        for i in range(8): #generate a sequence of 8 random integers 
            random_number = random.randint(0, 9)
            output = output + str(random_number)
        return output 

'''generate_org_id()
# Generates a random 12-character organization id
# Valid data case: 12 random digits and letters 
# Invalid data case: 9 random digits and letters 
'''
def generate_org_id():
    output = "" 
    r = random.randint(1, 2) # randomly generate either valid data (1) or invalid data (2)
    if r == 1: #generate valid data 
        for i in range(12): # generate a sequence of 12 random characters 
            q = random.randint(1,2) # decide if next character will be a letter or number randomly 
            if q == 1: #add a number
                random_number = random.randint(0, 9)
                output = output + str(random_number)
            if q == 2: #add a character
                randomLetter = random.choice(string.ascii_letters)
                output = output + randomLetter
        return output
    if r == 2: #generate invalid data 
        for i in range(9): # generate a sequence of 9 random characters 
            q = random.randint(1,2) # decide if next character will be a letter or number randomly 
            if q == 1: #add a number
                randomNumber = random.randint(0, 9)
                output = output + str(randomNumber)
            if q == 2: #add a character
                randomLetter = random.choice(string.ascii_letters)
                output = output + randomLetter
        return output
    
'''generate_date()
    # Generates a string version of the date using the datetime library 
    # Valid data case: date in the format "MM/DD/YYYY"
    # Invalid data case: date in the format "DD/MM/YYYY"
'''
def generate_date():
    output = None 
    r = random.randint(1, 2) # randomly generate either valid data (1) or invalid data (2)
    date = datetime.datetime.now()
    if r == 1:
        output = date.strftime("%m") + "/" + date.strftime("%d") + "/" + date.strftime("%Y")
    if r == 2:
        output = date.strftime("%d") + "/" + date.strftime("%m") + "/" + date.strftime("%Y")
    return output

'''generate_timestamp()
# Generates a string version of the time using the datetime library 
# Valid data case: timestamp in the form "HH:MM:SS AM/PM" with hour in 12-hour time
# Invalid data case: timestamp in the form "HH:MM:SS AM/PM" with hour in 24-hour time 
'''
def generate_timestamp():
    output = "" 
    r = random.randint(1, 2) # randomly generate either valid data (1) or invalid data (2)
    date = datetime.datetime.now()
    if r == 1:
        output = date.strftime("%I") + ":" + date.strftime("%M") + ":" + date.strftime("%S") + " " + date.strftime("%p")
    if r == 2:
        output = date.strftime("%H") + ":" + date.strftime("%M") + ":" + date.strftime("%S") + " " + date.strftime("%p")
    return output

'''generate_region()
# We decided to use remove this field from our data. 
But this method has been retained for extensibility.
'''
#def generate_region():
#pass

'''generate_category()
# Random integer
'''
def generate_category():
    category = random.randint(0, 9) 
    return category
   

'''generate_transaction_id()
# Returns a string of 13 consecutive random integers.
'''
def generate_transaction_id():
    output = ""
    for i in range(13): #generate a sequence of 9 random integers 
        random_number = random.randint(0, 9)
        output = output + str(random_number)
    return output

'''generate_transaction_code()
'''
def generate_transaction_code():
    output = random.randint(0, 3)
    return output
    

'''generate_cart_id()
# Generates a string of 13 random integers.
'''
def generate_cart_id():
    rand_cart_id = [random.randint(0, 9) for _ in range(13)]
    # Convert the list of integers to a string
    res = ''.join(map(str, rand_cart_id))
    return "#" + res
     

'''generate_billing_street_1()
# Returns street number, street name and street type.
'''
def generate_billing_street_1():
    street_names = ["Main", "Oak", "Maple", "Pine", "Cedar", "Elm", "Birch", "Spruce", "Hill", "Valley", "Meadow", "Brook", "River", "Lake", "Park"]
    street_types = ["St", "Ave", "Blvd", "Ln", "Dr", "Rd", "Ct", "Way", "Pl"]

    street_name = random.choice(street_names)
    street_type = random.choice(street_types)
    street_number = random.randint(100, 9999)

    return f"{street_number} {street_name} {street_type}"

''' generate_billing_street_2()
# Currently returns an empty string
# This method can expanded later with addt'l logic
'''
def generate_billing_street_2():
    return "" 

''' generate_billing_city()
# This method generates a random city name from a list of 300 possible cities 
'''
def generate_billing_city(): 
    city_Array = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", 
                    "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Columbus", "Indianapolis", "Fort Worth", 
                    "Charlotte", "Seattle", "Denver", "El Paso", "Detroit", "Washington", "Boston", "Memphis", "Nashville", 
                    "Portland", "Oklahoma City", "Las Vegas", "Baltimore", "Louisville", "Milwaukee", "Albuquerque", "Tucson", 
                    "Fresno", "Sacramento", "Mesa", "Atlanta", "Kansas City", "Colorado Springs", "Miami", "Raleigh", "Omaha", 
                    "Long Beach", "Virginia Beach", "Oakland", "Minneapolis", "Tulsa", "Arlington", "Tampa", "New Orleans", 
                    "Wichita", "Bakersfield", "Cleveland", "Aurora", "Anaheim", "Honolulu", "Santa Ana", "Riverside", 
                    "Corpus Christi", "Lexington", "Stockton", "St. Louis", "Saint Paul", "Henderson", "Pittsburgh", "Cincinnati", 
                    "Anchorage", "Greensboro", "Plano", "Newark", "Lincoln", "Orlando", "Irvine", "Toledo", "Durham", "Chula Vista", 
                    "Fort Wayne", "Jersey City", "St. Petersburg", "Laredo", "Madison", "Buffalo", "Lubbock", "Chandler", "Scottsdale", 
                    "Glendale", "Reno", "Norfolk", "Winston-Salem", "North Las Vegas", "Irving", "Chesapeake", "Gilbert", "Hialeah", 
                    "Garland", "Fremont", "Baton Rouge", "Richmond", "Boise", "San Bernardino", "Spokane", "Birmingham", "Modesto", 
                    "Des Moines", "Rochester", "Tacoma", "Fontana", "Oxnard", "Moreno Valley", "Fayetteville", "Huntington Beach", 
                    "Yonkers", "Aurora", "Montgomery", "Amarillo", "Little Rock", "Akron", "Shreveport", "Augusta", "Grand Rapids", 
                    "Mobile", "Salt Lake City", "Huntsville", "Tallahassee", "Grand Prairie", "Overland Park", "Knoxville", "Worcester", 
                    "Brownsville", "Newport News", "Santa Clarita", "Port St. Lucie", "Providence", "Fort Lauderdale", "Chattanooga", 
                    "Tempe", "Oceanside", "Garden Grove", "Rancho Cucamonga", "Cape Coral", "Santa Rosa", "Vancouver", "Sioux Falls", 
                    "Ontario", "Peoria", "Springfield", "Pembroke Pines", "Elk Grove", "Salem", "Corona", "Eugene", "McKinney", 
                    "Fort Collins", "Lancaster", "Cary", "Palmdale", "Hayward", "Salinas", "Frisco", "Springfield", "Pasadena", 
                    "Macon", "Alexandria", "Pomona", "Lakewood", "Sunnyvale", "Escondido", "Kansas City", "Hollywood", 
                    "Clarksville", "Joliet", "Rockford", "Torrance", "Naperville", "Savannah", "Paterson", "Bridgeport", 
                    "Mesquite", "Killeen", "Syracuse", "McAllen", "Pasadena", "Bellevue", "Fullerton", "Orange", "Dayton", 
                    "Miramar", "Thornton", "West Valley City", "Olathe", "Hampton", "Warren", "Midland", "Waco", "Charleston", 
                    "Denton", "Cedar Rapids", "New Haven", "Roseville", "Gainesville", "Visalia", "Coral Springs", "Thousand Oaks", 
                    "Elizabeth", "Stamford", "Concord", "Surprise", "Lafayette", "Topeka", "Kent", "Simi Valley", "Santa Clara", 
                    "Murrieta", "Hartford", "Athens", "Victorville", "Abilene", "Norman", "Vallejo", "Berkeley", "Round Rock", 
                    "Ann Arbor", "Cambridge", "Livonia", "Abilene", "Amarillo", "Beaumont", "Carrollton", "Erie", "Evansville", 
                    "Independence", "Provo", "Arvada", "El Monte", "Lansing", "Midland", "Westminster", "Bridgeport", "Clearwater", 
                    "Costa Mesa", "Fairfield", "Inglewood", "Manchester", "Murrieta", "Norwalk", "Pueblo", "Richmond", "Temecula", 
                    "Waterbury", "West Covina", "Billings", "Broken Arrow", "Burbank", "Centennial", "Daly City", "Downey", "Elgin", 
                    "Enterprise", "Fairfield", "Fargo", "Fayetteville", "Gresham", "Hillsboro", "Jurupa Valley", "Killeen", "Lakeland", 
                    "Lewisville", "Lowell", "Murfreesboro", "Nampa", "North Charleston", "Odessa", "Palm Bay", "Pearland", "Renton", 
                    "Richardson", "South Bend", "Sterling Heights", "Surprise", "Tempe", "Thornton", "Tyler", "Ventura", "West Jordan", 
                    "West Palm Beach", "Wichita Falls", "Albany", "Allen", "Beaverton", "Brockton", "Broomfield", "Carmel", "Champaign", 
                    "Clarksville", "Davenport", "Deerfield Beach", "Edinburg", "Fall River", "Fayetteville", "Fishers", "Gary", 
                    "Greeley", "Hammond", "Hesperia", "High Point", "Hoboken", "Hoover", "Janesville", "Kenosha", "Lakewood", "Lawton", 
                    "League City", "Lee's Summit", "Manchester", "Medford", "Meridian", "Mission Viejo", "New Bedford", "Newton", 
                    "Noblesville", "Norwalk", "O'Fallon", "Orem", "Parma", "Perris", "Plymouth", "Quincy", "Rialto", "Rock Hill", "Rogers", 
                    "Rosemead", "Roswell", "Round Rock", "Ryde", "Sandy", "Santa Maria", "Santa Monica", "Santa Rosa", "Shawnee", "Somerville", 
                    "South Gate", "South San Francisco", "Southfield", "St. Cloud", "St. George", "St. Joseph", "St. Louis Park"]
    random_number = random.randint(0, 299)
    return city_Array[random_number]

'''generate_billing_state()
# Returns a random 2-character state abbreviation from a list of 50 
'''
def generate_billing_state():
    output_Array = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", 
                    "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", 
                    "VA", "WA", "WV", "WI", "WY"]
    
    random_number = random.randint(0, 49)
    return output_Array[random_number]

'''generate_billing_zip() 
# Generates a string of 5 random numbers.
'''
def generate_billing_zip():
    output = ""
    for i in range(5): #generate a sequence of 9 random integers 
        random_number = random.randint(0, 9)
        output = output + str(random_number)
    return output

'''generate_billing_country()
# We decided to use USA as the billing country. But this method has been retained for extensibility.
'''
def generate_billing_country():  
    return "USA"

'''generate_credit_card_number()
# Generates a string containing 4 sequences of 4 random ints, with 3 dashes 
# inserted after the 1st through third sequences of ints 
'''
def generate_credit_card_number():
    output = ""
    for i in range(4):
        for J in range(4): #generate a sequence of 9 random integers 
            random_number = random.randint(0, 9)
            output = output + str(random_number)
        if i != 3:
            output = output + "-" 
    return output 
    

'''generate_cvv_number()
# Generates a string contaning 3 random integers
'''
def generate_cvv_number(): 
    output = ""
    for i in range(3): #generate a sequence of 9 random integers 
        random_number = random.randint(0, 9)
        output = output + str(random_number)
    return output
    

'''generate_card_type()
# Generates a string randomly containing either 'Mastercard', 'Visa', 
# 'American Express', or 'Discover'
'''
def generate_card_type(): 
    card_Array = ['Mastercard', 'Visa', 'American Express', 'Discover']
    random_number = random.randint(0, 3)
    return card_Array[random_number]

'''generate_transaction_amount()
# Generates string containing an integer between 0-1000 followed by a "."
# then a sequence of two random integers between 0-9
'''
def generate_transaction_amount(): 
    dollars = str(random.randint(0, 1000))
    cents_1 = str(random.randint(0, 9))
    cents_2 = str(random.randint(0, 9))
    output = dollars + "." + cents_1 + cents_2
    
    return output

'''generate_resource_ID()
# This method generates a string containing a sequence of 5 random characters followed 
# by an underscore then a sequence of 6 random integers and finally another random character. 
'''
def generate_resource_ID(): 
    random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    underscore = "_"
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(6))
    random_char = random.choice(string.ascii_letters)
    result_string = f"{random_chars}{underscore}{random_numbers}{random_char}"
    return result_string

''' generate_error_code() 
# This method generates a random error code from a list of 62 HTTP error code options 
'''
def generate_error_code():
    error_Array = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 
                   304, 305, 306, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 
                   412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 428, 429, 431, 451,
                     500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
    random_number = random.randint(0, 61)
    return error_Array[random_number]

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

if __name__ == "__main__":
    main()