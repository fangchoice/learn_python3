

"""
	在一个文件的每行都加上特定字符
"""

with open('demo2.sql', 'w+', encoding='utf-8') as fw:
	with open('demo.sql', 'r', encoding='utf-8') as f:
		for line in f:
			if line.strip() != "":
				new_line = line.strip() + ';\n'
				fw.write(new_line)

