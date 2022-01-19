import psycopg
import pandas as pd
import datetime

try:
    connection = psycopg.connect(user="sungjunchoi", password="1234", dbname='covidtracker')
    cursor = connection.cursor()
    print(cursor)
    print("PostgreSQL server information")
    record = ""
    for i in range(1,0,-1):
        year = (datetime.datetime.now()- datetime.timedelta(days=i)).strftime("%Y")
        month = (datetime.datetime.now()- datetime.timedelta(days=i)).strftime("%m")
        day = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%d")

        print(year + ' ' + month+ ' ' + day)
        
        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/" + month + '-' + day + '-' + year + ".csv"

        data = pd.read_csv(url)
        data = data[['Province_State', 'Confirmed', 'Deaths', 'Lat', 'Long_']]
        data = data.astype({'Deaths': 'int'})


        states = data.values.tolist()

        # print(states)

        # create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS states(
                id serial PRIMARY KEY,
                name varchar NOT NULL,
                confirmed varchar NOT NULL,
                deaths varchar NOT NULL,
                lat varchar,
                long varchar
            );
        """)


        # add states data
        for state in states:
            # state = ['state_name', 'confirmed', 'Deaths', 'Lat', 'Long']
            if state[0] != 'American Samoa' and state[0] != 'Diamond Princess' and state[0] != 'Grand Princess':
                cursor.execute(f"INSERT INTO states (name, confirmed, deaths, lat, long) VALUES ('{state[0]}', '{state[1]}', '{state[2]}', '{state[3]}', '{state[4]}');")
    cursor.execute("SELECT * FROM states")
    # print queries
    for record in cursor:
        print(record)
    cursor.fetchall()
    connection.commit()

except (Exception) as error:
    print("Error while connecting to PostgreSQL: ", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
