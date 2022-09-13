on_time_table_drop = "DROP TABLE IF EXISTS on_time;"
carriers_table_drop = "DROP TABLE IF EXISTS carriers;"
planes_table_drop = "DROP TABLE IF EXISTS planes;"
airports_table_drop = "DROP TABLE IF EXISTS airports;"

# TABLE CREATE QUERIES
on_time_table_create = """
    CREATE TABLE IF NOT EXISTS on_time (
        year SMALLINT,
        month SMALLINT,
        day SMALLINT,
        day_of_week SMALLINT,
        departure_time INT,
        crs_departure_time INT,
        arrival_time INT,
        crs_arrival_time INT,
        unique_carrier VARCHAR,
        flight_number SMALLINT,
        tail_number VARCHAR(6),
        actual_elapsed_time REAL,
        crs_elapsed_time REAL,
        air_time REAL,
        arrival_delay REAL,
        departure_delay REAL,
        origin CHAR(3),
        destination CHAR(3),
        distance REAL,
        taxi_in REAL,
        taxi_out REAL,
        cancelled BOOLEAN,
        cancellation_code CHAR(1),
        diverted BOOLEAN,
        carrier_delay REAL,
        wheather_delay REAL,
        nas_delay REAL,
        security_delay REAL,
        late_aircraft_delay REAL,
        PRIMARY KEY(year, month, day, departure_time, tail_number)
    );
"""

carriers_table_create = """
    CREATE TABLE IF NOT EXISTS carriers (
        code VARCHAR PRIMARY KEY,
        description VARCHAR
    );
"""

planes_table_create = """
    CREATE TABLE IF NOT EXISTS planes (
        tail_number VARCHAR(6) PRIMARY KEY,
        type VARCHAR,
        manufacturer VARCHAR,
        issue_date TEXT,
        model VARCHAR,
        status VARCHAR,
        aircraft_type VARCHAR,
        engine_type VARCHAR,
        year SMALLINT
    );
"""

airports_table_create = """
    CREATE TABLE IF NOT EXISTS airports (
        iata CHAR(3) PRIMARY KEY,
        name VARCHAR NOT NULL,
        city VARCHAR,
        state CHAR(2),
        country VARCHAR,
        lat NUMERIC(8,6),
        lon NUMERIC(9,6)
    );
"""

# TABLE INSERT QUERIES
on_time_table_insert = """
    INSERT INTO on_time (
        year,
        month,
        day,
        day_of_week,
        departure_time,
        crs_departure_time,
        arrival_time,
        crs_arrival_time,
        unique_carrier,
        flight_number,
        tail_number,
        actual_elapsed_time,
        crs_elapsed_time,
        air_time,
        arrival_delay,
        departure_delay,
        origin,
        destination,
        distance,
        taxi_in,
        taxi_out,
        cancelled,
        cancellation_code,
        diverted,
        carrier_delay,
        wheather_delay,
        nas_delay,
        security_delay,
        late_aircraft_delay
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT (year, month, day, departure_time, tail_number)
    DO UPDATE
    SET
        departure_time = EXCLUDED.departure_time,
        arrival_time = EXCLUDED.arrival_time,
        actual_elapsed_time = EXCLUDED.actual_elapsed_time,
        air_time = EXCLUDED.air_time,
        arrival_delay = EXCLUDED.arrival_delay,
        departure_delay = EXCLUDED.departure_delay,
        cancelled = EXCLUDED.cancelled,
        cancellation_code = EXCLUDED.cancellation_code,
        diverted = EXCLUDED.diverted,
        carrier_delay = EXCLUDED.carrier_delay,
        wheather_delay = EXCLUDED.wheather_delay,
        nas_delay = EXCLUDED.nas_delay,
        security_delay = EXCLUDED.security_delay,
        late_aircraft_delay = EXCLUDED.late_aircraft_delay; 
"""

planes_table_insert = """
    INSERT INTO planes (
        tail_number,
        type,
        manufacturer,
        issue_date,
        model,
        status,
        aircraft_type,
        engine_type,
        year
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT (tail_number)
    DO UPDATE
    SET
        type = EXCLUDED.type,
        manufacturer = EXCLUDED.manufacturer,
        issue_date = EXCLUDED.issue_date,
        model = EXCLUDED.model,
        status = EXCLUDED.status,
        aircraft_type = EXCLUDED.aircraft_type,
        engine_type = EXCLUDED.engine_type,
        year = EXCLUDED.year;
"""

carriers_table_insert = """
    INSERT INTO carriers (
        code,
        description
    ) VALUES (?, ?)
    ON CONFLICT (code)
    DO UPDATE
    SET
        description = EXCLUDED.description;
"""

airports_table_insert = """
    INSERT INTO airports (
        iata,
        name,
        city,
        state,
        country,
        lat,
        lon
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT (iata)
    DO UPDATE
    SET
        name = EXCLUDED.name,
        city = EXCLUDED.city,
        state = EXCLUDED.state,
        country = EXCLUDED.country,
        lat = EXCLUDED.lat,
        lon = EXCLUDED.lon;
"""

drop_table_queries = [planes_table_drop, carriers_table_drop, airports_table_drop, on_time_table_drop]
create_table_queries = [planes_table_create, carriers_table_create, airports_table_create, on_time_table_create]