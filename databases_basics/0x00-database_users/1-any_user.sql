-- create a user 'student_any' to access mysql database from any host

CREATE USER IF NOT EXISTS 'student_any'@'%' IDENTIFIED BY 'student123';