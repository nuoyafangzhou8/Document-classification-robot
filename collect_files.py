# 引用模块
import os
import shutil
from pathlib import Path
# 实现将路径下所有文件收集到一个路径下
targetpath=r'F:\sourceforclassify' # 目标路径
sourcepath=r'F:\targetforclassify' # 源路径
# 实例化源路径
res=Path(sourcepath)
# 遍历所有文件并移动到目标路径下
for item in res.rglob('*'): # rglog功能是递归生成所有存在的文件包括文件夹，不管其处在树形结构的什么位置。
    temp_file=Path(item)
    tar = Path(targetpath)/(temp_file.name)
    # 判断实例是否是文件
    if temp_file.is_file():
        temp_file.rename(tar) # 将源文件转移到目标路径下

# 转移完成后遍历所有文件并删除空文件夹
for item in res.rglob('*'):
    temp_file=Path(item)
    # if temp_file.is_dir():
    temp_file.rmdir() # 删除空文件夹

