"""API for multiDimMatrix table"""
import sys
sys.path.append('/home/ardelalegre/SoundMapping/Database')
from DatabaseAPI import DatabaseAPI

class MultiDimMatrixService:
   
    def __init__(self):
        self.database = DatabaseAPI()
    
    
    """
    Query for data points between a time interval

    @param datetime.datetime start_time - begininng of time interval
    @param datetime.datetime end_time - end of time interval

    @return data from query
    """
    def get_time_interval_object(self, start_time, end_time):
        
        query = '''
        SELECT *
        FROM multiDimMatrix
        WHERE quantized_time >= {0} AND quantized_time < {1}
        '''.format(start_time, end_time)
        
        return self.database.execute_query(query)