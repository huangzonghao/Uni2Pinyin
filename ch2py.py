#! /usr/bin/python3

import os, sys, re

with open('uni2pinyin.txt') as f:
    u2p_table = f.read()

def unicode2pinyin(dir_name):
    os.chdir(dir_name)
    filenames = os.listdir(u'.')
    for filename in filenames:
        if os.path.isdir(filename):
            unicode2pinyin(filename)
        filename_tmp = ''
        for x in filename:
            if 0x4e00 <= ord(x) <= 0x9fff: # Chinese Character Unicode range
                hexCH = (hex(ord(x))[2:]).upper() # strip leading '0x' and change to uppercase
                p = re.compile(hexCH+'\t([a-z]+)[\d]*') # define the match pattern
                mp = p.search(u2p_table)
                filename_tmp += mp.group(1).title()
            else:
                filename_tmp += x
        os.rename(filename, filename_tmp)
    os.chdir('..')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: {} path/to/dir1 path/to/dir2 ...\n\t".format(sys.argv[0]),
                "dir1, dir2, ... will be renamed as well")

    for dirname in sys.argv[1:]:
        if os.path.isdir(dirname):
            unicode2pinyin(dirname)
        else:
            print(dirname + 'is not a directory, skipping')
