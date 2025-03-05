import os
import json
import speedtest
import subprocess
from rich.console import Console
from rich.table import Table

console = Console()

# 🔍 Scan WiFi Terdekat
def scan_wifi():
    console.print("\n[cyan]🔍 Scanning WiFi...[/cyan]\n")
    result = os.popen("termux-wifi-scaninfo").read()
    try:
        wifi_data = json.loads(result)
        table = Table(title="📡 WiFi Analyzer", header_style="bold magenta")
        table.add_column("SSID", style="cyan", justify="left")
        table.add_column("MAC", style="green")
        table.add_column("Signal (dBm)", style="yellow")
        table.add_column("Channel", style="blue")
        table.add_column("Encryption", style="red")

        for wifi in wifi_data:
            ssid = wifi['ssid'] if wifi['ssid'] else "Hidden"
            mac = wifi['bssid']
            signal = str(wifi['rssi'])
            channel = str(wifi['frequency'])
            encryption = wifi['capabilities']
            table.add_row(ssid, mac, signal, channel, encryption)

        console.print(table)
    except json.JSONDecodeError:
        console.print("[red]❌ Gagal mendapatkan data WiFi. Pastikan Termux API sudah diinstal![/red]")

# 🌐 Cek Gateway & DNS
def check_network():
    console.print("\n[cyan]🌐 Mengecek Gateway & DNS...[/cyan]\n")
    gateway = os.popen("ip route | grep default | awk '{print $3}'").read().strip()
    dns = os.popen("getprop net.dns1").read().strip()
    console.print(f"🏠 [yellow]Gateway (Router):[/yellow] {gateway}")
    console.print(f"🌎 [green]DNS Server:[/green] {dns}")

# 🚀 Speed Test Internet
def speed_test():
    console.print("\n[cyan]🚀 Melakukan Speed Test...[/cyan]\n")
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    console.print(f"⬇️ [green]Download Speed:[/green] {download_speed:.2f} Mbps")
    console.print(f"⬆️ [yellow]Upload Speed:[/yellow] {upload_speed:.2f} Mbps")

# 📡 Ping Router & Google
def ping_test():
    console.print("\n[cyan]📡 Ping Router & Internet...[/cyan]\n")
    router_ping = subprocess.run(["ping", "-c", "3", "192.168.1.1"], capture_output=True, text=True)
    google_ping = subprocess.run(["ping", "-c", "3", "8.8.8.8"], capture_output=True, text=True)
    
    console.print("[yellow]📡 Ping ke Router:[/yellow]")
    console.print(router_ping.stdout)
    
    console.print("[green]🌍 Ping ke Google:[/green]")
    console.print(google_ping.stdout)

# 📂 Simpan Data ke File
def save_to_file():
    console.print("\n💾 [cyan]Menyimpan data WiFi ke file...[/cyan]")
    with open("wifi_report.txt", "w") as f:
        f.write("WiFi Analysis Report\n")
        f.write("===================\n")
        f.write(os.popen("termux-wifi-scaninfo").read())
    console.print("[green]✅ Data disimpan ke wifi_report.txt[/green]")

# 📌 Menu Utama
def main():
    while True:
        console.print("\n[bold magenta]📡 WiFi Analyzer - Termux[/bold magenta]")
        console.print("[1] 🔍 Scan WiFi Terdekat")
        console.print("[2] 🌐 Cek Gateway & DNS")
        console.print("[3] 🚀 Speed Test")
        console.print("[4] 📡 Ping Router & Google")
        console.print("[5] 💾 Simpan Data ke File")
        console.print("[0] ❌ Keluar")
        pilihan = input("\n🛠 Pilih menu: ")

        if pilihan == "1":
            scan_wifi()
        elif pilihan == "2":
            check_network()
        elif pilihan == "3":
            speed_test()
        elif pilihan == "4":
            ping_test()
        elif pilihan == "5":
            save_to_file()
        elif pilihan == "0":
            console.print("[red]❌ Keluar dari program...[/red]")
            break
        else:
            console.print("[red]❌ Pilihan tidak valid![/red]")

if __name__ == "__main__":
    main()
