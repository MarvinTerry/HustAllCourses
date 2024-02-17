import sqlite3

def create_db(db_name):
    # 连接数据库
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # 创建表结构（如果尚不存在）
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses
                      (KTBH TEXT UNIQUE, KCBH TEXT, KCMC TEXT, KTMC TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS course_details
                      (KTBH TEXT, KCMC TEXT, XM TEXT, JSMC TEXT, XQ TEXT, QSJC TEXT, JSJC TEXT, QSZC INT, JSZC INT, KTMC TEXT,
                      FOREIGN KEY(KTBH) REFERENCES courses(KTBH))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS s_keywords
                      (S_KEY TEXT)''')

def keyword_usability(db_name, keyword) -> bool:
    # 连接数据库
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # 查重：检查S_KEY是否已存在
    cursor.execute('SELECT S_KEY FROM s_keywords WHERE S_KEY = ?', (keyword,))
    if cursor.fetchone():
        print('关键字 {} 已存在'.format(keyword))
        return False
    else:
        print('关键字 {} 正在搜索'.format(keyword))
        return True
    
def keyword_markon(db_name, keyword):
    # 连接数据库
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO s_keywords (S_KEY) VALUES (?)',(keyword,))
    conn.commit()
    conn.close()

def insert_course_into_db(db_name, data:dict):
    # 连接数据库
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # 查重：检查KTBH是否已存在
    cursor.execute('SELECT KTBH FROM courses WHERE KTBH = ?', (data['KTBH'],))
    if not cursor.fetchone():
        # 插入主表（courses）
        cursor.execute('INSERT INTO courses (KTBH, KCBH, KCMC, KTMC) VALUES (?, ?, ?, ?)',
                       (data['KTBH'], data['KCBH'], data['KCMC'], data['KTMC']))
        
        # 插入从表（course_details）
        for tr in data['tr']:
            cursor.execute('INSERT INTO course_details (KTBH, KCMC, XM, JSMC, XQ, QSJC, JSJC, QSZC, JSZC, KTMC) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (data['KTBH'], data['KCMC'], tr['XM'], tr['JSMC'], tr['XQ'], tr['QSJC'], tr['JSJC'], tr['QSZC'], tr['JSZC'], data['KTMC']))
        
        # 提交事务
        conn.commit()
        print('{} {}已插入。'.format(data['KCMC'], data['KTBH']))
    
    else:
        print('{} {}已存在，跳过插入。'.format(data['KCMC'], data['KTBH']))

    # 关闭数据库连接
    conn.close()

# 示例JSON数据
json_data_1 = '''
{
    "ROWZ":1577,
    "KTBH":"20231w9027460011",
    "KTMC":"传统武术（三） - 课堂",
    "KCBH":"w902746",
    "KCMC":"传统武术（三）",
    "ktbh":"20231w9027460011",
    "tr":[
        {
            "JSZC":17,
            "JSJC":"6",
            "XM":"周伟章",
            "XQ":"星期五",
            "XQS":"5",
            "QSZC":4,
            "JSMC":"中心操场",
            "QSJC":"5"
        }
    ]
}
'''


json_data_2 = '''
{
    "ROWZ":1254,
    "KTBH":"20231w10745298",
    "KTMC":"临床医学类2301班",
    "KCBH":"w107452",
    "KCMC":"综合英语（一）",
    "ktbh":"20231w10745298",
    "tr":[
        {
            "JSZC":17,
            "JSJC":"6",
            "XM":"龚茜",
            "XQ":"星期一",
            "XQS":"1",
            "QSZC":4,
            "JSMC":"东九楼D216",
            "QSJC":"5"
        },
        {
            "JSZC":17,
            "JSJC":"4",
            "XM":"龚茜",
            "XQ":"星期三",
            "XQS":"3",
            "QSZC":4,
            "JSMC":"东九楼D216",
            "QSJC":"3"
        }
    ]
}
'''


