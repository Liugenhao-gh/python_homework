import pymysql
class note:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost', user='root', password='lgh1519', db='test')
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e.__context__)
            self.cur.close()
            self.conn.close()

    def add(self):
        message = input('输入留言信息：')
        name = input('输入名字：')
        sql = 'INSERT INTO leave_note (message, name, is_delete) VALUES (\'{}\', \'{}\', 0)'.format(message,name)
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            return
        else:
            print('添加成功！')

    def select_by_sth(self):
        index = input('''你想根据什么查询？
        ID 1、
        留言 2、
        名字 3、
        ''')
        if index == '1':
            id = input('输入要查询的id:')
            sql = 'select * from leave_note where id ={}'.format(int(id))
        elif index == '2':
            message = input('输入要查询的留言')
            sql = 'select * from leave_note where message=\'{}\''.format(message)
        elif index == '3':
            name = input('输入要查询的名字')
            sql = 'select * from leave_note where name=\'{}\''.format(name)
        else:
            print('没有这个选项')
            return
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            return
        else:
            for r in self.cur:
                print(r)

    def delete(self):
        index = input('''
你想根据什么删除？
ID 1、
留言 2、
名字 3、
                ''')
        if index == '1':
            id = input('输入要删除的id:')
            sql = 'delete  from leave_note where id ={}'.format(int(id))
        elif index == '2':
            message = input('输入要删除的留言')
            sql = 'delete  from leave_note where message=\'{}\''.format(message)
        elif index == '3':
            name = input('输入要删除的名字')
            sql = 'delete from leave_note where name=\'{}\''.format(name)
        else:
            print('没有这个选项')
            return
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            return
        else:
            print('删除成功！')

    def update(self):
        id = input('输入要修改项目的id：')
        message = input('输如修改后的留言')
        name = input('输入修改后的名字：')
        sql = 'update leave_note set message = \'{}\' , name = \'{}\' where id = \'{}\''.format(message, name,int(id))
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            return
        else:
            print('更新成功！')

    def close(self):
        self.cur.close()
        self.conn.close()
if __name__ == '__main__':
    n = note()
    n.update()
    n.close()

