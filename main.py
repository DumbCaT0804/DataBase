# import mariadb_operation.add 导入模块里的某个子模块
import mariadb_operation as ma_op
x,y = 3, 9

#z = mariadb_operation.add.add(x, y)
z = ma_op.add(x, y)
print(z)