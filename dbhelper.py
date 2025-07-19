import streamlit as st
import psycopg2

class DB:
    def __init__(self):
        try:
            self.connection_obj = psycopg2.connect(
                host=st.secrets["general"]["DB_HOST"],
                user=st.secrets["general"]["DB_USER"],
                password=st.secrets["general"]["DB_PASSWORD"],
                database=st.secrets["general"]["DB_NAME"]
            )
            self.connection_obj.autocommit = True
            self.mycursor = self.connection_obj.cursor()

        except Exception as e:
            st.error(f"Database connection failed: {e}")  # ✅ shows error in Streamlit app
            self.connection_obj = None
            self.mycursor = None
    def fetch_city_name(self):
        city=[]
        try:
            self.mycursor.execute("""
                SELECT DISTINCT(destination) FROM flights_cleaned
                UNION
                SELECT DISTINCT(source) FROM flights_cleaned;
            """)
            data = self.mycursor.fetchall()
            for item in data:
                city.append(item[0])
            return city
        except Exception as e:
            print("Error fetching city names:", e)
            
    def fetch_all_flights(self, source, destination):
        query = """
            SELECT airline, route, dep_time, duration, price
            FROM flights_cleaned
            WHERE destination = %s AND source = %s
        """
        self.mycursor.execute(query, (destination, source))
        data = self.mycursor.fetchall()
        return data
    
    def fetch_airlines_frequency(self):
        airline=[]
        count=[]
        self.mycursor.execute("""
                              select airline,count(*)
                              from flights_cleaned
                              group by airline
                              """)
        data=self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            count.append(item[1])
        return airline,count
    
    def busy_airport(self):
        name=[]
        count=[]
        self.mycursor.execute("""
                              select source,count(*)
                                from(select source
                                from flights_cleaned
                                union all
                                select destination
                                from flights_cleaned) t
                                group by t.source
                                order by count(*) desc
                              """)
        data=self.mycursor.fetchall()
        for item in data:
            name.append(item[0])
            count.append(item[1])
        return name,count
    
    def flights_per_day(self):
        date=[]
        count=[]
        self.mycursor.execute("""
                              select date_of_journey,count(*)
                                from flights_cleaned
                                group by date_of_journey
                                order by date_of_journey
                              """)
        data=self.mycursor.fetchall()
        
        for item in data:
            date.append(item[0])
            count.append(item[1])
        return date,count
    
    def non_stop_vs_connecting(self):
        airline=[]
        stops_count=[]
        Flight_Count=[]
        self.mycursor.execute("""
                              SELECT Airline, Total_Stops,COUNT(*) AS flight_count
                            FROM
                                flights_cleaned
                            GROUP BY
                                Airline, Total_Stops
                            ORDER BY
                                Airline, Total_Stops;
                              """)
        data=self.mycursor.fetchall()
        
    
        return data
    
    def fastest_airlines(self):
        
        self.mycursor.execute("""
                          SELECT
                            Airline,
                            ROUND(AVG(Duration::INT)) AS avg_duration_minutes
                        FROM
                            flights_cleaned
                        GROUP BY
                            Airline
                        ORDER BY
                            avg_duration_minutes ASC;
                              """)
        data=self.mycursor.fetchall()
        
        return data
    
    
    def cheapest_flights(self):
                
        self.mycursor.execute("""
                          SELECT 
                            Airline, 
                            ROUND(AVG(price)) AS avg_price
                        FROM flights_cleaned
                        GROUP BY Airline
                        ORDER BY avg_price ASC;

                              """)
        data=self.mycursor.fetchall()
        
        return data