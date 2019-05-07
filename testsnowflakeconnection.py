#!/usr/bin/env python
import snowflake.connector
#import os
# Get the version
conn = snowflake.connector.connect (
    user = 'viveksharma30'
    ,password = 'ShwetaSaraswat!234'
    ,account = 'kx62732.east-us-2.azure'
    ,database = 'testdb'
    ,schema = 'testschema'
    ,warehouse = 'tiny_warehouse'
    )


cs =conn.cursor()
try:
    #cs.execute("show databases")
    #cs.execute("show schemas")
    cs.execute("SELECT dataset_order, sepal_length FROM iris limit 10").fetchone()
    for (dataset_order, sepal_length) in cs:
        print('{0}, {1}'.format(dataset_order, sepal_length))

    print('\n DataSet_Order Sepal_Length \n')
    for (dataset_order, sepal_length) in cs.execute("select dataset_order, sepal_length FROM iris limit 10"):
        print('{0}, {1}'.format(dataset_order, sepal_length))


    print('\n new line')
    a, b = cs.execute("SELECT dataset_order, sepal_length FROM iris limit 10").fetchone()
    print('{0}, {1}'.format(a,b))    
finally:
    cs.close


conn.close()
