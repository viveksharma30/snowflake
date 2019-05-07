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
    cs.execute("create or replace table DD07T(DOMNAME string,DDLANGUAGE string, AS4LOCAL string, VALPOS string, AS4VERS string ,DDTEXT string , DOMVAL_LD string, DOMVAL_HD string,DOMVALUE_L string)")



finally:
    cs.close()
ctx.close()
