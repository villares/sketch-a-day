
nums = [random(512) for _ in range(512)]
i = 0

def setup():
    size(512, 512)
    colorMode(HSB)

def draw():
    background(200)
    global i
    for x, n in enumerate(nums):
        stroke(n / 2, 255, 255)
        line(x, n, x, height)
    tam = len(nums)
    if i < width - 1:
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
