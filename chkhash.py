#!/bin/python3
import os, hashlib, sys
rootdir = '/'
ignoredirs = [
'CyberPatriots',
'home',
'proc',
'sys',
'tmp',
'run',
'dev',
'root',
'mnt'
]

hashlist = dict()
with open("hashes.txt", 'r') as f:
    for line in f:
        temp = line.split("||")
        hashlist[temp[0]] = temp[1]

filelist = list(map(str.strip, list(hashlist.keys())))
fileamount = len(filelist)
scanned = 0
print('hashlist and filelist compiled')

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filename = os.path.join(subdir, file)
        dirnames = filename.split('/')
        if dirnames[1] not in ignoredirs:
            if filename.strip() not in filelist:
                print(f'NEW FILE: {filename}')
                continue

            if (hashlib.md5(open(filename, 'rb').read()).hexdigest().strip() != hashlist[filename].strip()):
                print(f"MODIFIED FILE: {filename}")

            scanned += 1
            sys.stdout.write(f"{scanned}/{fileamount} {scanned/fileamount * 100:.2f}% \r")
            sys.stdout.flush()
print('hashes checked')
