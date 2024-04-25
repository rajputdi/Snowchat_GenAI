import snowflake.connector
import sys
import configparser

# Read Snowflake config from file
config = configparser.ConfigParser()
config.read(sys.argv[1] + '/config')  # Change 'config' to the path of your config file

# Connection parameters
account = config.get('connections.dev', 'accountname')
user = config.get('connections.dev', 'username')
password = config.get('connections.dev', 'password')
warehouse = config.get('connections.dev', 'warehousename')
database = config.get('connections.dev', 'dbname')
schema = 'PUBLIC'

# Establish a connection
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)
# Create a cursor object
cursor = conn.cursor()

# Read SQL script from file
with open(sys.argv[2], 'r') as file:
    sql_script = file.read()

# Split the script into individual statements
statements = sql_script.split(';')

# Execute each statement
for statement in statements:
    try:
        cursor.execute(statement)
    except snowflake.connector.errors.ProgrammingError as e:
        print(f"Error executing statement: {statement}")
        print(f"Error details: {e}")

# Commit changes
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()
