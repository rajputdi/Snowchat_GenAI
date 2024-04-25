USE ROLE ACCOUNTADMIN;
USE WAREHOUSE HOL_WH;
USE DATABASE HOL_DB;
USE SCHEMA PUBLIC;

ALTER WAREHOUSE HOL_WH SET WAREHOUSE_SIZE = XLARGE WAIT_FOR_COMPLETION = TRUE;

CREATE OR REPLACE VIEW AirportFlights AS
    SELECT 
        ARRIVAL_IATA_AIRPORT_CODE AS AirportCode,
        COUNT(*) AS ArrivalFlightCount,
        0 AS DepartureFlightCount
    FROM 
        HOL_DB.PUBLIC.FLIGHT_STATUS_DATA_CLEANING
    GROUP BY 
        ARRIVAL_IATA_AIRPORT_CODE

    UNION ALL
    
    SELECT 
        DEPARTURE_IATA_AIRPORT_CODE AS AirportCode,
        0 AS ArrivalFlightCount,
        COUNT(*) AS DepartureFlightCount
    FROM 
        HOL_DB.PUBLIC.FLIGHT_STATUS_DATA_CLEANING
    GROUP BY 
        DEPARTURE_IATA_AIRPORT_CODE;
        
CREATE OR REPLACE VIEW RankedAirports AS
    SELECT 
        AirportCode,
        SUM(ArrivalFlightCount) AS ArrivalFlightCount,
        SUM(DepartureFlightCount) AS DepartureFlightCount
    FROM 
        AirportFlights
    GROUP BY
        AirportCode;
            
SELECT 
    AirportCode AS "Airport Code",
    ArrivalFlightCount AS "Number of Incoming Flights",
    DepartureFlightCount AS "Number of Outgoing Flights"
FROM 
    RankedAirports;

ALTER WAREHOUSE HOL_WH SET WAREHOUSE_SIZE = XSMALL;