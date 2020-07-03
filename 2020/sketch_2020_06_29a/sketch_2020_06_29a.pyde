
def setup():
    a, b = 31, 20
    c = a ^ b
    for n in(a, b, c):
        print(str(n) + ': ' + left_padded_bin(n, 8))

def left_padded_bin(v, n):
    f = '{{:0{}b}}'.format(n)
    return f.format(v)
