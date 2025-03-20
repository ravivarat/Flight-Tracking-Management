import mysql.connector

# MySQL connection settings
host = 'localhost'               # MySQL server
user = 'root'                    # Your MySQL username
password = 'Ravi@123'        # Your MySQL password
database = 'eu_flight_db'         # Your database name

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        auth_plugin='mysql_native_password'  # Use this here
    )

    print("✅ Connected to MySQL database successfully!")

    cursor = conn.cursor()

    # Retrieve all flight records
    cursor.execute("SELECT * FROM Flights")
    flights = cursor.fetchall()

    print("\nFlight Data:")
    for flight in flights:
        print(flight)

    # Close the connection
    cursor.close()
    conn.close()
    print("\n✅ MySQL connection closed!")

except Exception as e:
    print(f"❌ Error: {e}")
