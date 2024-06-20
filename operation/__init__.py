# init.py
# 1. 声明一个模块
# 2. 封装，提供外部接口和类型，隐藏具体实现方法
# 3. 只导入必要内容, 因为每次import mariadb_operation都会执行init.py中所有内容
import mariadb_operation.add

add = mariadb_operation.add.add # 子模块里的函数方法