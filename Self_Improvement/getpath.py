# -*- coding:utf-8-*-
import os


def get_path():
    """获取项目的根目录"""
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == '__main__':
    res=get_path()
    print(get_path())
    print(os.path.join(res, "a"))
    print('测试路径是否OK,路径为：', get_path())
