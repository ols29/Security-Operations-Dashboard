from flask import Flask, render_template, jsonify
import scapy.all as scapy
import sqlite3
import threading
import time
import socket
import os
import sys
import subprocess
from datetime import datetime


base_path = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_path, 'templates')
db_path = os.path.join(base_path, 'network_db.db')

app = Flask(__name__, template_folder=template_dir)

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       timestamp TEXT, ip TEXT, port INTEGER, status TEXT)''')
    conn.commit()
    conn.close()

def hacker_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

PORTS_29 = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 
            1723, 3306, 3389, 5432, 5900, 8080, 8443, 1433, 27017, 1521, 
            6379, 5000, 3000, 161, 162]

def scan_task():

    scapy.conf.iface = scapy.conf.iface
    my_ip = get_my_ip()
    while True:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            for port in PORTS_29:
                syn_pkt = scapy.IP(dst=my_ip)/scapy.TCP(dport=port, flags="S")
                res = scapy.sr1(syn_pkt, timeout=0.2, verbose=False)
                
                status = "Seguro (Fechada)"
                if res and res.haslayer(scapy.TCP):
                    if res.getlayer(scapy.TCP).flags == 0x12:
                        status = "ALERTA: ABERTA"
                        scapy.send(scapy.IP(dst=my_ip)/scapy.TCP(dport=port, flags="R"), verbose=False)

                cursor.execute("INSERT INTO logs (timestamp, ip, port, status) VALUES (?, ?, ?, ?)",
                               (datetime.now().strftime("%H:%M:%S"), my_ip, port, status))
            
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Monitor erro: {e}")
        
        time.sleep(29)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/logs')
def get_logs():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 29")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/api/generate_report')
def generate_report_route():
    try:

        report_script = os.path.join(base_path, "geratorreport_gen.py")
        subprocess.run([sys.executable, report_script], check=True)
        return jsonify({"status": "success", "message": "Relatorio PDF gerado com sucesso!"})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Erro interno: {str(e)}"}), 500

if __name__ == '__main__':
    init_db()
    hacker_print("\n" + "="*50)
    hacker_print(">>> SECURITY OPERATIONS CENTER THE SPECIAL SYSTEM")
    hacker_print(f">>> TARGET_IP: {get_my_ip()}")
    hacker_print(">>> DASHBOARD: http://localhost:2929")
    hacker_print("="*50 + "\n")
    
    threading.Thread(target=scan_task, daemon=True).start()
    app.run(debug=False, port=2929)