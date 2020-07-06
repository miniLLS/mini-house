import numpy as np

'''
ndarray 实际上是多维数组的含义。
在 NumPy 数组中，维数称为秩（rank），一维数组的秩为 1，二维数组的秩为 2，以此类推。
在 NumPy 中，每一个线性的数组称为一个轴（axes），其实秩就是描述轴的数量。
'''

def dp():
    '''
    divider_printer
    '''
    print('-'*20 + '\n')

dp()
#创建数组
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)
b[1, 1] = 10
print(b)

dp()
#结构数组
persontype = np.dtype({'names': ['name', 'age', 'chinese', 'math', 'english'], 'formats': ['S32', 'i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei", 32, 75, 100, 90),
                    ("GuanYu", 24, 85, 96, 88.5),
                    ("ZhaoYun", 28, 85, 92, 96.5),
                    ("HuangZhong", 29, 65, 85, 100)], dtype=persontype)
age = peoples[:]['age']
chinese = peoples[:]['chinese']
math = peoples[:]['math']
english = peoples[:]['english']
print(np.mean(age))
print(math)

dp()
#连续数组的创建
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(x1)
print(type(x1))
print(x1[0])
print(type(x1[0]))  #arange默认创建int类型
print(x2)
print(type(x2))
print(x2[-1])
print(type(x2[-1])) #linspace，linear space，默认创建float类型

dp()
#算数运算
print(np.add(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))

dp()
#计数组 / 矩阵中的最大值函数 amax()，最小值函数 amin()
cal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amax(cal))
print(np.amin(cal))
print(np.amax(cal, 0))  #axis=0，沿着row（行）的方向区分元素
print(np.amax(cal, 1))  #axis=1，沿着column（列）的方向区分元素

dp()
#统计最大值与最小值之差 ptp()
print(np.ptp(cal))
print(np.ptp(cal, 0))

dp()
#统计数组的百分位数 percentile()
print(np.percentile(cal, 100))
print(np.percentile(cal, 0))
print(np.percentile(cal, 50))
print(np.percentile(cal, 100, axis=0))

dp()
#统计数组中的中位数 median()、平均数 mean()
print(np.median(cal))
print(np.mean(cal))

dp()
#统计数组中的加权平均值 average()
print(np.average(cal[0]))
wts = np.array([1, 2, 3])
print(np.average(cal[0], weights=wts))

dp()
#统计数组中的标准差 std()、方差 var()
print(np.var(cal[0]))
print(np.std(cal[0]))
print((2/3)**0.5)

dp()
#NumPy 排序
#sort(a, axis=-1, kind=‘quicksort’, order=None)
#在 kind 里，可以指定 quicksort、mergesort、heapsort 分别表示快速排序、合并排序、堆排序。\
example = np.array([[4, 3, 2], [2, 4, 1]])
print(np.sort(example))
print(np.sort(example, axis=None))  #采用扁平化的方式作为一个向量进行排序
print(np.sort(example, axis=0))
print(np.sort(example, axis=1))
#order 字段，对于结构化的数组可以指定按照某个字段进行排序

dp()
'''
练习：

'''