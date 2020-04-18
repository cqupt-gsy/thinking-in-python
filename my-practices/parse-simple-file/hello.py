import sys
skip_line = int(sys.argv[1])
current_line = 0
files = open("test")
file_contents = files.readlines()
skip_header_line = skip_line + 1
skip_tail_line = len(file_contents) - skip_line - 1
contents = []

for line in file_contents:
    if(current_line < skip_header_line) or (current_line > skip_tail_line):
        current_line += 1
        continue
    current_line += 1
    contents.append(line.strip())

files.close()

content_maps = {}
current_row = 1
current_colunm = 1

for line in contents:
    row_content = line.split(" ")
    for colunm_content in row_content:
        content_maps[str(current_row)+str(current_colunm)] = colunm_content
        current_colunm += 1
    current_row += 1
    current_colunm = 1

read_row_begin = int(sys.argv[2])
read_row_end = int(sys.argv[3])
read_colunm_begin = int(sys.argv[4])
read_colunm_end = int(sys.argv[5])

results = []

for row_number in range(read_row_begin, read_row_end+1):
    for colunm_number in range(read_colunm_begin, read_colunm_end+1):
        results.append(content_maps[str(row_number)+str(colunm_number)])




print(results)


