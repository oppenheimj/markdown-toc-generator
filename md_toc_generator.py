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

def write_output_file():
  outfile = open('output.md', 'w')

  for entry in table_of_contents:
    outfile.write(entry + '\n')

  outfile.close()

infile = open('sample_input.md', 'r')
table_of_contents = []

depth2count = {}
previous_depth = 1

sections = [line for line in infile if line[0] == '#']

for section in sections:
  split_section = section.split()

  depth = len(split_section[0])

  spacing = (depth - 1) * '\t'
  number = depth_to_line_number(depth, previous_depth)
  title = ' '.join(split_section[1:])
  link = '#' + '-'.join([word.lower() for word in split_section[1:]])

  table_of_contents.append(spacing + number + markdown_hyperlink(title, link))

  previous_depth = depth

write_output_file()