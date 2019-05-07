#!/usr/bin/env python
from sqlalchemy import create_engine
#'snowflake://<user_login_name>:<password>@<account_name>/<database_name>/<schema_name>?warehouse=<warehouse_name>?role=<role_name>'
# Get the version
engine = create_engine ( 'snowflake://{user}:{password}@{account}/'.format(
    user = 'viveksharma30'
    ,password = 'ShwetaSaraswat!234'
    ,account = 'kx62732.east-us-2.azure'
    )
)


try:
    connection = engine.connect()
    results = connection.execute('select current_version()').fetchone()
    print(results[0])


finally:
    connection.close()
    engine.dispose()
