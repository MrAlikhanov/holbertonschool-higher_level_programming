-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 has only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password is set to user_0d_2_pwd

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the specific database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Ensure changes are applied
FLUSH PRIVILEGES;
