
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

FILES = {
    
}

with open('test.txt', 'r') as f:
    for line in f:
        filename = line[10:22]
        data = line[26:-1]

        if filename not in FILES:
            FILES[filename] = [data]
        else:
            FILES[filename].append(data)


for k in FILES:
    with open(k + '.txt', 'w') as fw:
        fw.write("".join(FILES[k]))