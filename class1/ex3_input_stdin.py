#!/usr/bin/env python
'''
3. In the test3.py (from class email week1), how would you modify the script to
remove the trailing newline on the end of 192.168.1.1?

>>>>> CODE (file test3.py) <<<<<
#!/usr/bin/env python

import fileinput

for line in fileinput.input():
    print line.split(".")
>>>>> END <<<<<
'''

import fileinput

for line in fileinput.input():
    line = line.strip()
    print line.split(".")
 
