#!/usr/bin/python
import re
import sys
contacts = []

file = open(sys.argv[1], mode = 'r', encoding = 'utf8')
entire_file = file.read()

file.close()

lines = entire_file.splitlines()


for line in lines:
    match = re.findall('- (.*):', line)
    if (match):
        contacts.append(match[0])
    

distinct_contacts = list(dict.fromkeys(contacts))
new_dis_cont = []
for ph in distinct_contacts:
    if (not (re.findall(':', ph))):
        new_dis_cont.append(ph)

new_contacts = []
for ph in contacts:
    if (not (re.findall(':', ph))):
        new_contacts.append(ph)


for i in new_dis_cont:
    print(i + " has message count of: " +  str(new_contacts.count(i)))