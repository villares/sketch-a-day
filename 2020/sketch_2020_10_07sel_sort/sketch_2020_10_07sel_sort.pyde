def setup():
    size(512, 512)
    randomize()

def randomize():
    global nums, i
    nums = [int(random(32)) for _ in range(512)]
    i = 0
    
def draw():
    global i
    background(200, 0, 0)
    for x, n in enumerate(nums):
        stroke(n * 8)
        line(x, height - n * 16, x, height)
        
    tam = len(nums)
    if i < tam-1:
        m = i
        for j in range(i + 1, tam):
            if nums[j] < nums[m]:
                m = j
        if nums[i] != nums[m]:
            nums[i], nums[m] = nums[m], nums[i]
        i += 1

def selection_sort(nums):
    # int i, j, m, aux;
    tam = len(nums)
    for i in range(tam - 1):
        m = i
        for j in range(i + 1, tam):
            if nums[j] < nums[m]:
                m = j
        if nums[i] != nums[m]:
            nums[i], nums[m] = nums[m], nums[i]

def keyPressed():
    randomize()
