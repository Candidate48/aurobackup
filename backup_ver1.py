# coding=gbk
# Filename: backup_ver1.py
import shutil
import os
import time

#Դ�ļ�Ŀ¼
source = 'D:\\share'#, '/home/swaroop/bin'
#Ŀ��Ŀ¼
dst_dir = r'D:\backup' # Remember to change this to what you will be using
#������
target = dst_dir + '\\share'+time.strftime('%Y%m%d%H%M%S') + '.rar'

copy_dir = dst_dir+'\\share'







# ���ʹ���в���ѹ������ ���ø����ļ�

if(os.path.exists(copy_dir)):
    shutil.rmtree(copy_dir)
# self.del_old_backups()
#�Ӵ�д����־ δ��
#�����ļ����ļ���
try:
    shutil.copytree(source, copy_dir)
except Exception as msg:

    print(msg)
#ѹ��ָ���ļ��е��ļ���������
rar_command = "winrar a -ibck {} {}".format(target, copy_dir)
print(rar_command)

# ִ��������
if os.system(rar_command) == 0:
    all_files = []
    for files in os.walk(dst_dir):
        all_files.append(files[2])
    print("all_files ")
    print(all_files[0])

    # ��ȡbackup �е��ļ�Ϊ���ݵ��ļ�
    backup_files = []
    for file_name in all_files[0]:
        if 'share' in file_name:
            if '.rar' in file_name:
                backup_files.append(file_name)
    print("del_files ")

    # ɸѡ����Ҫɾ����


    del_backup_list = backup_files[0:len(backup_files) - 5]
    print(del_backup_list)

    # ɾ����5�����ϵ��ļ�
    for del_back in del_backup_list:
        os.remove(dst_dir + '\\' + del_back)
    print('Successful backup to', target)
else:
    print('Backup FAILED')

def del_old_backups():
    # ��ȡbackup �е��ļ�
    all_files = []
    for files in os.walk(dst_dir):
        all_files.append(files[2])
    print("all_files ")
    print(all_files[0])

    # ��ȡbackup �е��ļ�Ϊ���ݵ��ļ�
    backup_files = []
    for file_name in all_files[0]:
        if 'share' in file_name:
            if '.rar' in file_name:
                backup_files.append(file_name)
    print("del_files ")

    # ɸѡ����Ҫɾ����


    del_backup_list = backup_files[0:len(backup_files) - 5]
    print(del_backup_list)

    # ɾ����5�����ϵ��ļ�
    for del_back in del_backup_list:
        os.remove(dst_dir + '\\' + del_back)

