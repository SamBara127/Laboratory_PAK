import argparse as arg


parser = arg.ArgumentParser()
parser.add_argument('high', help='Value of top Pascal trangle', type=int)
args = parser.parse_args()


row = [1]
for i in range(args.high):
    for k in range(int(args.high-len(row))):
        print(' ', end=' ')
    print(row)
    row = [sum(x) for x in zip([0]+row, row+[0])]
        
