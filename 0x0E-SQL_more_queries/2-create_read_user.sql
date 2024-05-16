-- create database hbtn_0d_2
-- create the MySQL server user 'user_0d_2'
-- grant only SELECT privilege
CREATE USER
'user_0d_2'@'localhost'
IDENTIFIED BY
'user_0d_2_pwd';

GRANT SELECT
ON hbtn_0d_2
TO 'user_0d_1'@'localhost';

