#!/bin/python
import os, hashlib
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

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filename = os.path.join(subdir, file)
        if filename.split('/')[1] not in ignoredirs:
            try:
                hashlist[filename] = hashlib.md5(open(filename, 'rb').read()).hexdigest()
            except:
                print(f"WARNING: Hash for {filename} not generated. (Broken symlink?)")

print('hashlist compiled')

with open('hashes.txt', 'w') as hf:
    for i in list(hashlist.keys()):
        hf.write(f"{i}||{hashlist[i]}\n")



