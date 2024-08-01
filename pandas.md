# pandas学习笔记

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240801112933074.png" alt="image-20240801112933074" style="zoom: 33%;" />

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240801113136760.png" alt="image-20240801113136760" style="zoom: 33%;" />

### 一维带标签数组Series

```python
import pandas as pd
import numpy as np

# #一维带标签数组；标签：前面的索引；可通过字典创建，可通过range+指定index创建
# p1 = pd.Series([11,22,33,44,55])
# print(p1,type(p1))

#指定索引;不指定索引默认从零开始
# p2 = pd.Series(np.array(range(3,9)), index = ['a','b','c','d','e','f']).astype("int8")#设置数据整型
# print(p2,type(p2))

#传入字典，可以自动变成左右对应的信息
temp_dict = {"name":"xiaoming", "age":13, "tel":123456789}#类型：object
p3 = pd.Series(temp_dict)
# print(p3)#打印的类型也是object

# a = {string.ascii_uppercase[i]:i for i in range(10)}#字典推导式创建一个字典a
# p4 = pd.Series(a)
# p5 = pd.Series(a,index = list(string.ascii_uppercase[5:20]))#多的索引会自动填充NAN
# print(a)
# print(p4)
# print(p5)

#切片和索引
# print(p3[0])#取出0索引的数据
# print(p3["name"])#取出name key;最好不要用防止版本报错

#取出前两行
#print(p3[:2])#取索引0,1
print(p3[[0,1]])#注意用两个方括号
```

### 用pandas打开外部数据

```python
#用pandas打开外部文件
df = pd.read_csv("D:\\1-scRNA-Seq-Analysis\\data-format-transform\\data\\origin\\Mouse-GSM6202261_Liver-1_5DE_genematrix.csv")#直接读取csv文件
print(df)
```

### 二维矩阵Dataframe

```python
#pandas创建dataframe:可以理解为dataframe里存了多个series（每一列对应一个series）
p1 = pd.DataFrame(np.arange(12).reshape(3,4))#第一行为行索引，第一列为列索引
print(p1)

p2 = pd.DataFrame(np.array(range(12)).reshape(3,4), index = list("abc"), columns = ["W", "X", "Y","Z"])#指定行索引（index）和列索引（columns）两个索引的格式不同，要注意
print(p2)

temp_dict = {"name":["xiaoming","xiaohong","xiaolan"],"age":[20,32,89],"tel":[123455,345322,786473]}#key=列索引，行索引默认从0开始;直接将字典转化为dataframe
p3 = pd.DataFrame(temp_dict)
print(p3)

temp2_dict = [{"name":"xiaoming","age":14,"tel":1234322},{"name":"lingling","age":24,"tel":126894652}]#另一种字典，转化为dataframe；某个object没有某个key则会显示nan
p4 = pd.DataFrame(temp2_dict)
print(p4)

print(p4.index,p4.columns)#看看数据的行索引和列索引
print(p4.values) #dataframe里的值
print(p4.shape)#形状
print(p4.dtypes)#每列数据的类型
print(p4.ndim)#维度，几维的

print(p4.head())#默认前五行，填入数字可以改变显示行数
print(p4.tail())#显示后五行

print(p4.info())#展示df的概览
print(p4.describe())#统计dataframe的数据

#按照顺序排列
p4 = p4.sort_values(by = "age")#升序排列,括号里传入要排序的列名
print(p4)
```

