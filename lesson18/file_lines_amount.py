with open('lines.txt', 'r') as f:
    counter = 0
    lines = f.read()
    content = lines.split('\n')
    for line in content:
        if line:
            counter += 1
    print(counter)