# @Time : 2024/7/3 21:37
# @Author : luoxin
import pymysql


def main():
    # 数据库连接参数
    db_config = {
        'host': 'db4free.net',
        'port': 3306,
        'user': 'hhpmmxobithcux',
        'password': '12345678',
        'database': 'study_tester',
        'charset': 'utf8mb4',  # 或者使用 'utf8' 根据你的数据库编码
        'cursorclass': pymysql.cursors.DictCursor  # 使用字典游标，这样返回的行就是字典格式
    }
    # 避免在数据库连接失败，进入except时，conn未被赋值；所以初始化conn
    conn = None
    # 连接数据库
    try:
        conn = pymysql.connect(**db_config)
        print('连接成功')

        # 使用cursor执行语句
        with conn.cursor() as cursor:
            # SQL查询语句，sql语句不需要commit操作
            sql = "select * from tb_student"
            cursor.execute(sql)

            # 获取所有记录；fetchone()获取一条；fetchmany()传入参数，获取指定的数据
            results = cursor.fetchall()
            print('results:', results)
            for row in results:
                print("每一行的值：", row)
    # 捕获大多数数据库异常
    except pymysql.MySQLError as e:
        print(f'数据库操作失败：{e}')

    # 捕获除数据库操作之外的大部分异常，select不需要回滚操作
    except Exception as e:
        print(f'发生错误:{e}')
    finally:
        # 关闭数据库连接
        if conn:
            conn.close()
            print('MySQL连接已关闭')


if __name__ == '__main__':
    main()
