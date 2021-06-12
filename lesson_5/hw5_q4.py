with open('hw5_q4.txt') as content:
    for lines in content:
        lines = lines.split()
        if 'One' in lines:
            lines.remove('One')
            lines.insert(0, 'Один')
            lines.insert(3, '\n\n')
            lines_str = ' '.join(lines)
            r_list = open('hw5_q4_r', 'w')
            r_list.write(lines_str)
        elif 'Two' in lines:
            lines.remove('Two')
            lines.insert(0, 'Два')
            lines.insert(3, '\n\n')
            lines_str = ' '.join(lines)
            r_list.write(lines_str)
        elif 'Three' in lines:
            lines.remove('Three')
            lines.insert(0, 'Три')
            lines.insert(3, '\n\n')
            lines_str = ' '.join(lines)
            r_list.write(lines_str)
        elif 'Four' in lines:
            lines.remove('Four')
            lines.insert(0, 'Четыре')
            lines_str = ' '.join(lines)
            r_list.write(lines_str)
            r_list.close()