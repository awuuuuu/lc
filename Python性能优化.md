#Python 性能优化
https://www.ibm.com/developerworks/cn/linux/l-cn-python-optim/index.html

##交换变量，用a,b=b,a,而不是设置一个tmp

##if done is not None 比语句 if done != None 更快

## operator.add(a,b)快，lt,le,eq,
https://docs.python.org/2/library/operator.html

##while 1 要比 while True 更快

##字符串连接的使用尽量使用 join() 而不是 +

