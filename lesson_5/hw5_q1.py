import sys
with open('hw5_q1.txt', 'w') as content:
    while 1 == 1:
        input_data = input('Input data: ')
        content.write(input_data)
        content.write('\n')
        stop = len(input_data)
        if stop == 0:
            sys.exit(0)

