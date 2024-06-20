import mysql.connector

mydb = mysql.connector.connect(
    host="",
    port="",
    user="root",
    password="my-secret-pw",
    database="onedb"
)

mycursor = mydb.cursor()


# 创建数据库，并展示
#mycursor.execute("Create database onedb")  

# mycursor.execute("Show databases")    

# for x in mycursor:
#     print(x)           


# 建table， 然后展示
# create_table = """create table customers(
#     name varchar(255),
#     address varchar(255)
# )"""
# mycursor.execute(create_table)

# mycursor.execute("show tables")

# for x in mycursor:
#     print(x)

# 往表中插入数据 单行
# sql = "insert into customers (name, address) values (%s, %s)"
# 


# mycursor.execute(sql, val)

# mydb.commit()   #数据库插入数据，要提交确认更改

# print(mycursor.rowcount, "record inserted.")    #rowcount获取最近一次执行SQL语句影响的行数


# 往表中插入数据 多行( 采用列表元组，executemany()方法：两个参数)
# sql = "insert into customers (name, address) values (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql,val)

# mydb.commit()

# print("The last record inserted, ID:", mycursor.lastrowid) 
# print(mycursor.rowcount, "was inserted.") 

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid) 

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid) 

