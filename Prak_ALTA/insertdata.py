# nama : al-zastrouw mulla sadra
# nim : 241080200052
# semester/kelas : 2A1

import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")
k = koneksi_ke_DB.cursor()

k.execute("""
    INSERT INTO TBCars (
        id,
        name,
        brand,
        model,
        price
    ) VALUES (
        '101',
        'Red Car',
        'Honda',
        'CRV',
        12000
    ), 
    (
        '102',
        'Black Car',
        'Honda',
        'City',
        15000
    )
""")

koneksi_ke_DB.commit()
koneksi_ke_DB.close()
