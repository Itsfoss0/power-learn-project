-- Revoke some privileges from 'plpstudent'@'localhost'

REVOKE DROP, CREATE, INSERT ON *.* FROM 'plpstudent'@'localhost';