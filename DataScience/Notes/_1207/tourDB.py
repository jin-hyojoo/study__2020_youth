import pymysql as p

class TourDB:
    def __init__(self):
        self.db_init()
    def db_init(self):
        self.conn = p.connect(host='localhost', port=3306,
                              user='root', password='1234',
                              db='pythonDB', charset='utf8')

    def db_free(self):
        if self.conn:
            self.conn.close()

    def tour_crawlingInsert(self, title, price, term, area):
        sql = ''' insert into tour_crawling(title, price, term, area)
              values(%s, %s, %s, %s);  '''
        with self.conn.cursor() as cursor:
            cursor.execute(sql, (title, price, term, area))
        self.conn.commit()


if __name__ == "__main__":
    db = TourDB()
    db.tour_crawlingInsert('test', '10000원','1228-2200', '도시')
    db.db_free()
    