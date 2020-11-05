i = 10
while i <= 99:
    s = int((i % 10) + (i / 10))
    if i == s + s * s:
        print("Это число:", i)
    i += 1
