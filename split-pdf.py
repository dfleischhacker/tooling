#!/usr/bin/env python

"""
Splits the given PDF into parts at the given page numbers

Depends:
	* pdftk
"""

import sys
import subprocess


if len(sys.argv) < 3:
	print 'Usage:\n\t<pdf file> <page number to split at> [...]'
	sys.exit(1)

split_points = []

file_name = sys.argv[1]

for split_point in sys.argv[2:]:
	split_points.append(split_point)

# rotate 

start_page = 1
for page in split_points:
	end_page = str(int(page) - 1)
	subprocess.call(['/usr/bin/pdftk', '%s' % file_name, 'cat', '%s-%s' % (str(start_page), str(end_page)), 'output', '%s.pdf' % str(start_page)])
	start_page = page

end_page = 'end'

subprocess.call(['/usr/bin/pdftk', '%s' % file_name, 'cat', '%s-%s' % (start_page, end_page), 'output', '%s.pdf' % start_page])

