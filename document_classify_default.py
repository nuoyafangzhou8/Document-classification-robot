# 导入相关模块
import os
import shutil
import pathlib
# 定义源文件路径和目标文件夹
file_source=r'F:\sourceforclassify'
file_target1=r'F:\targetforclassify\Document'
file_target2=r'F:\targetforclassify\Picture'
file_target3=r'F:\targetforclassify\Code'
file_target4=r'F:\targetforclassify\Others'
list_do=['.pdf','.docx','.doc','.xlsx','.txt','.xls','.xml']
list_pi=['.jpg','.png','.gif']
list_co=['.py','.js','.html']
# 定义后缀及文件名字符串
file_extension=None
def fileclassifydefault():
    for filename in os.listdir(file_source):
        src_path=os.path.join(file_source, filename)
        file_extension=os.path.splitext(filename)[1].lower()
        os.makedirs(file_target1, exist_ok=True)
        os.makedirs(file_target2, exist_ok=True)
        os.makedirs(file_target3, exist_ok=True)
        os.makedirs(file_target4, exist_ok=True)
        if file_extension in list_do:
            shutil.move(src_path,file_target1)
        elif file_extension in list_pi:
            shutil.move(src_path,file_target2)
        elif file_extension in list_co:
            shutil.move(src_path,file_target3)
        else:
            shutil.move(src_path, file_target4)
if __name__ == '__main__':
    fileclassifydefault()
