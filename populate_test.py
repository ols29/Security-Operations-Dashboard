import sqlite3
from datetime import datetime

def test_populate():
    conn = sqlite3.connect('network_db.db')
    cursor = conn.cursor()
    
    
    for i in range(1, 30):
        status = "ALERTA: ABERTA" if i % 5 == 0 else "Seguro"
        cursor.execute("INSERT INTO logs (timestamp, ip, port, status) VALUES (?, ?, ?, ?)",
                       (datetime.now().strftime("%H:%M:%S"), f"192.168.1.{i}", 80 + i, status))
    
    conn.commit()
    conn.close()
    print("29 logs de teste inseridos com sucesso!")

test_populate()