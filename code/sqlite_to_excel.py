import pandas as pd
import sqlite3

# SQLite数据库文件路径
database_path = 'hust_courses.db'
# 要导出的表格名称列表
tables_to_export = ['courses', 'course_details']
# 输出的Excel文件名
excel_file = 'hust_courses.xlsx'

# 创建数据库连接
conn = sqlite3.connect(database_path)

# 使用pandas的ExcelWriter，设置引擎为openpyxl
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    for table_name in tables_to_export:
        # 从数据库读取表格
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        # 将数据帧写入Excel文件的不同工作表中
        df.to_excel(writer, sheet_name=table_name, index=False)

    # 保存Excel文件
    # writer._save()

# 关闭数据库连接
conn.close()

print(f"表格已成功导出到'{excel_file}'。")
