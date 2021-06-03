str_num = 0
quan_str = 0
with open('hw5_q2.txt') as content:
    for lines in content:
        separ_lines = lines.split()
        word_num = len(separ_lines)
        quan_str += 1
        print(f"line {quan_str} has {word_num} words")
print(f"total strings: {quan_str}")