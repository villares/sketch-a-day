#!/home/villares/thonny-env/bin/python
import os
import sys

def please():
    print('you are welcome')
                
for arg in sys.argv[1:]:
    if arg.startswith('p'):
        please()
    else:
        print("""villares arguments:
    p   run please()
        'you are welcome'
""")
        exit()


