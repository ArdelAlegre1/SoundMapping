"""API for Database"""
import sys
from sqlalchemy import create_engine


class DatabaseAPI:
    
    def __init__(self):
        """database engine object used to access database"""
        self.database_engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                               .format(user="root",
                                       pw="test",
                                       db="odas_db_proc"))


    """Executes query to database

        @param String query - query to be exectued

        @return data from query or null"""
    def execute_query(self, query):

        try:
            return self.database_engine.execute(query)

        except Exception as e:

            print("Error when making query:\n{}".format(query), file=sys.stderr)
            raise e