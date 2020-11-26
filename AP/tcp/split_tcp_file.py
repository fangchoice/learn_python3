
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

FILES = {
    
}


with open('test.txt', 'r') as f:
    for line_data in f:
    	if line_data.startswith('f0aa01') and len(line_data)>=46:
            sub_string = line_data[:10].strip()
            cnt = line_data.count(sub_string)
            split_data = line_data.split(sub_string, cnt)
        
            for index, data in enumerate(split_data, 1):
                filename = data[:12]
              
                if filename not in FILES:
                    FILES[filename] = [data[16:].strip()]
                else:
                    FILES[filename].append(data[16:].strip())

for k in FILES:
    with open(k + '.txt', 'w') as fw:
        fw.write("".join(FILES[k]))
