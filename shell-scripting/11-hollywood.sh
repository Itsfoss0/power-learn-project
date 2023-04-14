#!/usr/bin/env bash
#Lets get pranky
python -m pyfiglet Itsfoss 
echo "[*]STARTING THE ATTACK.........." | pv -qL 26
echo "[*]Acessing the Database......" | pv -qL 10
echo "********************************" | pv -qL 40
echo
echo "Running Recon.................." | pv -qL 10
echo -e "Found something\t....Looking now" | pv -qL 10
for file in $(ls); do
    echo "Found $file" | pv -qL 20
    if [[ $file == 5-* ]]; then
	echo "$(cat $file)" | pv -qL 36
    fi
done
clear

echo "[+] Assets Compromised.....clearing logfiles now" | pv -qL 15
