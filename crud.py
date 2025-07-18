import psycopg2

# Connect to the default 'postgres' database
try:
    connection_obj = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='1234',
        database="indigo"
    )
    connection_obj.autocommit = True  # ✅ REQUIRED for CREATE DATABASE
    mycursor = connection_obj.cursor()

    #mycursor.execute("CREATE DATABASE indigo")
    #print("Database 'indigo' created successfully!")
    # mycursor.execute("""
    #                  create table airport(
    #                      airport_id integer primary key,
    #                      code varchar(10),
    #                      city varchar(50),
    #                      name varchar(50)
    #                  )
    #                  """)
    #connection_obj.commit()
    
    #insert into table
    # mycursor.execute("""
    #                  insert into airport values
    #                  (1,'Del','New Delhi','IGIA'),
    #                  (2,'CCU','Kolkata','NSCA'),
    #                  (3,'bom','mumbai','csma')
    #                  """)
    # connection_obj.commit()
    
#     mycursor.execute("""
#                     CREATE TABLE flights_cleaned (
#     Airline VARCHAR(100),
#     Date_of_Journey DATE,
#     Source VARCHAR(50),
#     Destination VARCHAR(50),
#     Route TEXT,
#     Dep_Time TIME,
#     Duration VARCHAR(20),
#     Total_Stops VARCHAR(20),
#     Price INTEGER
# )""")
#     connection_obj.commit()
    
    # Open CSV file
    with open('flights.csv', 'r') as f:
        next(f)
        mycursor.copy_from(f, 'flights_cleaned', sep=',', null='')

    # Commit and close
    connection_obj.commit()
    mycursor.close()
    connection_obj.close()
except Exception as e:
    print("Error:", e)