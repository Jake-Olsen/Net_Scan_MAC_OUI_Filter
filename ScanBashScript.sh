#!/bin/bash
#Look up all valid IPv4 Subnets present on router.
ip -4 r | grep -v -E 'default|nexthop|169.' | awk '{print $1}' > subnetlist.txt
#Run quick ping scan on all valid subnets
nmap -sn -n -PR -iL subnetlist.txt --max-rtt-timeout 100ms --max-retries 3 --send-eth -oN scanResults.txt
#Run though MAC OUI Filter
python PhoneMacFilter.py > phoneFilteredList.txt
echo "Script Finished. You can find the results in phoneFilteredList.txt"