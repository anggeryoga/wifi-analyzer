
---

## 📂 **3. Buat File Install Otomatis (`install.sh`)**  
Biar pengguna bisa install lebih cepat, buat file `install.sh` di GitHub dan **paste ini**:  

```sh
#!/bin/bash

echo "🚀 Installing dependencies..."
pkg update -y && pkg upgrade -y
pkg install python termux-api git -y
pip install speedtest-cli rich

echo "✅ Installation complete!"
echo "Ketik 'python wifi-analyzer.py' untuk menjalankan tools ini."
