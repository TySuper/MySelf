import pymysql


class UseMysql():
    def __init__(self, ip, user, password, database='school'):
        """
        连接mysql数据库,并配置数据库指针
        :param ip: 数据库地址
        :param user: 用户名
        :param password: 密码
        :param database: 所使用的数据库
        """
        config = {
            'host': ip,
            'port': 3306,
            'user': user,
            'passwd': password,
            'db': database,
            'charset': 'utf8'
        }
        self.db = pymysql.connect(**config)
        self.cursor = self.db.cursor()

    def create_table(self, sql):
        """
        创建表
        :param sql: 创表语句
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f"请留意你的SQL语句是否正确:{e}")

    def fetchall(self, sql):
        """
        查询多条数据
        :param sql:
        :return:查询的值
        """
        # 执行sql语句
        self.cursor.execute(sql)
        # 通过fetchall获取所有的查询值
        results = self.cursor.fetchall()
        return results

    def fetchone(self, sql):
        """
        查询获取单条数据：
        使用execute()方法执行SQL语句，
        使用fetchone()方法获取单条数据；
        :param sql:
        :return: 查询值
        """
        self.cursor.execute(sql)
        results = self.cursor.fetchone()
        return results

    def execute(self, sql):
        """
        添加,删除,更新操作
        使用execute()方法执行SQL语句，
        提交到数据库执行，发生错误时回滚；
        :param sql: 
        :return: 
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f"请留意你的SQL语句是否正确:{e}")


if __name__ == '__main__':
    operate = UseMysql("192.168.170.140", "root", "abc@123")
    # sql = """CREATE TABLE IF NOT EXISTS student_score(sid INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    #                                                          sname VARCHAR (20) NOT NULL,
    #                                                          sdept VARCHAR (20) NOT NULL,
    #                                                          chinese FLOAT(5,2) NOT NULL,
    #                                                          math FLOAT(5,2) NOT NULL,
    #                                                          englist FLOAT(5,2) NOT NULL,
    #                                                          average_score FLOAT(5,2) NOT NULL,
    #                                                          classmate_score FLOAT(5,2) NOT NULL,
    #                                                          teacher_score FLOAT(5,2) NOT NULL,
    #                                                          total_score FLOAT(5,2) NOT NULL
    #        )ENGINE =Innodb default charset =utf8
    #        """
    c_name_v = ['英语', '数学', '语文', '政治', '地理', '化学', '物理']
    sql = "insert into course (c_name) values ('化学')"
    operate.execute(sql)
