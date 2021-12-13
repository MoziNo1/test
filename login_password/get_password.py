import os
import sys
import ibm_db
print(sys.path)   # 查看当前路径


from os import path
d = path.dirname(__file__)  # 获取当前路径
parent_path = os.path.dirname(d)  # 获取上一级路径
sys.path.append(parent_path)    # 如果要导入到包在上一级

ibm_db.coonect()
