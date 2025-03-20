import mysql.connector

# MySQL connection settings
host = 'localhost'               
user = 'root'                    
password = 'Ravi@123'       
database = 'eu_flight_db'        

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        auth_plugin='mysql_native_password' 
    )

    print("✅ Connected to MySQL database successfully!")

    cursor = conn.cursor()

    # Retrieve all flight records
    cursor.execute("SELECT * FROM Flights")
    flights = cursor.fetchall()

    print("\nFlight Data:")
    for flight in flights:
        print(flight)

    # Close connection
    cursor.close()
    conn.close()
    print("\n✅ MySQL connection closed!")

except Exception as e:
    print(f"❌ Error: {e}")
