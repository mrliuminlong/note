# student.py

# 此模块用于描述Student类的定义

class Student:
    def __init__(self, n, a, s=0):
        self.__name = n
        self.__age = a
        self.__score = s
    def get_infos(self):
        return (self.__name, str(self.__age), str(self.__score))

    def get_name(self):
        return self.__name

    def set_score(self, s):
        assert 0 <= s <= 100, '成绩不合法'
        self.__score = s

    def get_score(self):
        return self.__score

    def get_age(self):
        return self.__age

    def write_to_file(self, file):
        file.write(self.__name)
        file.write(' ')
        file.write(str(self.__age))
        file.write(' ')
        file.write(str(self.__score))
        file.write('\n')

