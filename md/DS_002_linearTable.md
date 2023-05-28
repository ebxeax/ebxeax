# 线性表
## 一、逻辑结构和基本操作
### 1. 逻辑结构
- 具有相同数据类型的n个数据元素的有限序列，表长n，n=0为空表
- 表头：第一个元素
- 表尾：最后一个元素
- 除第一个元素外，每个元素有且仅有一个直接前驱
- 除最后一个元素外，每个元素有且仅有一个直接后继
### 2. 基本操作
```c++
initList(&L);
len(L);
locateElem(L, i);
getElem(L, i);
listInsert(&L, i, e);
listDelete(&L, i, &e);
printList(L);
isEmptyList(L);
destroyList(&L);
```

## 二、顺序存储结构
### 1. 定义：又称顺序表，使用一组地址连续的存储单元，依次存储线性表的数据元素，使逻辑上相邻的两个元素物理位置也相邻
- 存储空间的起始位置data[ ]
- 顺序表最大存储容量MaxSize
- 顺序表当前最大长度len
特点
- 随机访存，O(1)时间复杂度访问
- 存储密度高，每个结点只存储数据元素
- 无需花费空间建立数据之间的逻辑关系，由物理位置相邻特性决定
- 逻辑上物理上均相邻，插入删除操作需要移动大量元素
### 2. 基本操作
（1）插入元素
```c++
//插入元素
boolean listInsert(SqList &L, int i, Elemtype e){
	if(i < 1 || i > L.len + 1)
		return -1;
	if(L.len >= MaxSize)
		return -1;
	for(int j = L.len; j > i; j--)
		L.data[j] = L.data[j - 1];
	L.data[i - 1] = e;
	L.len++;
}
```
分析
- 最好情况
- 最坏情况
- 平均情况
（2）删除元素