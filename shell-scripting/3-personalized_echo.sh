#!//usr/bin/env bash
#read name from stdin and
#print "Hello <name>" to stdout

echo -n "Hi, How can I call you? ";
read -r name;
echo "Hello $name";
