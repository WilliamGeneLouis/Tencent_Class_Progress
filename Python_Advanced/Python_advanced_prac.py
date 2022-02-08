class People:
    my_name = 'None'

    def __init__(self, name, age):
        self.my_name = name
        self.my_age = age
        # 此时并没有事前定义 my_age 函数，相当于在此时创建了一个 my_age 函数
        #

    def func(self, opinion):
        return 'my opinion is : ' + opinion


student = People('william', 19)

print(student.func('spider man (Amazing By Andrew)'))

print(student.my_age)

print(student.my_name)

print(People.my_name)


class Student(People):
    # 添加People类到Student类中
    def __init__(self, name, age, curriculum):
        super(Student, self).__init__(name, age)
        # 此时相当于在Student类直接使用People中的构造函数
        self.curriculum = curriculum

    def func2(self, opinion, time):
        return 'my opinion is : ' + opinion + time



# print(student.opinion)  AttributeError: 'People' object has no attribute 'opinion'

# student.my_name = 'william'
# print(student.my_name)
# print(student.func('william'))
#
# print(dir(1))
# print(dir(student))

#  类中构建构造函数，该方法在类实例化时会自动调用

# def __init__ (self):
#     self.data = []
#
# def __init__(self, name,id):     __init__ 可以添加参数
#     self.data = []
#     print('my name {}, my id {}'.format(name, id))
