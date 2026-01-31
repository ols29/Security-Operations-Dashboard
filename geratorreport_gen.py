import sqlite3
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, 'network_db.db')

def generate_pdf():
    pdf_file = f"Relatorio_SOC_Red29_{datetime.now().strftime('%Y%m%d')}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "RELATÓRIO DE SEGURANÇA - PROJECT RED-29")
    c.setFont("Helvetica", 10)
    c.drawString(50, 735, f"Analista: Oliver Santos (ols29) | Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    c.line(50, 730, 550, 730)


    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, ip, port, status FROM logs ORDER BY id DESC LIMIT 30")
    logs = cursor.fetchall()
    conn.close()

    y = 700
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "Hora")
    c.drawString(120, y, "IP de Origem")
    c.drawString(220, y, "Porta")
    c.drawString(280, y, "Status de Segurança")
    
    y -= 20
    c.setFont("Helvetica", 9)
    for log in logs:
        if y < 50:
            c.showPage()
            y = 750
        

        if "ALERTA" in log[3]:
            c.setFillColorRGB(0.7, 0, 0)
        else:
            c.setFillColorRGB(0, 0, 0)
            
        c.drawString(50, y, str(log[0]))
        c.drawString(120, y, str(log[1]))
        c.drawString(220, y, str(log[2]))
        c.drawString(280, y, str(log[3]))
        y -= 15

    c.save()
    print(f"\n[SUCESSO] Relatório gerado: {pdf_file}")

if __name__ == '__main__':
    generate_pdf()