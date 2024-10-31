file_path = '/html/csv/text.txt'

with open(file_path, encoding="UTF-8") as file_in:
    them = {"subject": file_in.readline().rstrip('\n')}
    symbols = file_in.read()
    # line = []
    # for symbol in symbols:
    #     try:
    #         if symbol + 1 == '"':
    #             symbol = '\\'
    #             line.append(symbol)
    #     except:line.append('symbol')

file_in.close()

# print(line)

print(f'{symbols}')
print(f'--\n--\n')
# print(f'--\n-- to text:\n')
# print([symbols])

new_line = []
for symbol in symbols:
    if symbol  == '"':
        symbol = '\\"'
    if symbol == '\n' or symbols == '\r':
        symbol = '\\n'
        # new_line.append(symbol)
    new_line.append(symbol)
# print(new_line)
strin = ""
# str1 = ( "geeks", "for", "geeks" )
print(f'--{them}\n-- to HTML:\n')
print(strin.join(new_line))


