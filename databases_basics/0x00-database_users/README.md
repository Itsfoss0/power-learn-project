
##  Managing Users in MySQL
- Creating Users
- Managing Users' Authentication 
- Giving Privileges to Users
- Revoking Priviledges
- Deleting Users

### Creating Users
The General syntax for creating a new users is
```sql
CREATE USER IF NOT EXISTS 'username'@'hostname' IDENTIFIED BY 'password'
```
Where:
-  __username__: is the name of the user
- __hostname__: is the hostname that the user will access the database from. In most cases, this is alway set to ```localhost``` for development environments. If the user should be allowed to access the database server from any host, the ```<hostname>``` should be set to ```'%'```
- __password__: is the password the user will use to authenticate to the server. 

### Granting privileges
After creating a user, we will to allow them to perfom certian ```actions``` on the database objects. For this we need to grant them privileges
The general syntax for granting privileges is
```sql
GRANT privilege_type ON database_object to 'user'@'host'; FLUSH PRIVILEGES
```
Where: 
- __privilege_type__: is the kind of action or actions to allow the user to perfom 
- __user__: is the username for the user
- __host__: host is the hostname

After that we have to Flush the privileges

### Showing the grants
This is how we see the actions the user is allowed to do on the server

```sql
SHOW GRANTS FOR 'user'@'hostname';
```

```
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $cat 2-grant_privs.sql  | mysql -u root -p;
Enter password: 
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $cat 3-show_grants.sql  | mysql -u root -p;
Enter password: 
Grants for plpstudent@localhost
GRANT SELECT, INSERT, CREATE, DROP ON *.* TO `plpstudent`@`localhost` IDENTIFIED BY PASSWORD '*AF8B0FA3E4FD603DDS87DSHDSUDHSJKDSJ634F62731916EC4031BFA25A'
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $
```

### Revoking grants
For one reason or the other, we might need to revoke some privileges from a user on the server. 

Revoking privileges from a user is a straightforward process that can be accomplished using the `REVOKE` command. It takes the following syntax. 

```sql
REVOKE privilege_type [, privilege_type]
ON object_type
FROM 'user'@'hostname';
```
where:
- __privilege_type__: is the privilege we want to revoke from the user
- __object_type__: is the database object we want to revoke the privilege on
- __'user'@'hostname'__: is the user

Example
```
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $cat 4-revoke_grants.sql | mysql -u root -p;
Enter password: 
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $cat 3-show_grants.sql | mysql -u root -p;
Enter password: 
Grants for plpstudent@localhost
GRANT SELECT ON *.* TO `plpstudent`@`localhost` IDENTIFIED BY PASSWORD '*AF8B0FA3E4FD603D634F62731916EC4031BFA25A'
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $
```
From the above example, after running the revoke commands, and checking for the grants again, we see that only the SELECT privilege is left.


### Deleting users
In the long run, we will eventually have to delete user(s) from the database server.
The general sytantax for the command to delete a user is 

```sql
DROP USER [IF EXISTS] 'user_name'@'host_name'
```

Before deleting any user, lets first take a run at who are the current users in the server
```
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $cat 5-show_users.sql | mysql -u root -p
Enter password: 
User
student_any
itsfoss
mariadb.sys
mysql
plpstudent
root
techie
test_user
user_0d_1
user_0d_2
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $
```
Let's delete the test_user, student_any and techie  users

```
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $cat 6-delete_users.sql  | mysql -u root -p;
Enter password: 
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $cat 5-show_users.sql | mysql -u root -p;
Enter password: 
User
itsfoss
mariadb.sys
mysql
plpstudent
root
user_0d_1
user_0d_2
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/databases_basics/0x00-database_users]
└──╼ $
```
