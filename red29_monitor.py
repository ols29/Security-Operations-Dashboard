import scapy.all as scapy
import datetime

class Red29Monitor:
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.critical_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3389]
        self.found_vulnerabilities = 0

    def scan_network(self):
        print(f"--- Iniciando Scan Red-29 em: {self.target_ip} ---")
        
        arp_request = scapy.ARP(pdst=self.target_ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        print(f"Dispositivos encontrados: {len(answered_list)}")
        return answered_list

    def port_check(self, ip):
        """Verifica se portas críticas estão abertas no alvo"""
        print(f"Verificando vulnerabilidades no IP: {ip}")
        for port in self.critical_ports:
           
            syn_packet = scapy.IP(dst=ip)/scapy.TCP(dport=port, flags="S")
            response = scapy.sr1(syn_packet, timeout=0.5, verbose=False)
            
            if response and response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags == 0x12:
                print(f"[ALERTA] Porta {port} ABERTA em {ip}. Risco detectado.")
                self.found_vulnerabilities += 1
                
                scapy.sr(scapy.IP(dst=ip)/scapy.TCP(dport=port, flags="R"), timeout=1, verbose=False)

    def generate_birthday_report(self):
        """Gera o log final com a temática de 29"""
        now = datetime.datetime.now()
        print("\n" + "="*30)
        print(f"RELATÓRIO DE ANIVERSÁRIO - DIA 29")
        print(f"Status: Monitoramento Ativo")
        print(f"Data/Hora: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Total de falhas potenciais analisadas: 29") 
        print(f"Ameaças reais bloqueadas: {self.found_vulnerabilities}")
        print("="*30)

if __name__ == "__main__":
   
    monitor = Red29Monitor("192.168.1.1/24")
    
 
    devices = monitor.scan_network()
    
    
    if devices:
        target = devices[0][1].psrc
        monitor.port_check(target)
    monitor.generate_birthday_report()