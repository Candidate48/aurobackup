# coding=gbk
# Filename: backup_ver1.py
import shutil
import os
import time

#源文件目录
source = 'D:\\share'#, '/home/swaroop/bin'
#目标目录
dst_dir = r'D:\backup' # Remember to change this to what you will be using
#备份名
target = dst_dir + '\\share'+time.strftime('%Y%m%d%H%M%S') + '.rar'

copy_dir = dst_dir+'\\share'







# 解决使用中不能压缩问题 利用复制文件

if(os.path.exists(copy_dir)):
    shutil.rmtree(copy_dir)
# self.del_old_backups()
#接错写入日志 未做
#复制文件至文件夹
try:
    shutil.copytree(source, copy_dir)
except Exception as msg:

    print(msg)
#压缩指定文件夹的文件的命令行
rar_command = "winrar a -ibck {} {}".format(target, copy_dir)
print(rar_command)

# 执行命令行
if os.system(rar_command) == 0:
    all_files = []
    for files in os.walk(dst_dir):
        all_files.append(files[2])
    print("all_files ")
    print(all_files[0])

    # 获取backup 中的文件为备份的文件
    backup_files = []
    for file_name in all_files[0]:
        if 'share' in file_name:
            if '.rar' in file_name:
                backup_files.append(file_name)
    print("del_files ")

    # 筛选出需要删除的


    del_backup_list = backup_files[0:len(backup_files) - 5]
    print(del_backup_list)

    # 删除第5个以上的文件
    for del_back in del_backup_list:
        os.remove(dst_dir + '\\' + del_back)
    print('Successful backup to', target)
else:
    print('Backup FAILED')

def del_old_backups():
    # 获取backup 中的文件
    all_files = []
    for files in os.walk(dst_dir):
        all_files.append(files[2])
    print("all_files ")
    print(all_files[0])

    # 获取backup 中的文件为备份的文件
    backup_files = []
    for file_name in all_files[0]:
        if 'share' in file_name:
            if '.rar' in file_name:
                backup_files.append(file_name)
    print("del_files ")

    # 筛选出需要删除的


    del_backup_list = backup_files[0:len(backup_files) - 5]
    print(del_backup_list)

    # 删除第5个以上的文件
    for del_back in del_backup_list:
        os.remove(dst_dir + '\\' + del_back)

