from sqlite3 import dbapi2 as sqlite

con = sqlite.connect('test.db')
print (con.execute('select count (filename) from imlist').fetchone())
#(1000,)
print (con.execute('select * from imlist').fetchone())
#(u'ukbench00000.jpg',)