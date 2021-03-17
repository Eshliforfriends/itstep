data = ['Fast and furious 1', 'Fast and furious 2', 'Fast and furious 1']
with open("any_file.txt", "w") as f:
    f.writelines(line + "\n" for line in data)