#! /usr/bin/python3
import os
import sys

def please():
    pass
                
for arg in sys.argv[1:]:
    if arg.startswith('p'):
        please()
    else:
        print("""usage:
        p        : run please()
        """)
        exit()


