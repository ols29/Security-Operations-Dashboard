@echo off
color 0A
title Sentinel-29 SOC Monitor
cls

cd /d "%~dp0"

echo ==================================================
echo   SENTINEL-29 SECURITY OPERATIONS DASHBOARD
echo   [SYSTEM STATUS: ONLINE]
echo ==================================================
echo.


net session >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERRO] PERMISSAO NEGADA!
    echo ---------------------------------------------------
    echo O Scapy precisa de acesso total a placa de rede.
    echo Por favor, clique com o botao DIREITO neste arquivo
    echo e selecione "Executar como Administrador".
    echo ---------------------------------------------------
    pause
    exit
)

python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Python nao encontrado! Instale e marque "Add to PATH".
    pause
    exit
)


python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Dependencias nao encontradas.
    echo [*] Instalando automaticamente via requirements.txt...
    
    pip install -r requirements.txt
    
    if %errorlevel% neq 0 (
        color 0C
        echo [ERROR] Falha ao instalar dependencias. Verifique sua internet.
        pause
        exit
    )
    echo [OK] Tudo instalado com sucesso!
    echo.
)


echo [SUCCESS] Starting Dashboard...
echo [INFO] Access via browser at http://localhost:2929
echo.
python app.py

pause