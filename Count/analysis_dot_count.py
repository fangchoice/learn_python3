"""
  分析count值是不是连续的
"""

from itertools import groupby

last_count = -1
join_FE = []
store_count = []

with open('test.txt', 'r') as f:
    for line in f:
        data = line.lower().replace(' ','').strip()

        if data.startswith('fe'):
            if data[2] == '1' or data[3] == '1':
                join_FE.append(data)
            if data[2] == '2' or data[3] == '2':
                join_FE.append(data)
                a = join_FE[0] + join_FE[1]
                fe_num = int(data[-10: -8], base=16)

                store_count.append(fe_num)
                if last_count != -1:
                    if fe_num == last_count:
                        cm = fe_num + 247
                    else:
                        cm = fe_num
                    if cm - last_count != 1:
                        print('red')

                last_count = fe_num
                print('{:<40}, count = {:<4}'.format(a, fe_num))
            
        elif data.startswith('fc'):
            fc_num = int(data[-2:], base=16)
            if last_count != -1:
                if fc_num < last_count:
                    cm = fc_num + 247
                else:
                    cm = fc_num
                if cm - last_count != 1:
                    print('red')
                
            last_count = fc_num
            print('{:<40}, count = {:<4}'.format(data, fc_num))
            store_count.append(fc_num)

def continue_num_range():
    func = lambda x: x[1] - x[0]
    discard_num = 0

    for k, g in groupby(enumerate(store_count), func):
        l1 = [j for i,j in g]
        if len(l1) > 1:
            scope = str(min(l1)) + '-' + str(max(l1))
            if min(l1) > 0 or max(l1) < 246:
                discard_num += 1

        else:
            scope = l1[0]
        print("Continue Num Range : {}".format(scope))
    
    print('-'*70)
    if discard_num - 2 >= 0:
        print('Discard Count: {}'.format( discard_num - 2))
    else:
        print('Discard Count: {}'.format(0))
    print('-'*70)

continue_num_range()
join_FE.clear()
store_count.clear()
