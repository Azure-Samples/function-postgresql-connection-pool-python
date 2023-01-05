import logging

import azure.functions as func
import psycopg2
import psycopg2.pool


# Connection details
host = "myostgresql.postgres.database.azure.com"
user = "username"
password = "securepassword"
db_name = "mypgsqldb"

# Create a connection pool
pool = psycopg2.pool.SimpleConnectionPool(
    1, # minimum number of connections
    20, # maximum number of connections
    host=host,
    user=user,
    password=password,
    dbname=db_name
)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        query = "SELECT * FROM mytable"
        # Get a connection from the pool
        connection = pool.getconn()
        
        # Create a cursor
        cursor = connection.cursor()
        logging.info('Max connection.' + str (pool.maxconn))
        # Execute the query
        #cursor.execute(query)
        # Fetch the results
        #rows = cursor.fetchall()
        # Close the cursor and connection
        #cursor.close()
        pool.putconn(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while running the query", error)

   
    return func.HttpResponse(
            "This HTTP triggered function executed successfully.",
            status_code=200
    )
