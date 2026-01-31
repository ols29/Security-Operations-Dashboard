<div align="center">

# 🛡️ Sentinel-29: Security Operations Dashboard
### Active Network Monitoring & Threat Detection System

![Version](https://img.shields.io/badge/Version-1.1.0_Stable-blue?style=flat&logo=semver)
![Status](https://img.shields.io/badge/Status-Operational-success?style=flat&logo=statuspage)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

<br>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
<img src="https://img.shields.io/badge/Scapy-Packet_Analysis-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/Windows_Batch-0078D6?style=for-the-badge&logo=windows&logoColor=white" />

</div>

---

## 📋 Sobre o Projeto

O **Sentinel-29** é uma plataforma de **SOC (Security Operations Center)** desenvolvida para monitoramento ativo de redes e detecção de vulnerabilidades.

Focado em **Blue Team Operations**, o sistema simula a rotina de um analista de segurança, automatizando a varredura de portas (SYN Scan), identificação de serviços críticos e auditoria de segurança.

---

## 🚀 Novas Funcionalidades (v1.1)

* **🧠 Smart Auto-Discovery:** O sistema agora detecta automaticamente a interface de rede ativa (Wi-Fi ou Ethernet) e calcula o range de IP da rede. **Zero configuração manual necessária.**
* **⚡ Auto-Healing Launcher:** O script de inicialização (`scanner.bat`) possui inteligência para:
    * Verificar e exigir privilégios de Administrador.
    * Detectar ausência de bibliotecas (Flask/Scapy).
    * Instalar dependências automaticamente via `requirements.txt` se necessário.
* **🕵️ Active Stealth Scanning:** Utiliza pacotes TCP SYN modificados para identificar portas abertas sem completar o handshake (técnica *Half-open*).
* **📄 Relatórios Executivos:** Geração automática de relatórios de incidente em PDF.

---

## ⚙️ Instalação e Execução

### 1. Pré-requisito Obrigatório (Windows)
O motor de scan (Scapy) exige um driver de captura de pacotes.
* Baixe o **[Npcap](https://npcap.com/#download)**.
* ⚠️ **IMPORTANTE:** Durante a instalação, marque a opção: **"Install Npcap in WinPcap API-compatible Mode"**.

### 2. Como Rodar (Modo Automático)
Basta clicar com o botão direito no arquivo **`scanner.bat`** e selecionar:
> **"Executar como Administrador"**

O script irá:
1.  Verificar seu ambiente Python.
2.  Instalar as dependências automaticamente (se faltarem).
3.  Detectar sua rede.
4.  Abrir o Dashboard no navegador.

### 3. Acesso
O painel estará disponível em:
👉 **http://localhost:2929**

---

## 🛠️ Solução de Problemas

| Erro Comum | Solução |
| :--- | :--- |
| **"Permissão Negada" / Scan falhou** | Você esqueceu de rodar o `scanner.bat` como **Administrador**. O Scapy precisa de acesso raw socket à placa de rede. |
| **WARNING: No libpcap provider** | O **Npcap** não está instalado ou a opção "WinPcap Mode" não foi marcada. Reinstale o Npcap. |
| **Erro de Interface (IP não encontrado)** | O Auto-Discovery falhou? Você pode forçar a interface editando o `red29_monitor.py` manualmente (mas é raro acontecer). |

---

## 👨‍💻 Autor

<div align="center">

**Oliver 'ols29' Casto**
<br>
*Analista de TI - JR| Eng.Software Student @ PUCPR*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ols29)

</div>
