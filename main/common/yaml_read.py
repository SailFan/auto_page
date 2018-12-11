# 用于文件的读取,包含配置文件和数据文件的读取函数.根据文件地址，返回文件中包含的内容
import yaml;
import os
from xlrd import open_workbook

class YamlReader():
    def __init__(self, yamlFilePath):
        if os.path.exists(yamlFilePath):
            self.yamlFilePath = yamlFilePath;
        else:
            raise FileNotFoundError("文件不存在");
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlFilePath, "rb") as f:
                self._data = list(yaml.safe_load_all(f))
        return  self._data;


class SheetTypeError(Exception):
    pass


class ExcelReader():
    def __init__(self, excelpath, sheet=0, title_line=False):
        if os.path.exists(excelpath):
            self.excelpath = excelpath  # excel文件路径
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet  # sheet可以是int表示表格的索引，可以是str表示表格的名称
        self.title_line = title_line  # 是否存在标题行，有标题行，每一行都是都是对应列名的取值；没有标题行，每一行都是一个列表
        self._data = list()  # 用于存储每行生成的数据。

    @property
    def data(self):
        if not self._data :
            workbook  = open_workbook(self.excelpath)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0) # 首行为title
                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
        return self._data;



if __name__=="__main__":
    # y = 'D:\Test_framework\config\config.yml'
    # reader = YamlReader(y);
    # print(reader.data)

    e = 'D:/Test_framework/data/baidu.xlsx'
    reader = ExcelReader(e, title_line=True,sheet="Sheet2")
    print(reader.data)