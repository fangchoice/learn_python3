

"""
  left             right
   |               |
  [5,7,4,6,3,1,2,9,8]
  
  取出 tmp = li[left]
  
  [_,7,4,6,3,1,2,9,8]
  
  找到右边比tmp小的数
  left         right
   |           |
  [_,7,4,6,3,1,2,9,8]
  
  把右边的值放在左边的空位上
  [2,7,4,6,3,1,_,9,8]
  
  此时找到左边比tmp大的数
    left       right
     |         |
  [2,7,4,6,3,1,_,9,8]
  
  把左边的值放在右边的空位上
  [2,_,4,6,3,1,7,9,8]
  
  依次类推
          left
           |
  [2,1,4,3,_,6,7,9,8]
           |
          right
  
  
"""



def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1           # 往左走一步
        li[left] = li[right]     # 把右边的值写在左边的空位上
        print(li)
        while left < right and li[left] <= tmp:   # 从左边找比tmp大的数
            left += 1            # 往右走一步
        li[right] = li[left]     # 把左边的值写到右边空位上
    li[left] = tmp               # 把tmp归位
    return left                  # 返回中间的位置

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid+1, right)


li = [5,7,4,6,3,1,2,9,8]
print(li)
# partition(li, 0, len(li) - 1)
quick_sort(li, 0, len(li)-1)
print(li)

