lijsteke = [int(_) for _ in input()]
goed_lijsteke = lijsteke[::-1]
result = ""
x = 0
while x < len(goed_lijsteke):
    result += str(goed_lijsteke[x])
    x += 1
print(result)

