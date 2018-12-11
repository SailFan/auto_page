"""
项目公共内容配置，以及读取配置文件中的配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""

import os
import logging
from yaml_read import YamlReader
# 所有相关文件的路径
# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH,'resources', 'conf', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')



class Config:
    def __init__(self, config = CONFIG_FILE, index=1, element = "home"):
            logging.warning('配置文件地址：',config)
            self.config = YamlReader(config).data
    def get(self, element, index):
        return self.config[index].get(element)




if __name__ == '__main__':
    c = Config()
    print(c.config)
