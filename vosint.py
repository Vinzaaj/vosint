#!/usr/bin/env python3
"""
VOSINT - Termux OSINT Toolkit
Author: Vinzaa
Version: 1.1
"""

import argparse
import json
import sys
import os
from datetime import datetime
from modules.social import SocialScanner
from modules.domain import DomainScanner
from modules.network import NetworkScanner

class Vosint:
    def __init__(self):
        self.banner = """
\033[91m
███████╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔════╝██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
█████╗  ██║   ██║███████╗██║██╔██╗ ██║   ██║   
██╔══╝  ██║   ██║╚════██║██║██║╚██╗██║   ██║   
██║     ╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═╝      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
\033[0m
\033[93m           TERMUX OSINT TOOLKIT v1.0\033[0m
\033[94m        Created for Educational Purposes\033[0m
"""
        
        self.social_scanner = SocialScanner()
        self.domain_scanner = DomainScanner()
        self.network_scanner = NetworkScanner()
    
    def print_banner(self):
        """Display awesome banner"""
        print(self.banner)
        print(f"\033[92m[+] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m")
        print(f"\033[92m[+] Running on: {os.uname().sysname}\033[0m\n")
    
    def save_results(self, data, filename=None):
        """Save results to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"vosint_results_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\033[92m[+] Results saved to: {filename}\033[0m")
        return filename

def main():
    vosint = Vosint()
    
    parser = argparse.ArgumentParser(description='VOSINT - Termux OSINT Toolkit')
    parser.add_argument('-s', '--social', help='Social media username scan')
    parser.add_argument('-i', '--ip', help='IP address lookup')
    parser.add_argument('-d', '--domain', help='Domain information')
    parser.add_argument('-p', '--phone', help='Phone number lookup')
    parser.add_argument('-u', '--url', help='Website reconnaissance')
    parser.add_argument('-o', '--output', help='Output file name')
    
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        vosint.print_banner()
        parser.print_help()
        return
    
    try:
        results = {}
        vosint.print_banner()
        
        if args.social:
            print(f"\033[93m[+] Scanning social media for: {args.social}\033[0m")
            results['social_media'] = vosint.social_scanner.scan(args.social)
        
        if args.ip:
            print(f"\033[93m[+] Looking up IP address: {args.ip}\033[0m")
            results['ip_lookup'] = vosint.network_scanner.ip_lookup(args.ip)
        
        if args.domain:
            print(f"\033[93m[+] Analyzing domain: {args.domain}\033[0m")
            results['domain_info'] = vosint.domain_scanner.analyze(args.domain)
        
        if args.phone:
            print(f"\033[93m[+] Looking up phone number: {args.phone}\033[0m")
            results['phone_lookup'] = vosint.network_scanner.phone_lookup(args.phone)
        
        if args.url:
            print(f"\033[93m[+] Scanning website: {args.url}\033[0m")
            results['website_scan'] = vosint.domain_scanner.website_scan(args.url)
        
        # Save results
        if results:
            vosint.save_results(results, args.output)
            
            # Print summary
            print(f"\n\033[92m[✓] Scan completed! Collected {len(results)} data categories\033[0m")
        else:
            print("\033[91m[!] No results collected. Check your arguments.\033[0m")
            
    except KeyboardInterrupt:
        print(f"\n\033[91m[!] Scan interrupted by user\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error: {str(e)}\033[0m")

if __name__ == "__main__":
    main()
