from web_query import query_courses
from database_inject import keyword_usability, insert_course_into_db, create_db, keyword_markon

# 配置信息
db_name = 'hust_courses.db'
keywords_txt = './code/keywords.txt'
uname = 'U202XXXXX' # 修改为自己的账号
upass = 'XXXXXXXXX' # 修改为自己的密码

print('---本脚本通过 “我要蹭课” 功能爬取华科课程信息---')
print(f'---课程信息将存入SQLite数据库：{db_name}---')
print('---数据库文件可通过 sqlite_to_excel.py 转换为 Excel 文件---')

print(f'\n1) 通过关键词列表 {keywords_txt} 自动爬取')
print('2) 通过手动输入爬取')
method = input('请选择爬取方式：')

create_db(db_name)

if method == '1':
    with open(keywords_txt, 'r', encoding='utf-8') as f:
        for line in f:
            keyword = line.strip()
            if keyword_usability(db_name, keyword):
                course_list = query_courses(uname, upass, keyword)
                for data in course_list:
                    insert_course_into_db(db_name, data)
                print('***包含 {} 的{}门课程已全部插入成功。***'.format(keyword,len(course_list)))
                keyword_markon(db_name, keyword)
            
if method == '2':
    while True:
        keyword = input('请输入课程关键字：')
        if keyword_usability(db_name, keyword):
            course_list = query_courses(uname, upass, keyword)
            for data in course_list:
                insert_course_into_db(db_name, data)
            print('***包含 {} 的{}门课程已全部插入成功。***'.format(keyword,len(course_list)))
            keyword_markon(db_name, keyword)
