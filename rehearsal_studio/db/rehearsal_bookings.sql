DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS studios;



CREATE TABLE studios (
    id SERIAL PRIMARY KEY,
    studio_number INT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name_user VARCHAR (255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id),
    studio INT NOT NULL REFERENCES studios(id),
    booking_date DATE,
    booking_time VARCHAR(255),
    attendees INT
);