
infile = open('markdown_file.md', 'r')
table_of_contents = []

def markdown_hyperlink(text, url):
  return '[' + text + '](' + url + ')'

sections = [line for line in infile if line[0] == '#']

depth2count = {}
previous_depth = 1

for section in sections:
  split_section = section.split()

  depth = len(split_section[0])

  if depth < previous_depth:
    for key in range(previous_depth, depth, -1):
      depth2count.pop(key, None)

  try:
    depth2count[depth] += 1
  except:
    depth2count[depth] = 1

  spacing = ((len(split_section[0]) - 1) * '\t')
  number = str(depth2count[depth]) + '. '
  title = ' '.join(split_section[1:])
  link = '#' + '-'.join([x.lower() for x in split_section[1:]])

  table_of_contents.append(spacing + number + markdown_hyperlink(title, link))

  previous_depth = depth

outfile = open('output.md', 'w')
for entry in table_of_contents:
  outfile.write(entry + '\n')
outfile.close()