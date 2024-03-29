DROP TABLE bookings;
DROP TABLE members;
DROP TABLE sessions;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    active_member BOOLEAN
);


CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    session_name VARCHAR(255),
    time VARCHAR(255),
    max_capacity INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE
);
