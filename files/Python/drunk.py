
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import hashlib
import time

parser = argparse.ArgumentParser(description='drunk.py the drinking script.')
parser.add_argument('-o', '--output', help='specificy output file.',
                    type=argparse.FileType('w'), action='store', nargs='?',
                    default=open('drunk.txt', 'w'))
parser.add_argument('-t', '--time', help='specificy time between drinks',
                    type=int, action='store', nargs='?', default=5)
parser.add_argument('-v', '--verbose', action='count',
                    help='increase output verbosity')
args = parser.parse_args()

lines = []

try:
    while True:
        try:
            sha = hashlib.sha3_256(text.encode('utf-8')).hexdigest()
            text = '{} - Drink ! {}'.format(
                time.strftime('%d/%m/%y, %H:%M:%S', time.localtime()), sha[:8]
                )
        except NameError:
            sha = '58535fe5'
            text = '{} - First drink ! {}'.format(
                time.strftime('%d/%m/%y, %H:%M:%S', time.localtime()), sha[:8]
                )
        if args.verbose == 1:
            print(text.split(' - ', 1)[1].split(' ! ', 1)[0])
        elif args.verbose == 2:
            print(text.split(', ', 1)[1])
        else:
            print(text)
        lines.append(text+'\n')
        time.sleep(args.time)
except KeyboardInterrupt:
    args.output.writelines(lines)

