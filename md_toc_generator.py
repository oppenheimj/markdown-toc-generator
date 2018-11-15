
infile = open('markdown_file.md', 'r')
toc = []

sections = [line for line in infile if line[0] == '#']


for section in sections:
  toc_entry = ''
  split_section = section.split()
  toc_entry += ((len(split_section[0]) - 1) * '\t')