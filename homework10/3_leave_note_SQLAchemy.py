from  sqlalchemy import create_engine, String, Integer, Column, Date ,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import pymysql
db_name = 'mysql+mysqlconnector://root:lgh1519@localhost:3306/test'
Base = declarative_base() # 基类
engine = create_engine(db_name, echo=False)
session_maker = sessionmaker(bind=engine)
session = session_maker()
class Note(Base):
    __tablename__ = 'leave_note'
    id = Column('id', Integer, primary_key=True)
    message = Column('message', String, nullable='False')
    name = Column('name', String, nullable='False')
    date = Column('date', Date, nullable='False')
    is_delete = Column('is_delete', Boolean)

# 增
def add(session):
    note = input('输入留言：')
    name = input('输入名字：')
    d_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        tex = Note(name=name, message=note, date=d_time, is_delete=0)
        session.add(tex)
        session.commit()
        # session.close()
    except Exception as e:
        print(e)
# 删
def delete(session):
    id = input('输入你想删除留言的id:')
    try:
        note_is_delete = session.query(Note).filter_by(id=id).first()
        session.delete(note_is_delete)
        session.commit()
    except Exception as e:
        print(e)

# 查

def find(session):
    id = input('输入你想查询的id:')
    try:
        note = session.query(Note).filter_by(id=id).first()
        print('id : {}; name : {}; note : {}; date : {}; is_delete : {}'.format(note.id, note.name,note.message, note.date, note.is_delete))
    except Exception as e:
        print(e)

# 改
def change(session):
    id = input('输入你想修改的id:')
    note = input('输入修改后的留言：')
    name = input('输入修改后的名字：')
    try:
        note_result = session.query(Note).filter_by(id= id).first()
        note_result.message = note
        note_result.name = name
        session.commit()
    except Exception as e:
        print(e)
if __name__ == '__main__':
    find(session)
    # change(session)

