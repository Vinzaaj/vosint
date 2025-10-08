# 🔥 VOSINT - Ultimate OSINT BY VINZAA

<div align="center">

![Vosint Banner](https://img.shields.io/badge/VOSINT-ULTIMATE%20OSINT-red)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Termux](https://img.shields.io/badge/Termux-Compatible-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

## 🌟 Features

### 🔍 Intelligence Gathering
- **Social Media Intelligence** (30+ platforms)
- **Domain & DNS Analysis** 
- **IP Geolocation & Threat Intel**
- **Phone Number Intelligence**
- **Email Verification & Breach Check**
- **Cryptocurrency Investigation**
- **Image Metadata & Reverse Search**
- **Dark Web Monitoring** (Basic)
- **Vulnerability Assessment**

### 🛠 Technical Features
- **Async Scanning** for speed
- **Multi-format Export** (JSON, HTML, PDF, TXT)
- **Real-time Monitoring**
- **API Integration** (VirusTotal, Shodan, etc.)
- **Custom Reporting**
- **Batch Processing**

## 🚀 Quick Start

### Termux Installation
```bash
# Update system
pkg update && pkg upgrade

# Install dependencies
pkg install python git libxml2 libxslt

# Clone repository
git clone https://github.com/yourusername/vosint.git
cd vosint

# Install Python packages
pip install -r requirements.txt

# Run Vosint
python vosint.py -h

# Install with all features
chmod +x install.sh
./install.sh

# Comprehensive target scan
python vosint.py -t target.com --full

# Social media reconnaissance
python vosint.py -s username --deep

# Domain intelligence
python vosint.py -d example.com --dns --whois --subdomains

# Phone number analysis
python vosint.py -p +628123456789 --carrier --location

# Image investigation
python vosint.py -i image.jpg --metadata --reverse-search

# Dark web monitoring
python vosint.py -t "query" --darkweb

# Generate report
python vosint.py -t target.com --html-report

Output Formats

JSON: Machine-readable

HTML: Interactive reports

PDF: Professional documentation

• TXT: Simple text format

CSV: Spreadsheet compatible

▲ Legal Disclaimer

This tool is for:

Educational purposes

Authorized penetration testing

Security research

Legal investigations

Never use for illegal activities!
