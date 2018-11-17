depth2count = {}

def depth_to_line_number(depth, previous_depth):
  if depth < previous_depth:
    for key in range(previous_depth, depth, -1):
      depth2count.pop(key, None)

  try:
    depth2count[depth] += 1
  except:
    depth2count[depth] = 1

  return str(depth2count[depth]) + '. '

def markdown_hyperlink(text, url):
  return '[' + text + '](' + url + ')'

def read_file():
  try:
    file_path = input('Enter file path: ')
    infile = open(file_path, 'r')
    sections = [line for line in infile if line[0] == '#']
    infile.close()

    return sections
  except:
    print('Error reading file.')
    return read_file()

def write_file(table_of_contents):
  outfile_name = 'toc_output.md'
  outfile = open(outfile_name, 'w')

  for entry in table_of_contents:
    outfile.write(entry + '\n')

  outfile.close()
  print(f'Success! Table of contents written to {outfile_name}.')

def generate_table_of_contents(sections):
  table_of_contents = []
  previous_depth = 1

  for section in sections:
    split_section = section.split()
    depth = len(split_section[0])

    spacing = (depth - 1) * '\t'
    number = depth_to_line_number(depth, previous_depth)
    title = ' '.join(split_section[1:])
    link = '#' + '-'.join([word.lower() for word in split_section[1:]])

    table_of_contents.append(spacing + number + markdown_hyperlink(title, link))

    previous_depth = depth

  return table_of_contents

sections = read_file()
table_of_contents = generate_table_of_contents(sections)
write_file(table_of_contents)
