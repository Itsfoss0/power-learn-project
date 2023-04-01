-- lets give our user 'plpstudent'@'localhost'  privileges
GRANT SELECT, DROP, CREATE, INSERT ON *.* TO 'plpstudent'@'localhost'; FLUSH PRIVILEGES;