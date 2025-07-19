# nama : al-zastrouw mulla sadra
# nim : 241080200052
# semester/kelas : 2A1

import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")
k = koneksi_ke_DB.cursor()

k.execute("""
    UPDATE TBCars SET
        price = 20000
    WHERE
        id = 101
""")
print(k.fetchall())

koneksi_ke_DB.commit()
koneksi_ke_DB.close()