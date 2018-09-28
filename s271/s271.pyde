size(200, 101)
colorMode(HSB)
noStroke()

y = 0
for i in range(8):
    fill(i * 32, 255, 255)
    rect(i * 20, y, 20, 20)

y += 20
for i in range(5):
    fill(i * 42.5, 255, 255)
    rect(i * 20, y, 20, 20)

y += 20
for i in range(5):
    fill(i * 48, 255, 255)
    rect(i * 20, y, 20, 20)

y += 20
for i in range(5):
    fill(i * 51, 255, 255)
    rect(i * 20, y, 20, 20)

y += 20            
for i in range(4):
    fill(i * 64, 255, 255)
    rect(i * 20, y, 20, 20)
