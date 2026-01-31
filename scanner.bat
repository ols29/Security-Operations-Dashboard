@echo off

chcp 65001 > nul
title SOC-BIRTHDAY SECURITY CONSOLE - STARTUP
color 0A


net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERRO] Por favor, clique com o botão direito e "Executar como Administrador".
    pause
    exit
)


pushd "%~dp0"

echo ==========================================
echo    PROJECT DASHBOARD // SOC MONITORING
echo    SISTEMA ESPECIAL DE ANIVERSÁRIO - 29/01/2026
echo ==========================================
echo [DIRETÓRIO ATUAL]: %CD%


set PYTHON_EXE="C:\Users\oliver.csantos\AppData\Local\Microsoft\WindowsApps\python.exe"


start http://localhost:2929


echo [INFO] Iniciando Servidor Backend...
%PYTHON_EXE% app.py

if %errorLevel% neq 0 (
    echo.
    echo [ERRO FATAL] O Python não conseguiu iniciar o servidor.
    echo Verifique se o app.py está nesta pasta: %CD%
)

pause