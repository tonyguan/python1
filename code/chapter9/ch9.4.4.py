# coding=utf-8
# 代码文件：chapter9/ch9.4.4.py

student_dict = {102: '张三', 105: '李四', 109: '王五'}

print('---遍历键---')
for student_id in student_dict.keys():
    print('学号：' + str(student_id))

print('---遍历值---')
for student_name in student_dict.values():
    print('学生：' + student_name)

print('---遍历键:值---')
for student_id, student_name in student_dict.items():
    print('学号：{0} - 学生：{1}'.format(student_id, student_name))
