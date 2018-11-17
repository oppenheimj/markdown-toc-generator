# markdown-toc-generator
This script is used to generate a table of contents for a markdown file.

Sample usage:
```
python .\md_toc_generator.py
Enter file path: sample_input.md
Success! Table of contents written to toc_output.md.
```
The file path can be absolute or relative. The script isn't ultra robust but should work in most cases.

# Sample output
Were the the input file to contain the sections below, for example, this is what the generated table of contents would look like. Note that each entry in the table links to the given section.

1. [Structure](#structure)
	1. [The perceptron](#the-perceptron)
	2. [The network](#the-network)
	3. [Implementation](#implementation)
		1. [Weights](#weights)
		2. [Neural activity and output](#neural-activity-and-output)
		3. [Deltas](#deltas)
2. [Operation](#operation)
	1. [Overview](#overview)
	2. [Forward propagation](#forward-propagation)
	3. [Back propagation](#back-propagation)
		1. [Calculating deltas](#calculating-deltas)
		2. [Updating weights](#updating-weights)

# Structure
## The perceptron
## The network
## Implementation
### Weights
### Neural activity and output
### Deltas
# Operation
## Overview
## Forward propagation
## Back propagation
### Calculating deltas
### Updating weights