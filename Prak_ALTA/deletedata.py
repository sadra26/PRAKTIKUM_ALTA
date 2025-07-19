# nama : al-zastrouw mulla sadra
# nim : 241080200052
# semester/kelas : 2A1

import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")
k = koneksi_ke_DB.cursor()

k.execute("""
    DELETE FROM TBCars
    WHERE
        id = 102
""")
print(k.fetchall())

koneksi_ke_DB.commit()
koneksi_ke_DB.close()