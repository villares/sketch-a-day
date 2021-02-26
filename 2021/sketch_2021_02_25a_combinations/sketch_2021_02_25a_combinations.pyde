from itertools import permutations, combinations, product
colorMode(HSB)
noStroke()
grid = product((-1, 0.5, 2), repeat=3)
combs = (p for p in combinations(grid, 3)
              if p[0][0] != p[1][0] != p[2][0] and
                 p[0][1] != p[1][1] != p[2][1] and
              p[0][2] != p[1][2] != p[2][2]
              )     
comb_l = list(combs)
for c in comb_l:
    print(c)
print('----')
print(len(comb_l))
size(400, 400, P3D)
translate(150, 150, -150)
scale(100)
background(0)
lights()
for i, (a, b, c) in enumerate(comb_l):
    fill(i * 1.6, 255, 255, 64)
    beginShape()
    vertex(*a)
    vertex(*b)
    vertex(*c)
    endShape(CLOSE)
 

 
# things = ("A", "B", "C",
#           "D", "E", "F",
#           "G", "H", "I",)
# p = permutations(things, 3)
