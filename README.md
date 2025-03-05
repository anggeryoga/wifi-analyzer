# 📡 WiFi Analyzer (Termux)
Tools ini digunakan untuk menganalisis jaringan WiFi di Termux.

## 🚀 Fitur
✅ Scan WiFi terdekat (SSID, MAC, sinyal, enkripsi)  
✅ Cek kualitas sinyal (dBm)  
✅ Tampilkan Gateway & DNS  
✅ Speed Test otomatis  
✅ Ping Router & Google  

## 🔧 Cara Install & Jalankan
```sh
git clone https://github.com/username/wifi-analyzer.git
cd wifi-analyzer
pkg install python termux-api -y
pip install speedtest-cli rich
python wifi-analyzer.py
