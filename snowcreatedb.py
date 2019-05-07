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
    cs.execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse")
    cs.execute("CREATE DATABASE IF NOT EXISTS testdb")
    cs.execute("USE DATABASE testdb")
    cs.execute("CREATE SCHEMA IF NOT EXISTS testschema")
    print(one_row[0])
finally:
    cs.close()
ctx.close()
