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
            # SQL建表语句
            sql = "insert into tb_college (colname) values('机械学院')"
            cursor.execute(sql)
            # 事务提交。如果你执行了修改数据库的操作（如INSERT、UPDATE、DELETE），你需要调用连接对象的commit()方法来提交这些更改。
            conn.commit()

    except pymysql.MySQLError as e:
        print(f'数据库操作失败：{e}')
        # 发生异常进行回滚
        if conn:
            conn.rollback()
    # 捕获除数据库操作之外的大部分异常
    except Exception as e:
        print(f'发生错误:{e}')
        if conn:
            conn.rollback()
    finally:
        # 关闭数据库连接
        if conn:
            conn.close()
            print('MySQL连接已关闭')


if __name__ == '__main__':
    main()
