Uni2Pinyin
====

Convert UTF Chinese Characters in directory names or file names to Pinyin without tones.

## Usage
    git clone https://github.com/huangzonghao/Uni2Pinyin.git
    cd Uni2Pinyin
    ./ch2py.py path/to/dir1 path/to/dir2 ...
        # dir1, dir2, ... will be converted as well
## Dependency
Python 3

## Initiative
This tool is meant to solve for situations where only ASCII code is displayable
due to system limitations. For me it is a vehicle's Read-from-USB function being
only able to display music file name in ASCII code. Can't believe it's a vehicle
from 2018.

## Limitation
The tool only looks up the Pinyin character by character, disregarding semantics
and [gramma of Pinyin](http://www.moe.gov.cn/ewebeditor/uploadfile/2015/01/13/20150113091717604.pdf).
So in no way it could handle homophones or words. Be prepared to see some weird
combinations in the converted file names.

## License
MIT
