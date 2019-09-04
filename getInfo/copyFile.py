import os
import shutil

file_dir = 'E:/video'
newPath = 'E:/111111111111'


def file_name(file_dir):
    """
    获取目录下所有文件及文件夹
    :param file_dir:
    :return:{'files': files, 'dirs': dirs}
    """
    files = []
    dirs = []
    for dirPath, dirNames, fileNames in os.walk(file_dir):
        for file in fileNames:
            # if os.path.splitext(file)[1] == '.jpg':
            files.append(os.path.join(dirPath, file))
        for dir in dirNames:
            dirs.append(os.path.join(dirPath, dir))
            # print(dirs)
    return {'files': files, 'dirs': dirs}


def getFileType(file):
    """
    判断文件类型
    :param file:
    :return:string
    """
    if file.endswith(('.mp4', '.mkv', '.avi', '.wmv', '.iso', 'mov', 'mpeg')):
        return 'video'
    elif file.endswith(('.mpg', '.png', '.jpg', '.jpeg', '.gif')):
        return 'image'
    elif file.endswith(('.mp3', '.wma', '.wave', '.cd')):
        return 'audio'
    else:
        print(file)
        return 'other'


def copyFile(files):
    """
    根据文件后缀复制到对应文件夹
    :param files: 文件集合
    :return:
    """
    i = 1
    print(files)
    new_V_Path = newPath + '/video'
    new_Ima_Path = newPath + '/image'
    new_A_Path = newPath + '/audio'
    new_other_Path = newPath + '/other'
    for file in files:
        print('正在处理第 %d 个文件:' % i + file)
        if getFileType(file) == 'video':    # 判断文件类型
            if not os.path.exists(new_V_Path):  # 判断文件夹是否存在
                os.makedirs(new_V_Path)  # 创建文件夹
            # shutil.copy(file, new_V_Path)
        if getFileType(file) == 'image':
            if not os.path.exists(new_Ima_Path):
                os.makedirs(new_Ima_Path)
            # shutil.copy(file, new_Ima_Path)
        if getFileType(file) == 'audio':
            if not os.path.exists(new_A_Path):
                os.makedirs(new_A_Path)
            # shutil.copy(file, new_A_Path)
        if getFileType(file) == 'other':
            if not os.path.exists(new_other_Path):
                os.makedirs(new_other_Path)
            # shutil.copy(file, new_other_Path)
        i += 1
    print('复制结束')


copyFile(file_name(file_dir)['files'])
