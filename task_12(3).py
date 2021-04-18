def foo():
    with open("123.txt", "r") as f:
        for line in f:
            yield line.strip()


for line in foo():
    print(line)
