''' 페리카나 데이터 DB에 저장'''
import pymysql as p

class PelicanaDB:
    def __init__(self):
        self.db_init()
    def db_init(self):
        self.conn = p.connect(host='localhost', port=3306,
                    user='root', password='1234',
                    db='pythonDB', charset='utf8')

    def db_free(self):
        if self.conn:
            self.conn.close()

    def pelicana_crawlingInsert(self, store, sido, gungu, address, phone):
        sql = """ insert into pelicana_crawling (store, sido, gungu, address, phone)
                   values(%s, %s, %s, %s, %s); """
        
        # with문은 자원 사용하고 반납할 때 많이 사용
        with self.conn.cursor() as cursor:
            cursor.execute(sql, (store, sido, gungu, address, phone))
        self.conn.commit()

if __name__ == '__main__':
    db= PelicanaDB()
    db.pelicana_crawlingInsert('test', 'test', 'test','test', '1234')
    db.db_free()