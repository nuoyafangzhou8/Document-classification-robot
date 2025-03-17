
# 一些优化
# 导入相关模块
import os
import shutil
import pathlib
from document-classify-default import fileclassifydefault
# 定义源文件路径和目标文件夹

# file_target1=r'F:\targetforclassify\Document'
# file_target2=r'F:\targetforclassify\Picture'
# file_target3=r'F:\targetforclassify\Code'
# file_target4=r'F:\targetforclassify\Others'
# list_do=['.pdf','.docx','.doc','.xlsx','.txt','.xls','.xml']
# list_pi=['.jpg','.png','.gif']
# list_co=['.py','.js','.html']
# 定义后缀及文件名字符串
file_extension=None
# 封装一个函数fileclassify()
def fileclassify(file_source):
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


# 输入文件夹定义主函数
if __name__ == '__main__':
    try:
        file_source=input('请输入需要整理的文件路径：')
        file_target1=input('请输入第一类文件的存放路径：')
        list_do=input('请输入第一类文件的后缀（以列表形式输入）：')
        file_target2 = input('请输入第二类文件的存放路径：')
        list_pi=input('请输入第二类文件的后缀（以列表形式输入）：')
        file_target3 = input('请输入第三类文件的存放路径：')
        list_co = input('请输入第三类文件的后缀（以列表形式输入）：')
        file_target4 = input('请输入其它文件的存放路径：')
        fileclassify(file_source)
    except FileNotFoundError:
        fileclassifydefault()


