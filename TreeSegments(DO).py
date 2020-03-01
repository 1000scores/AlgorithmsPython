''' Дерево отрезков с максимумом на отрезке '''
def update(curV, leftBound, rightBound, ind, value):
    if ind < leftBound or ind > rightBound:
        return
    if ind == leftBound and ind == rightBound:
        tree[curV] = (value, ind)
        return

    mid = (leftBound + rightBound) // 2
    update(curV*2, leftBound, mid, ind, value)
    update(curV*2 + 1, mid+1, rightBound, ind, value)

    tree[curV] = max(tree[2 * curV], tree[2 * curV + 1])

def getMax(curV, leftBound, rightBound, leftX, rightX):
    if rightBound < leftX or leftBound > rightX:
        return (0, 0)

    if leftBound >= leftX and rightBound <= rightX:
        return tree[curV]

    mid = (leftBound + rightBound) // 2

    mx = max(getMax(curV * 2, leftBound, mid, leftX, rightX), getMax(curV * 2 + 1, mid + 1, rightBound, leftX, rightX))

    return mx


n = int(input())



tree = [(0, 0)]*4*n

ar = [int(i) for i in input().split(' ')]

for ind, value in enumerate(ar):
    #print(ind, value, sep = ' ')
    update(1, 0, n-1, ind, value)

q = int(input())
for i in range(q):
    inp = input().split(' ')

    left = int(inp[0]) - 1
    right = int(inp[1]) - 1
    ans = getMax(1, 0, n-1, left, right)
    print(ans[0], ans[1] + 1, sep = ' ')


