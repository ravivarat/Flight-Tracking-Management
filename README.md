# Flight-Tracking-Management


# ✈️ Real-Time Flight Tracker Project
A real-time flight tracking system using **Python, MySQL**, and the **AviationStack API**. This project fetches live flight data and stores it in a MySQL database, allowing you to query and analyze the flights.

![Description](./Img/1.jpeg)

---



## 🚀 **Features**
✅ Fetches real-time flight data from the AviationStack API  
✅ Stores data in MySQL tables with **Airports, Airlines, Flights, and FlightStatus**  
✅ Identifies delayed flights with real-time statuses  
✅ Easy querying of flight details, delays, and airport information  

---

## ⚙️ **Technologies Used**
- **Python** (pymysql, requests)  
- **MySQL** (for database storage)  
- **AviationStack API** (real-time flight data)  

---

## 💡 **Database Schema**
### 1. **Airports Table**
- `airport_id`: INT (Primary Key)  
- `name`: VARCHAR  
- `iata_code`: VARCHAR  
- `icao_code`: VARCHAR  
- `country`: VARCHAR  
- `city`: VARCHAR  
- `latitude`: FLOAT  
- `longitude`: FLOAT  

### 2. **Airlines Table**
- `airline_id`: INT (Primary Key)  
- `name`: VARCHAR  
- `iata_code`: VARCHAR  
- `icao_code`: VARCHAR  
- `country`: VARCHAR  

### 3. **Flights Table**
- `flight_id`: INT (Primary Key)  
- `airport_id`: INT (Foreign Key)  
- `airline_id`: INT (Foreign Key)  
- `flight_number`: VARCHAR  
- `departure_time`: DATETIME  
- `arrival_time`: DATETIME  
- `status`: VARCHAR  

### 4. **FlightStatus Table**
- `status_id`: INT (Primary Key)  
- `flight_id`: INT (Foreign Key)  
- `delay`: INT  
- `status_description`: VARCHAR  

---

## 🔥 **API Integration**
This project uses the [AviationStack API](https://aviationstack.com/) to fetch live flight data.  
To get the data:
1. Sign up at AviationStack and get your free API key.
2. Replace the API key in the Python script:
```python
API_KEY = "YOUR_API_KEY_HERE"
