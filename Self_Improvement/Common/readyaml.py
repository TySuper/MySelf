"""
1. 安装yaml
    pip install pyyaml
2. yaml使用
    2.1 读yaml文件
    yaml.safe_load(文件)
    yaml.safe_load_all(文件)
"""

import yaml
import os


# path = os.path.split("文件路径")  # 分割目录和文件
# os.path.dirname("文件路径") # 查找文件夹
# os.path.realpath(__file__)
BASE_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0] # 获取当前目录--获取项目目录
CONFIG_FILE = os.path.join(BASE_PATH,'config','interface.yml')  # 将"Common"文件夹的interface.yaml添加到当前目录


class ReadYml:
    def __init__(self,filepath):
        if os.path.exists(filepath):  # 判断文件是否存在
            self.filepath = filepath
        else:
            # print("文件没找到")
            raise FileNotFoundError(f"文件{filepath}没找到")
        self._data = None

    # @property 将类中的方法当做属性来使用
    @property
    def data(self):
        """如果是第一次读取数据,那就使用data(),如果是第二次使用,会读取默认存在的数据"""
        if self._data is None:
            with open(self.filepath,'r',encoding='utf-8') as f:
                self._data = list(yaml.safe_load_all(f))
            return self._data


class Config:
    def __init__(self,configfile=CONFIG_FILE):
        """读取具体yml文件"""
        self.data = ReadYml(configfile).data

    def get(self,name,index=0):
        """根据读取的文件获取具体数据"""
        return self.data[index].get(name)



if __name__ == '__main__':
#     readyml = ReadYml("../config/interface.yml")
#     print(readyml.data)
#     readyml.
#     # print(readyml.get("add_dep"))
    config = Config()
    print(config.get("get_dep"))
    print(config.get("add_dep"))
    print(config.get("upd_dep"))
    print(config.get("del_dep"))
