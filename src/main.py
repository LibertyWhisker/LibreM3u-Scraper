#!/usr/bin/env python3
"""
M3U Scraper - Main Application
Interactive IPTV playlist scraper with Xtreme portal support
"""

import os
import sys
import json
import getpass
from datetime import datetime
from typing import Dict, Optional
import logging

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import our scraper
from robust_iptv_scraper import RobustIPTVScraper

# Ensure logs directory exists
logs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
os.makedirs(logs_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(logs_dir, 'iptv_scraper.log')),
        logging.StreamHandler(sys.stdout)
    ]
)

class M3UScraperApp:
    def __init__(self):
        self.config_file = "scraper_config.json"
        self.saved_credentials = self.load_saved_credentials()
        
    def load_saved_credentials(self) -> Dict:
        """Load saved credentials from config file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logging.warning(f"Failed to load config: {e}")
        return {}
    
    def save_credentials(self, username: str, password: str, server: str):
        """Save credentials to config file"""
        config = {
            'username': username,
            'server': server,
            'last_used': datetime.now().isoformat()
        }
        # Note: We don't save the password for security reasons
        
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            logging.info("Credentials saved (password not stored for security)")
        except Exception as e:
            logging.warning(f"Failed to save config: {e}")
    
    def print_banner(self):
        """Print application banner"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                    M3U Scraper v1.0                          ║
║              IPTV Playlist Generator                          ║
║                                                              ║
║  Extract M3U playlists from Xtreme portal providers         ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def get_user_input(self, prompt: str, default: str = "", is_password: bool = False) -> str:
        """Get user input with optional default value"""
        if default:
            prompt = f"{prompt} [{default}]: "
        else:
            prompt = f"{prompt}: "
        
        if is_password:
            return getpass.getpass(prompt)
        else:
            return input(prompt).strip()
    
    def prompt_for_credentials(self) -> tuple:
        """Prompt user for Xtreme portal credentials"""
        print("\n🔐 Xtreme Portal Credentials")
        print("=" * 40)
        
        # Username
        default_username = self.saved_credentials.get('username', '')
        username = self.get_user_input("Enter your username", default_username)
        if not username:
            print("❌ Username is required!")
            sys.exit(1)
        
        # Password
        password = self.get_user_input("Enter your password", is_password=True)
        if not password:
            print("❌ Password is required!")
            sys.exit(1)
        
        # Server URL
        default_server = self.saved_credentials.get('server', '')
        server = self.get_user_input("Enter server URL (e.g., http://hi-world.me)", default_server)
        if not server:
            print("❌ Server URL is required!")
            sys.exit(1)
        
        # Add http:// if not present
        if not server.startswith(('http://', 'https://')):
            server = 'http://' + server
        
        return username, password, server
    
    def confirm_credentials(self, username: str, server: str) -> bool:
        """Ask user to confirm credentials"""
        print(f"\n📋 Credentials Summary:")
        print(f"   Username: {username}")
        print(f"   Server: {server}")
        print(f"   Password: {'*' * 8}")
        
        confirm = input("\nProceed with these credentials? (y/N): ").strip().lower()
        return confirm in ['y', 'yes']
    
    def run(self):
        """Main application flow"""
        try:
            self.print_banner()
            
            # Get credentials
            username, password, server = self.prompt_for_credentials()
            
            # Confirm before proceeding
            if not self.confirm_credentials(username, server):
                print("❌ Operation cancelled by user")
                sys.exit(0)
            
            # Save credentials (without password)
            self.save_credentials(username, password, server)
            
            print(f"\n🚀 Starting M3U playlist generation...")
            print(f"   Server: {server}")
            print(f"   Username: {username}")
            print("=" * 50)
            
            # Initialize scraper with output directory
            output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')
            scraper = RobustIPTVScraper(username, password, server, output_dir=output_dir)
            
            # Run the scraping process
            m3u_file = scraper.run()
            
            if m3u_file:
                print(f"\n✅ SUCCESS!")
                print(f"📁 M3U Playlist created: {m3u_file}")
                print(f"📊 Check the 'output' directory for detailed data")
                print("\n🎉 You can now use this M3U file with your IPTV player!")
            else:
                print(f"\n❌ FAILED!")
                print("Failed to create M3U playlist. Check the logs for details.")
                sys.exit(1)
                
        except KeyboardInterrupt:
            print(f"\n\n⚠️  Operation cancelled by user")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            logging.error(f"Application error: {e}", exc_info=True)
            sys.exit(1)

def main():
    """Entry point"""
    app = M3UScraperApp()
    app.run()

if __name__ == "__main__":
    main() 