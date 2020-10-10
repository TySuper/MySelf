# -*- coding:utf-8 -*-
import os


def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == '__main__':
    # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
    path = get_Path()  # 调用实例化，这个类返回的路径为当前项目所在路径
    config_path = os.path.join(path, 'config.ini')  # 这句话是在path路径下再加一级
