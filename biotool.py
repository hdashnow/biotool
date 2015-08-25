"""
We're going to make a solid start with quite a few of these issues,
simply by using python's inbuilt argparse module, namely:
1. Print something if no parameters are supplied
2. Always have a "-h" or "--help" switch
6. Validate your parameters
"""

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const='sum', default='max',
                   help='sum the integers (default: find the max)')

# 3. Have a "-v" or "--version" switch
# I chose --version, not -v because some programs like grep use -v to mean inverse
parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')


args = parser.parse_args()

if args.accumulate == 'sum':
    print(sum(args.integers))
elif args.accumulate == 'max':
    print(max(args.integers))

"""
Still to-do:
4. Do not use stdout for messages and errors
5. Always raise an error if something goes wrong
7. Don't hard-code any paths
8. Don't pollute the PATH
9. Check that your dependencies are installed
10. Don't distribute bare JAR files
"""
