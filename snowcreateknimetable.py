#!/usr/bin/env python
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='viveksharma30',
    password='ShwetaSaraswat!234',
    account='kx62732.east-us-2.azure'
    
    )
cs = ctx.cursor()
try:
    #cs.execute("SELECT current_version()")
    # Creating database, schema and warehouse if not exists
    #cs.execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse")
    #cs.execute("CREATE DATABASE IF NOT EXISTS testdb")
    #cs.execute("USE DATABASE testdb")
    #cs.execute("CREATE SCHEMA IF NOT EXISTS testschema")
    #print(one_row[0])

    #using warehouse and schema to create table
    cs.execute("USE warehouse tiny_warehouse")
    cs.execute("USE schema testdb.testschema")
    #cs.execute("create or replace table DD07T(DOMNAME string,DDLANGUAGE string, AS4LOCAL string, VALPOS string, AS4VERS string ,DDTEXT string , DOMVAL_LD string, DOMVAL_HD string,DOMVALUE_L string)")
    cs.execute ("create or replace table nyc_taxi_data ("
"medallion			 string"
",hack_license       string"
",vendor_id          string"
",payment_type       string"
",fare_amount        string"
",surcharge          string"
",mta_tax            string"
",tip_amount         string"
",tolls_amount       string"
",total_amount       string"
",rate_code          string"
",pickup_datetime    string"
",dropoff_datetime   string"
",passenger_count    string"
",trip_time_in_secs  string"
",trip_distance      string"
",pickup_longitude   string"
",pickup_latitude    string"
",dropoff_longitude  string"
",dropoff_latitude   string"
",credit_card        string"
")"
)


finally:
    cs.close()
ctx.close()
