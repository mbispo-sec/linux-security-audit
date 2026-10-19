import os
import datetime

print("-" * 60)
print("     LINUX SECURITY AUDIT TOOL - INTERACTIVE HARDENING")
print("-" * 60)

# Entrada interativa: o usuário escolhe qual pasta quer auditar
target_dir = input("Digite o caminho da pasta que deseja auditar (ex: /etc, /var/log ou digite '.' para a pasta atual): ").strip()

# Se o usuário deixar vazio, assume a pasta atual
if not target_dir:
    target_dir = os.getcwd()

if not os.path.exists(target_dir):
    print(f"[!] Erro: O diretório '{target_dir}' não existe.")
    exit()

report_lines = []
report_lines.append("=" * 60)
report_lines.append("LINUX SECURITY AUDIT REPORT")
report_lines.append(f"Target Directory: {target_dir}")
report_lines.append(f"Generated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report_lines.append("=" * 60)

# 1. Checar arquivos críticos do sistema
critical_files = ["/etc/passwd", "/etc/shadow"]

for filepath in critical_files:
    if os.path.exists(filepath):
        try:
            file_perm = oct(os.stat(filepath).st_mode)[-3:]
            msg = f"[+] Arquivo verificado: {filepath} | Permissões: {file_perm}"
            print(msg)
            report_lines.append(msg)
            
            if filepath == "/etc/shadow" and file_perm != "600" and file_perm != "000":
                warning = f"  ⚠️ ALERTA: {filepath} está com permissão arriscada ({file_perm})!"
                print(warning)
                report_lines.append(warning)
        except PermissionError:
            msg = f"[-] Sem permissão para ler metadados de: {filepath} (execute com sudo se necessário)"
            print(msg)
            report_lines.append(msg)
    else:
        msg = f"[-] Arquivo não encontrado: {filepath}"
        print(msg)
        report_lines.append(msg)

# 2. Varredura dinâmica na pasta escolhida: procurar permissões perigosas 777
print(f"\n[+] Analisando arquivos com permissões totalmente abertas (777) em: {target_dir}...")
report_lines.append(f"\nDangerous Permissions Scan (777) in {target_dir}:")

risky_files_found = 0

for root, dirs, files in os.walk(target_dir):
    for file in files:
        full_path = os.path.join(root, file)
        try:
            mode = os.lstat(full_path).st_mode
            perm = oct(mode)[-3:]
            
            if perm == "777":
                alert = f"  ⚠️ PERIGO: O arquivo '{full_path}' está com permissão 777!"
                print(alert)
                report_lines.append(alert)
                risky_files_found += 1
        except (PermissionError, FileNotFoundError):
            pass

if risky_files_found == 0:
    msg = "[✓] Nenhum arquivo com permissão 777 encontrado no diretório analisado."
    print(msg)
    report_lines.append(msg)

# Salvar relatório automático em arquivo de texto
with open("report_linux.txt", "w") as f:
    f.write("\n".join(report_lines))

print("-" * 60)
print("Auditoria concluída com sucesso! Relatório salvo em 'report_linux.txt'.")
print("-" * 60)
