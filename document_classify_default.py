# 导入相关模块
import os
import shutil
import pathlib
# 定义源文件路径和目标文件夹
file_source=r'F:\sourceforclassify'  # 需要分类的源文件路径
file_target1=r'F:\targetforclassify\Document' # 第一个目标文件路径用于存放文件
file_target2=r'F:\targetforclassify\Picture'  # 第二个目标文件路径用于存放图片
file_target3=r'F:\targetforclassify\Code'     # 第三个目标文件路径用于存放代码
file_target4=r'F:\targetforclassify\Others'   # 第四个目标文件路径 用于存放其他类型文件
list_do=['.pdf','.docx','.doc','.xlsx','.txt','.xls','.xml'] # 文件类型的后缀
list_pi=['.jpg','.png','.gif'] # 图片类型的后缀
list_co=['.py','.js','.html']  # 代码类型的后缀
# 定义后缀及文件名字符串
file_extension=None
# 定义默认文件分类函数
def fileclassifydefault():
    # 遍历所有文件并将文件按照后缀移动到指定的文件夹中
    for filename in os.listdir(file_source): #listdir的功能是返回包含目录中文件名的列表，此处遍历生成包含所有文件名的列表
        src_path=os.path.join(file_source, filename) # 将路径与文件名组合生成新路径
        file_extension=os.path.splitext(filename)[1].lower() # 将文件名通过'.'分割，取第二个部分（后缀）并转化为小写赋给file_extension
        os.makedirs(file_target1, exist_ok=True) # 创建file_target1的目录，如果存在则覆盖
        os.makedirs(file_target2, exist_ok=True)
        os.makedirs(file_target3, exist_ok=True)
        os.makedirs(file_target4, exist_ok=True)
        if file_extension in list_do: # 判读后缀在list_do列表中则将文件移动到file_target1目录下
            shutil.move(src_path,file_target1)
        elif file_extension in list_pi:
            shutil.move(src_path,file_target2)
        elif file_extension in list_co:
            shutil.move(src_path,file_target3)
        else:
            shutil.move(src_path, file_target4) # 以上都不是则将文件移动到file_target4目录下
if __name__ == '__main__':
    fileclassifydefault()
