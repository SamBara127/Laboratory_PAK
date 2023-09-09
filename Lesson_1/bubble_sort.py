import argparse as arg
import random as rnd


parser = arg.ArgumentParser()
parser.add_argument('value', help='Value of data vector', type=int)
args = parser.parse_args()
buf = []
cont = 0
for i in range(args.value):
    buf.append(round(rnd.random(), 4))
print(buf)
cont = True
while(cont == True):
    cont = False
    for i in range(args.value-1):
        if (buf[i]>buf[i+1]):
            cont = buf[i]
            buf[i] = buf[i+1]
            buf[i+1] = cont
            cont = True
print(buf)

            
