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
    cs.execute("USE warehouse VIVEK_WH")
    cs.execute("USE snowflake_sample_data.tpch_sf1")
    cs.execute("select o.* from orders o join customer c on o.O_CUSTKEY = c.C_CUSTKEY and c.c_custkey = 75001;")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()
