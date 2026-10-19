Linux Security Audit & Hardening Tool 🐧🛡️

Uma ferramenta leve desenvolvida em Python para automatizar verificações de segurança e auditoria de permissões em sistemas Linux.

## 📌 O que este projeto faz?
No dia a dia de um analista de segurança (Blue Team) ou Administrador de Sistemas, garantir que os ficheiros críticos do sistema operacional não estejam expostos é fundamental. Este script realiza:
1. **Auditoria de Ficheiros Sensíveis:** Verifica o estado e as permissões de acesso de ficheiros críticos do sistema (como `/etc/passwd` e `/etc/shadow`).
2. **Varredura de Riscos (Permissões 777):** Faz uma busca recursiva no diretório de trabalho à procura de ficheiros com permissões totalmente abertas (`777`), que representam brechas críticas de segurança.
3. **Geração Automática de Relatório:** Compila todos os achados num relatório detalhado (`report_linux.txt`) com carimbo de data e hora.

## 🚀 Como Executar

Certifica-te de ter o Python 3 instalado e corre o script no terminal:

```bash
python3 linux_audit.py
------------------------------------------------------------
     LINUX SECURITY AUDIT TOOL - HARDENING CHECKER
------------------------------------------------------------
[+] Arquivo verificado: /etc/passwd | Permissões: 644
[+] Arquivo verificado: /etc/shadow | Permissões: 600
[+] Analisando arquivos com permissões totalmente abertas (777)...
[✓] Nenhum arquivo com permissão 777 encontrado na pasta analisada.
------------------------------------------------------------
Auditoria concluída com sucesso! Relatório salvo em 'report_linux.txt'.
------------------------------------------------------------
