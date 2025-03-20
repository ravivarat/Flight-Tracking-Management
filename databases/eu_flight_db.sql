CREATE DATABASE eu_flight_db;
USE eu_flight_db;



CREATE TABLE Airports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    iata_code VARCHAR(10),
    icao_code VARCHAR(10),
    country VARCHAR(50),
    city VARCHAR(50),
    latitude FLOAT,
    longitude FLOAT
);



CREATE TABLE Flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    airport_id INT,
    flight_number VARCHAR(10),
    airline VARCHAR(50),
    departure_time DATETIME,
    arrival_time DATETIME,
    status VARCHAR(20),
    FOREIGN KEY (airport_id) REFERENCES Airports(id)
);




INSERT INTO Airports (name, iata_code, icao_code, country, city, latitude, longitude) VALUES
('Frankfurt Airport', 'FRA', 'EDDF', 'Germany', 'Frankfurt', 50.0379, 8.5622),
('Berlin Brandenburg Airport', 'BER', 'EDDB', 'Germany', 'Berlin', 52.3667, 13.5033),
('Munich Airport', 'MUC', 'EDDM', 'Germany', 'Munich', 48.3538, 11.7861),
('Hamburg Airport', 'HAM', 'EDDH', 'Germany', 'Hamburg', 53.6304, 9.9882),
('Düsseldorf Airport', 'DUS', 'EDDL', 'Germany', 'Düsseldorf', 51.2895, 6.7668);



INSERT INTO Flights (airport_id, flight_number, airline, departure_time, arrival_time, status) VALUES
(1, 'LH123', 'Lufthansa', '2025-03-20 10:00:00', '2025-03-20 12:30:00', 'on-time'),
(2, 'AF456', 'Air France', '2025-03-20 11:00:00', '2025-03-20 14:30:00', 'delayed'),
(3, 'BA789', 'British Airways', '2025-03-20 09:30:00', '2025-03-20 11:00:00', 'on-time'),
(4, 'EW101', 'Eurowings', '2025-03-20 12:00:00', '2025-03-20 14:45:00', 'delayed'),
(5, 'LH202', 'Lufthansa', '2025-03-20 08:00:00', '2025-03-20 10:30:00', 'on-time');





SELECT * FROM Airports;
SELECT * FROM Flights;


