-- Dummy Data for Users
INSERT INTO users (user_id, username, password_hash, role, preferred_timezone)
VALUES
    (1, 'admin', 'admin_password_hash', 'admin', 'UTC'),
    (2, 'user1', 'user1_password_hash', 'user', 'GMT'),
    (3, 'user2', 'user2_password_hash', 'user', 'CET');

-- Dummy Data for Channels
INSERT INTO channels (channel_id, name, description)
VALUES
    (1, 'Channel 1', 'Description of Channel 1'),
    (2, 'Channel 2', 'Description of Channel 2'),
    (3, 'Channel 3', 'Description of Channel 3');

-- Dummy Data for Programs
INSERT INTO programs (program_id, title, description, start_time, end_time, genre, channel_id)
VALUES
    (1, 'Program 1', 'Description of Program 1', '2024-01-12 08:00', '2024-01-12 10:00', 'Drama', 1),
    (2, 'Program 2', 'Description of Program 2', '2024-01-12 10:30', '2024-01-12 12:30', 'Comedy', 2),
    (3, 'Program 3', 'Description of Program 3', '2024-01-12 14:00', '2024-01-12 16:00', 'Action', 3);

-- Dummy Data for Schedules
INSERT INTO schedules (schedule_id, channel_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3);

-- Dummy Data for Scheduled Programs (Associations)
INSERT INTO scheduled_programs (schedule_id, program_id)
VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3);
