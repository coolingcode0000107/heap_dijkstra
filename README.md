# 用heap实现dijkstra
## 实现
用defaultdict实现邻接表存储边和长度，defaultdict(list)中的list中元素用元组来表示方便解包读取。
用小顶堆实现优先队列，将每次未更新的距离最近的边heappush进priority_queue,每次用heappop取出第一个元素。
*tips：因为可能两个点之间可能有多个边，应该加入判断*
当priority_queue空时停止。
本代码目的用来解决洛谷单源最短路径问题，但是加入堆优化后还是超时。
（~~本人刚学python还是太弱了~~）
[P3371 【模板】单源最短路径（弱化版） - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P3371)
