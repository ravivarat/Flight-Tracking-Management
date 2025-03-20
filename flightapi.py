import pymysql
import requests

# ✅ Database Connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Ravi@123',
    database='eu_flight_db'
)
cursor = connection.cursor()

# ✅ API Endpoint
API_KEY = "a4a980c5c89e4b7f3faaa0b7367aa7c0"
URL = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}"

# ✅ Fetch Real-Time Data
response = requests.get(URL)
flights_data = response.json().get('data', [])

# ✅ Take only the first 50 flights
flights_data = flights_data[:50]

if not flights_data:
    print("❌ No data fetched from API.")
    exit()

# ✅ Insert Real-Time Data into Tables
for flight in flights_data:
    try:
        # ✅ Extract and handle missing fields gracefully
        departure = flight.get('departure', {})
        arrival = flight.get('arrival', {})
        airline = flight.get('airline', {})
        flight_info = flight.get('flight', {})

        airport_name = departure.get('airport', 'Unknown Airport')
        iata_code = departure.get('iata', 'N/A')
        icao_code = departure.get('icao', 'N/A')
        country = departure.get('country', 'Unknown')
        city = departure.get('city', 'Unknown')

        latitude = float(departure.get('latitude', 0) or 0)
        longitude = float(departure.get('longitude', 0) or 0)

        airline_name = airline.get('name', 'Unknown Airline')
        airline_iata = airline.get('iata', 'N/A')
        airline_icao = airline.get('icao', 'N/A')
        airline_country = airline.get('country', 'Unknown')

        flight_number = flight_info.get('iata', 'N/A')
        departure_time = departure.get('estimated', None)
        arrival_time = arrival.get('estimated', None)
        status = flight.get('flight_status', 'Unknown')

        delay = int(arrival.get('delay', 0) or 0)

        # ✅ Insert Airport Data (if not exists)
        cursor.execute("""
        INSERT IGNORE INTO Airports (name, iata_code, icao_code, country, city, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (airport_name, iata_code, icao_code, country, city, latitude, longitude))
        connection.commit()

        # ✅ Get Airport ID
        cursor.execute("SELECT airport_id FROM Airports WHERE iata_code = %s", (iata_code,))
        airport_id = cursor.fetchone()
        if airport_id:
            airport_id = airport_id[0]

        # ✅ Insert Airline Data (if not exists)
        cursor.execute("""
        INSERT IGNORE INTO Airlines (name, iata_code, icao_code, country)
        VALUES (%s, %s, %s, %s)
        """, (airline_name, airline_iata, airline_icao, airline_country))
        connection.commit()

        # ✅ Get Airline ID
        cursor.execute("SELECT airline_id FROM Airlines WHERE iata_code = %s", (airline_iata,))
        airline_id = cursor.fetchone()
        if airline_id:
            airline_id = airline_id[0]

        # ✅ Insert Flight Data
        if airport_id and airline_id:
            cursor.execute("""
            INSERT INTO Flights (airport_id, airline_id, flight_number, departure_time, arrival_time, status)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (airport_id, airline_id, flight_number, departure_time, arrival_time, status))
            connection.commit()

            # ✅ Get Flight ID
            flight_id = cursor.lastrowid

            # ✅ Insert Flight Status
            cursor.execute("""
            INSERT INTO FlightStatus (flight_id, delay, status_description)
            VALUES (%s, %s, %s)
            """, (flight_id, delay, f"Real-time status: {status}"))
            connection.commit()

            print(f"✅ Inserted flight {flight_number} successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")
        connection.rollback()

# ✅ Close Connection
cursor.close()
connection.close()

print("\n✅ Successfully inserted 50 real-time flights from API!")
