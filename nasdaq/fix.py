import sys

with open('%s' % sys.argv[1], 'r') as f:
	content = f.read().split('\n')

with open('%s' % sys.argv[1], 'w+') as f:
	f.write(',\n'.join(content))