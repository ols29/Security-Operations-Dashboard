import scapy.all as scapy
import datetime
import socket

scapy.conf.verb = 0

class Red29Monitor:
    def __init__(self, target_ip=None, interface=None):
        # Se não passar nada, ele detecta sozinho
        self.interface, self.target_ip = self.auto_discover(interface, target_ip)
        
        self.critical_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3389, 8080]
        self.found_vulnerabilities = 0

    def auto_discover(self, iface_manual, ip_manual):
        """Detecta automaticamente a interface de saída e a faixa de IP"""
        try:
            route = scapy.conf.route.route("8.8.8.8")
            
            final_iface = iface_manual if iface_manual else route[3]
            

            if not ip_manual:
                my_ip = route[1]
                base_ip = ".".join(my_ip.split('.')[:3]) + ".0/24"
                final_ip = base_ip
            else:
                final_ip = ip_manual

            print(f"\n[*] Configuração Automática Detectada:")
            print(f"    > Interface: {final_iface.name if hasattr(final_iface, 'name') else final_iface}")
            print(f"    > IP Local: {route[1]}")
            print(f"    > Alvo do Scan: {final_ip}")
            
            return final_iface, final_ip
            
        except Exception as e:
            print(f"[!] Erro na auto-detecção: {e}")
            return scapy.conf.iface, "192.168.0.1/24"

    def scan_network(self):
        print(f"\n--- Iniciando Scan Sentinel-29 ---")
        
        try:
            arp_request = scapy.ARP(pdst=self.target_ip)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = broadcast/arp_request
            
            
            answered = scapy.srp(packet, timeout=2, verbose=False, iface=self.interface)[0]

            print(f"[+] Dispositivos ativos encontrados: {len(answered)}")
            return answered
            
        except Exception as e:
            print(f"[ERROR] Falha crítica no Scan: {e}")
            print("Dica: Verifique se o Npcap está instalado em modo 'WinPcap compatible'.")
            return []

    def port_check(self, ip):
        print(f"[*] Verificando vulnerabilidades no IP: {ip}")
        for port in self.critical_ports:
            try:
                
                syn_packet = scapy.IP(dst=ip)/scapy.TCP(dport=port, flags="S")
                resp = scapy.sr1(syn_packet, timeout=0.5, verbose=False, iface=self.interface)
                
                if resp:
                    
                    if resp.haslayer(scapy.TCP) and resp.getlayer(scapy.TCP).flags == 0x12:
                        print(f"   [ALERTA 🚨] Porta {port} ABERTA em {ip}")
                        self.found_vulnerabilities += 1
                        
                        
                        scapy.send(scapy.IP(dst=ip)/scapy.TCP(dport=port, flags="R"), verbose=False, iface=self.interface)
            except:
                pass

    def generate_birthday_report(self):
        now = datetime.datetime.now()
        print("\n" + "="*40)
        print(f"🛡️  RELATÓRIO SENTINEL-29")
        print(f"Data: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Ameaças Detectadas: {self.found_vulnerabilities}")
        print("="*40)

if __name__ == "__main__":

    monitor = Red29Monitor()
    
    devices = monitor.scan_network()
    
    if devices:
        target = devices[0][1].psrc
        print(f"\n[TESTE] Iniciando Port Scan no alvo: {target}")
        monitor.port_check(target)
    else:
        print("\n[!] Nenhum dispositivo encontrado na rede.")

    monitor.generate_birthday_report()