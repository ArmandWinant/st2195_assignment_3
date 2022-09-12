on_time_table_drop = "DROP TABLE IF EXISTS on_time;"
carriers_table_drop = "DROP TABLE IF EXISTS carriers;"
planes_table_drop = "DROP TABLE IF EXISTS planes;"
airports_table_drop = "DROP TABLE IF EXISTS airports;"

on_time_table_create = """
    CREATE TABLE IF NOTE EXISTS on_time (
        year SMALLINT NOT NULL,
        month SMALLINT NOT NULL,
        day_of_month SMALLINT NOT NULL,
        day_of_week SMALLINT NOT NULL,
        departure_time NOT NULL,
        crs_departure_time NOT NULL,
        arrival_time NOT NULL,
        crs_arrival_time NOT NULL,
        unique_carrier TEXT NOT NULL,
        flight_number SMALLINT NOT NULL,
        tail_number NOT NULL,
        elapsed_time NOT NULL,
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

drop_table_queries = [planes_table_drop, carriers_table_drop, airports_table_drop]
create_table_queries = [planes_table_create, carriers_table_create, airports_table_create]