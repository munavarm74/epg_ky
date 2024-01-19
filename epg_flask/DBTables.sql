
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    preferred_timezone VARCHAR(50) NOT NULL
);

CREATE TABLE channels (
    channel_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE programs (
    program_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    genre VARCHAR(50) NOT NULL,
    channel_id INT,
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id)
);

CREATE TABLE schedules (
    schedule_id INT PRIMARY KEY,
    channel_id INT UNIQUE NOT NULL,
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id)
);

CREATE TABLE scheduled_programs (
    schedule_id INT,
    program_id INT,
    PRIMARY KEY (schedule_id, program_id),
    FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id),
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);





