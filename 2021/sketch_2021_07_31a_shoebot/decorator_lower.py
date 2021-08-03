



def lower_case(func):
    def decorated(*args):
        return func(*args).lower()
    return decorated

@lower_case
def greeter(name):
    return 'Olá ' + name + '!'

print(greeter('Alexandre'))