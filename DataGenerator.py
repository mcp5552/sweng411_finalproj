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
import string
import datetime
from ETLSystem import Feature
from ETLSystem import DataHandler
  
''' main()
# Calls the generate() method one time to generate random data 
# then sends that data to an S3 bucket for processing 
'''
def main():
    # Instantiate a DataGenerator object 
    dg = DataGenerator() 
    # Get some data by using the DataGenerator generate() method
    data = dg.generate()
    print("Data Generated.") 
    print(data.to_string())

    # Create a DataHandler instance 
    dh = DataHandler()

    # call the sendCSV method on the data   
    print("Sending data to cloud...") 
    dh.sendCsv(data)
    print("Sent!") 

''' class DataGenerator
# Contains the definition of the generate() method and all the sub-methods
# needed to generate demo data.  
'''
class DataGenerator(Feature):
    ''' Class Constructor
    # Here in case needed later 
    '''
    def __init__(self):
        pass   

    """ generate()
    # The main generation method which randomly generates one of 
    # 3 types of data
    """
    def generate(self): 
        r = random.randint(1, 3)
        print("Generating data of type: " + str(r) + "...")
        if r == 1:
            data = self.generate1()
        if r == 2:
            data = self.generate2()
        if r == 3:
            data = self.generate3() 
        return data 

    ''' generate1()
    # This is the generator method for data of type 1
    '''
    def generate1(self):   
        User_ID	= self.generate_user_id()
        Org_ID = self.generate_org_id()
        Date = self.generate_date()	
        Timestamp = self.generate_timestamp()	
        Entry_Type = 1
        #Region = self.generate_region()	
        Category = self.generate_category() 
        Transaction_ID = self.generate_transaction_id()
        Transaction_Code = self.generate_transaction_code()
        Cart_ID	= self.generate_cart_id()
        Billing_Street_1 = self.generate_billing_street_1()
        Billing_Street_2 = self.generate_billing_street_2()
        Billing_City = self.generate_billing_city()
        Billing_State = self.generate_billing_state()
        Billing_ZIP	= self.generate_billing_zip()
        Billing_Country	 = "USA"
        Credit_Card_Number = self.generate_credit_card_number()
        CVV_Number = self.generate_cvv_number()
        Card_Type = self.generate_card_type()
        Transaction_Amount = self.generate_transaction_amount() 

        #define list of data values 
        data_values = np.array([[User_ID, Org_ID, Date, Timestamp, Entry_Type, 
                                None, Category, Transaction_ID, Transaction_Code, Cart_ID, Billing_Street_1, 
                                Billing_Street_2, Billing_City, Billing_State, Billing_ZIP, Billing_Country, 
                                Credit_Card_Number, CVV_Number, Card_Type, Transaction_Amount]])

        #define column names
        column_names = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", "<useless_column>", "Category", 
                        "Transaction_ID" , "Transaction_Code", "Cart_ID", "Billing_Street_1", "Billing_Street_2", 
                        "Billing_City", "Billing_State", "Billing_ZIP", "Billing_Country", "Credit_Card_Number", 
                        "CVV_Number", "Card_Type", "Transaction_Amount"]

        #create pandas DataFrame out of specified data and column values 
        df = pd.DataFrame(data = data_values, columns = column_names) 
        return df 

    '''generate2()
    # This is the generator method for data of type 2
    '''
    def generate2(self): 	
        User_ID	= self.generate_user_id()
        Org_ID = self.generate_org_id()
        Date = self.generate_date()	
        Timestamp = self.generate_timestamp()		
        Entry_Type = 2 
        #Region = self.generate_region()	
        Resource_ID = self.generate_resource_ID() 

        #define list of data values 
        data_values = np.array([[User_ID, Org_ID, Date, Timestamp, Entry_Type, None, Resource_ID]])

        #define column names
        column_values = ["User_ID", "Org_ID", "Date", "Timestamp", "Entry_Type", 
                        "<useless_column>", "Resource_ID"]

        #create pandas DataFrame out of specified data and column values 
        df = pd.DataFrame(data = data_values, columns = column_values) 
        return df 

    '''generate3()
    # This is the generator method for data of type 3 
    '''
    def generate3(self):  
        User_ID	= self.generate_user_id()
        Org_ID =  self.generate_org_id()
        Date = self.generate_date()	
        Timestamp = self.generate_timestamp()			
        Entry_Type = 3
        #Region = self.generate_region()	
        Resource_ID	= self.generate_resource_ID() 
        Error_Code = self.generate_error_code() 

        #define list of data values 
        data_values = np.array([[User_ID, Org_ID, Date, Timestamp, Entry_Type, None, Resource_ID, Error_Code]])

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
    def generate_user_id(self):
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
    def generate_org_id(self):
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
    def generate_date(self):
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
    def generate_timestamp(self):
        output = None 
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
    def generate_region(self):
        pass

    '''generate_category()
    # Returns a random integer from 0-9 
    '''
    def generate_category(self):
        category = random.randint(0, 9) 
        return category

    '''generate_transaction_id()
    # Returns a string of 13 consecutive random integers.
    '''
    def generate_transaction_id(self):
        output = ""
        for i in range(13): #generate a sequence of 9 random integers 
            random_number = random.randint(0, 9)
            output = output + str(random_number)
        return output


    '''generate_transaction_code()
    # Returns a string of random integers from 0 to 3.
    '''
    def generate_transaction_code(self):
        output = random.randint(0, 3)
        return output
        

    '''generate_cart_id()
    # Generates a string of 13 random integers.
    '''
    def generate_cart_id(self):
        rand_cart_id = [random.randint(0, 9) for _ in range(13)]
        # Convert the list of integers to a string
        res = ''.join(map(str, rand_cart_id))
        return "#" + res

    '''generate_billing_street_1()
    # Returns a string containing a random number from 1-9999 followed by a space then
    # A randomly generated street name. Street names are 2-word names with each word
    # randomly generated from a separate list of possible words e.g. "Oak St"
    '''
    def generate_billing_street_1(self):
        street_names = ["Main", "Oak", "Maple", "Pine", "Cedar", "Elm", "Birch", "Spruce", "Hill", "Valley", "Meadow", "Brook", "River", "Lake", "Park"]
        street_types = ["St", "Ave", "Blvd", "Ln", "Dr", "Rd", "Ct", "Way", "Pl"]
        street_name = random.choice(street_names)
        street_type = random.choice(street_types)
        street_number = random.randint(1, 9999)
        return f"{street_number} {street_name} {street_type}"

    ''' generate_billing_street_2()
    # Currently returns an empty string
    # This method can expanded later with addt'l logic
    '''
    def generate_billing_street_2(self):
        return ""

    '''generate_billing_city()
    # This method generates a random city name from a list of 300 possible cities 
    '''
    def generate_billing_city(self): 
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
    # Returns a random 2-character state abbreviation string from a list of 50
    '''
    def generate_billing_state(self):
        output_Array = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", 
                        "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", 
                        "VA", "WA", "WV", "WI", "WY"]
        
        random_number = random.randint(0, 49)
        return output_Array[random_number]

    '''generate_billing_zip() 
    # Generates a string of 5 random numbers.
    '''
    def generate_billing_zip(self):
        output = ""
        for i in range(5): #generate a sequence of 9 random integers 
            random_number = random.randint(0, 9)
            output = output + str(random_number)
        return output

    '''generate_billing_country()
    # We decided to use USA as the billing country. But this method has been retained for extensibility.
    '''
    def generate_billing_country(self):  
        return "USA"

    '''generate_credit_card_number()
    # Generates a string containing 4 sequences of 4 random ints, with 3 dashes 
    # inserted after the 1st through third sequences of ints 
    '''
    def generate_credit_card_number(self):
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
    def generate_cvv_number(self): 
        output = ""
        for i in range(3): #generate a sequence of 9 random integers 
            random_number = random.randint(0, 9)
            output = output + str(random_number)
        return output
        

    '''generate_card_type()
    # Generates a string randomly containing either 'Mastercard', 
    # 'Visa', 'American Express', or 'Discover'
    '''
    def generate_card_type(self): 
        card_Array = ['Mastercard', 'Visa', 'American Express', 'Discover']
        random_number = random.randint(0, 3)
        return card_Array[random_number]

    '''generate_transaction_amount()
    # Generates string containing an integer between 0-1000 followed by a "."
    # then a sequence of two random integers between 0-9 
    '''
    def generate_transaction_amount(self): 
        dollars = str(random.randint(0, 1000))
        cents_1 = str(random.randint(0, 9))
        cents_2 = str(random.randint(0, 9))
        output = dollars + "." + cents_1 + cents_2
        return output

    '''generate_resource_ID()
    # This method generates a string containing a sequence of 5 random characters followed 
    # by an underscore then a sequence of 6 random integers and finally another random character. 
    '''
    def generate_resource_ID(self): 
        random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        underscore = "_"
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(6))
        random_char = random.choice(string.ascii_letters)
        result_string = f"{random_chars}{underscore}{random_numbers}{random_char}"
        return result_string

    ''' generate_error_code() 
    # This method generates a random error code from a list of 62 HTTP error code options 
    '''
    def generate_error_code(self):
        error_Array = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 
                    304, 305, 306, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 
                    412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 428, 429, 431, 451,
                        500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
        random_number = random.randint(0, 61)
        return error_Array[random_number]

''' 
# Definition of main method for demo / dev purposes 
'''
if __name__ == "__main__":
        main()