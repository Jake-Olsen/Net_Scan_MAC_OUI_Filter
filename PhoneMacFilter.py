#!/usr/bin/python
# Script for Filtering results from an NMAP scan for specific devices and merging each result onto a single line
#
File1 = open('scanResults.txt', 'r')
ScanList = File1.readlines()
File1.close()
#
Polycom_MAC_OUI_1 = "MAC Address: 64:16:7F:"
Polycom_MAC_OUI_2 = "MAC Address: 00:04:F2:"
#
Yealink_MAC_OUI_1="00:15:65:"
Yealink_MAC_OUI_2="80:5E:C0:"
#
Cisco8841_MAC_OUI_01="4A:BC:48:"
Cisco8841_MAC_OUI_02="54:86:BC:"
Cisco8841_MAC_OUI_03="A4:B2:39:"
Cisco8841_MAC_OUI_04="CC:70:ED:"
Cisco8841_MAC_OUI_05="70:C9:C6:"
Cisco8841_MAC_OUI_06="AC:BC:48:"
Cisco8841_MAC_OUI_07="D0:EC:35:"
Cisco8841_MAC_OUI_08="4C:BC:48:"
Cisco8841_MAC_OUI_09="4C:BC:48:"
Cisco8841_MAC_OUI_10="70:01:B5:"
Cisco8841_MAC_OUI_11="A4:4C:11:"
#
Cisco122_MAC_OUI_01="00:27:90:"
Cisco122_MAC_OUI_02="00:A2:89:"
Cisco122_MAC_OUI_03="00:DA:55:"
Cisco122_MAC_OUI_04="34:F8:E7:"
Cisco122_MAC_OUI_05="50:06:AB:"
Cisco122_MAC_OUI_06="70:1F:53:"
Cisco122_MAC_OUI_07="88:75:56:"
Cisco122_MAC_OUI_08="88:90:8D:"
Cisco122_MAC_OUI_09="AC:F2:C5:"
Cisco122_MAC_OUI_10="CC:5A:53:"
Cisco122_MAC_OUI_11="CC:D5:39:"
Cisco122_MAC_OUI_12="CC:EF:48:"
Cisco122_MAC_OUI_13="E0:2F:6D:"
#
counter = 0
while counter < len(ScanList):
    if (Polycom_MAC_OUI_1 in ScanList[counter]) \
            or (Polycom_MAC_OUI_2 in ScanList[counter]) \
            or (Yealink_MAC_OUI_1 in ScanList[counter]) \
            or (Yealink_MAC_OUI_2 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_01 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_02 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_03 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_04 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_05 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_06 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_07 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_08 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_09 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_10 in ScanList[counter]) \
            or (Cisco8841_MAC_OUI_11 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_01 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_02 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_03 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_04 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_05 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_06 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_07 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_08 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_09 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_10 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_11 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_12 in ScanList[counter]) \
            or (Cisco122_MAC_OUI_13 in ScanList[counter]) \
            :
        CombinedString = (str(ScanList[counter].rstrip('\n')) + " " + str(ScanList[counter - 1].rstrip('\n')))
        print(CombinedString)
    counter += 1
# end of while
print("Filtering Complete")