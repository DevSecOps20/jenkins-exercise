import os
import sys

if len(sys.argv) !=2:
    print('USAGE: python expects 1 arg ')
    sys.exit(1)

word = sys.argv[1]
file_to_test= os.environ.get('FILE_TO_TEST')

if not file_to_test:
    print("ERROR: env 'FILE_TO_TEST' not declared ")
    sys.exit(2)

if not os.path.isfile(file_to_test):
    print(f"ERROR: canno open this file : {file_to_test} ")
    sys.exit(127)

try:
    with open(file_to_test,'r') as file:
        content = file.read()
except Exception as e:
    print('ERROR: cannot convert the content')

if word not in content:
    print(f"TEST FAILED: {word} wasnt found in {file_to_test}")
    sys.exit(1)

print('TEST PASSED ')
sys.exit(0)