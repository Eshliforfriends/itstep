with open('lines.txt', 'r') as f:
    counter = 0
    lines = f.read()
    for line in lines:
        line = line.strip('\n')
        words = line.split()
        counter += len(words)
    print(counter)