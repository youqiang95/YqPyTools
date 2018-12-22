# coding: utf-8

class FormatData(object):
    def __init__(self, source_data):
        self.source_data = source_data
    
    def transform_to_format(self):
        # 需要子类实现
        pass


class TableFormatData(FormatData):
    def __init__(self, source_data, field_length=None):
        # source_data 为二维数组，其中的每个一维数组代表一行记录，长度必须一致。
        # field_length 为列宽
        super(TableFormatData, self).__init__(source_data)
        self.field_length = field_length
        need_updata_flg = True if not self.field_length else False
        self.check_source_data(need_updata_flg)

    def check_source_data(self,need_updata_flg=True):
        source_data = self.source_data
        if not source_data:
            raise Exception('source data must True')
        elif not isinstance(source_data, list):
            raise Exception('source data must a list but %s given'%(type(source_data)))
        else:
            length = len(source_data[0])
            self.field_length = [0 for _ in xrange(length)] if need_updata_flg else self.field_length
            for item in source_data[1:]:
                if len(item) != length:
                    raise Exception('every item length  of source data  no equal!')
                elif need_updata_flg:
                    for i, field in enumerate(item, 0):
                        field_length = len(str(field))
                        if field_length > self.field_length[i]:
                            self.field_length[i] = field_length 


    def transform_to_format(self):
        def add_line_data(s, split_str, middle_data):
            for i in xrange(len(self.field_length)) :
                s += split_str
                s += middle_data[i]
            s += split_str + '\n'
            return s 
        
        def add_split_line(s):
            s = add_line_data(s, '+', ['-'* (lg + 2) for lg in self.field_length])
            
            return s

        # 开头
        s = ''
        s = add_split_line(s)
        
        # 数据
        for item in self.source_data:
            line_data = []
            for i, field_data in enumerate(item, 0):
                str_field_data = str(field_data)
                line_data.append(' ' + str_field_data + ' ' * (self.field_length[i] + 1 - len(str_field_data)))
            
            s = add_line_data(s, '|', line_data)
            s = add_split_line(s)
        
        # 结尾
        s += '===============>'
    
        return s 





        

