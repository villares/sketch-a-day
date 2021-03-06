list_a = ["A", "B", "C", "D", "F"] 
list_b = ["A", "C", "D", "E", "F"]

def setup():
    size(400, 400)
    fill(0); textFont(createFont("Inconsolata Condensed Bold", 22))
    text("1st list: " + str(list_a), 10, 30)
    text("2nd list: " + str(list_b), 10, 60)
    text("New in 2nd: " + str(new_elements(list_a, list_b)), 10, 90)
    text("Missing in 2nb: " + str(missing_elements(list_a, list_b)), 10, 120)
        
# naive
        
def new_elements(a, b):
    return [element for element in b
            if element not in a]
        
def missing_elements(a, b):
    return [element for element in a
            if element not in b]
        
# with sets - order not guaranteed

def new_elements(a, b):
    return list(set(b) - set(a))

def missing_elements(a, b):
    return list(set(a) - set(b))
