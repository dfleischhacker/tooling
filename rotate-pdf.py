#!/usr/bin/env python

# rotates the given PDF file

import subprocess
import sys
import shutil

if len(sys.argv) != 3:
	print 'Usage:\n\t<pdf file> <rotation [R|L]>'
	sys.exit(1)

file_name = sys.argv[1]

subprocess.call(['/usr/bin/pdftk', file_name, 'cat', '1-end%s' % (str(sys.argv[2])), 'output', 'temp%s' % file_name])

shutil.move(file_name, '%s_orig' % file_name)
shutil.move('temp%s' % file_name, file_name)
