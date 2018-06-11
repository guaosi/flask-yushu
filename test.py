class Student:
    name="张1"
student1=Student()
print(student1.name)

a={
    '张三':15,
    '李四':16,
    '王五':17,
    '赵六':18
}
b=[key for key,val in a.items()] #作为列表返回
print(b)