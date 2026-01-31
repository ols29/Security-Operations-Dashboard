## Security Operations Dashboard // Special Birthday

O Sentinel-29 é um dashboard de monitoramento de rede em tempo real desenvolvido como prova de conceito (PoC) para segurança cibernética. O sistema realiza varreduras ativas e análise de tráfego para identificação de portas abertas e possíveis vulnerabilidades. 

## Funcionalidades
Monitoramento de Rede: Scan de portas críticas utilizando a técnica TCP SYN com a biblioteca Scapy.

Dashboard em Tempo Real: Interface web dinâmica para visualização de tráfego e métricas de ameaças.

Persistência de Dados: Histórico de eventos e auditoria armazenado em banco de dados SQLite.

Geração de Relatórios: Exportação automática de logs de incidentes para formato PDF.

## Tecnologias
Linguagem: Python 3.13 (Flask, Scapy, ReportLab).

Banco de Dados: SQLite3.

Frontend: Tailwind CSS, jQuery (AJAX).

Automação: Windows Batch Scripting.

### Instalação e Uso ##
Instalar dependências:

Bash
pip install flask scapy reportlab
Executar o sistema (Como Administrador):

Bash
python app.py
Acessar o Painel: http://localhost:2929

## Autor
Oliver Santos (ols29)
Estudante de Eng.Software (PUCPR)