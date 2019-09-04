# from pymediainfo import MediaInfo
#
# media_info = MediaInfo.parse(r'G:\微课\案件管理中如何督促和落实司法责任制.mp4')
# data = media_info.to_json()
# # data = media_info.to_data()
# print(data)
# # print(data['tracks'][0]['file_name'])

import os


# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))

#
# def file_name(file_dir):
#     """
#     获取目录下所有文件及文件夹
#     :param file_dir:
#     :return:{'files': files, 'dirs': dirs}
#     """
#     files = []
#     dirs = []
#     for dirPath, dirNames, fileNames in os.walk(file_dir):
#         for file in fileNames:
#             # if os.path.splitext(file)[1] == '.jpg':
#             files.append(os.path.join(dirPath, file))
#         for dir in dirNames:
#             dirs.append(os.path.join(dirPath, dir))
#             # print(dirs)
#     return {'files': files, 'dirs': dirs}
#
#
# print(file_name("D:\视频")['files'])









