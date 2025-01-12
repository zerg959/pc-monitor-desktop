import sqlite3

DATABASE = 'sys_monitor.db'


def init_db():
    con = sqlite3.connect(DATABASE)
    con.execute("""
        CREATE TABLE IF NOT EXISTS sys_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpu_percent REAL,
            ram_percent REAL,
            ram_used REAL,
            ram_total REAL,
            disk_percent REAL,
            disk_used REAL,
            disk_total REAL,
            timestamp TEXT
        )
    """)
    return con


def insert_sys_data(data):
    con = init_db()
    cur = con.cursor()
    cur.execute('''
      INSERT INTO sys_data (
                cpu_percent,
                ram_percent,
                ram_used,
                ram_total,
                disk_percent,
                disk_used,
                disk_total,
                timestamp
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', (
            data['cpu_percent'],
            data['ram_percent'],
            data['ram_used'],
            data['ram_total'],
            data['disk_percent'],
            data['disk_used'],
            data['disk_total'],
            data['time'])
            )
    con.commit()
    con.close()


def db_records_list():
    con = init_db()
    cur = con.cursor()
    cur.execute('''SELECT * from sys_data''')
    rows = cur.fetchall()
    con.close()
    return rows
