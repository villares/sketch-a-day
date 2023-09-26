import sys, subprocess

def run(path):
    subprocess.Popen(
        ['python', path],
#         stdin=None,
#         stdout=None,
#         stderr=None,
    )

print('starting...')
run('sketch_1.py')
print('2nd sketch...')
run('sketch_2.py')
print('done.')

"""
>>> # Clean up from within the second Python shell
>>> existing_smd.shm.close()  # or "del existing_smd"

>>> # Clean up from within the first Python shell
>>> smd.shm.close()
>>> smd.shm.unlink()  # Free and release the shared memory block at the very end
>>> del smd  # use of smd after call unlink() is unsupported
"""