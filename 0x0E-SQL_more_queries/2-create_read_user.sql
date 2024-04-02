-- create a database called hbtn_0d_2 with user user_0d_2
-- user should have SELECT privilege on database, have a set password
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' 
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLASH PRIVILEGES;
