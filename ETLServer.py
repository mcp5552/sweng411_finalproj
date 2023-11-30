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

'''main() 
# Creates an ETL Server class instance and runs the
# serve() method from that class 
'''
def main():
    #create an instance of the ETL server class
    ETL_server = ETLServer()

    # constantly perform the serve() method
    while True:
        ETL_server.serve()

''' ETLServer
# This class 
'''
class ETLServer:
    def __init__(self):
        # Instantiate the dataHandler to be used by this class object
        dh = DataHandler()

    ''' serve()
    # This method 
    '''
    def serve(self):
        #read in a csv file as a pandas dataframe
        df = self.dh.getCSV() 

        #verify CSV data has been retrieved successfully 
        VerifyData.verifyInData()

        #sanitize the data 
        df = Transform.sanitize(df)

        #load the data        
        self.dh.load(df) 

        #verify that parquet data has been sent successfully 
        VerifyData.verifyOutData() 


class VerifyData:
    def verifyInData():
        return True
    def verifyOutData():
        return False

class Logger(Feature):
    def writeToLog():
        pass 

class Transform:
    def sanitize(df):
        pass 

# 
if __name__== "__main__":
    main()