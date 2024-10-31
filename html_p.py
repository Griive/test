# from sys import stdin

file_path = '/html/csv/text.txt'

with open(file_path, encoding="UTF-8") as file_in:
    _ = ""
    for line in file_in:
        _ = line.rstrip("\n")
        print( f'{"<p>"}{_}{"</p>"}')