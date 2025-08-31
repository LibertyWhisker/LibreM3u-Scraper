#!/usr/bin/env python3
"""
Robust IPTV Scraper
Handles connection issues and builds complete M3U playlists
"""

import requests
import json
import time
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('iptv_scraper.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class RobustIPTVScraper:
    def __init__(self, username: str, password: str, server: str, output_dir: str = "output"):
        self.username = username
        self.password = password
        self.server = server.rstrip('/')
        self.output_dir = output_dir
        self.session = requests.Session()
        
        # More conservative rate limiting
        self.request_delay = 3  # seconds between requests
        self.max_retries = 3
        self.retry_delay = 10
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        logging.info(f"Robust IPTV Scraper initialized for server: {server}")
    
    def make_api_request(self, url: str, retries: int = None) -> Optional[Dict]:
        """Make API request with conservative retry logic"""
        if retries is None:
            retries = self.max_retries
            
        for attempt in range(retries):
            try:
                logging.debug(f"Making request: {url}")
                
                # Add headers to look more like a browser
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive'
                }
                
                response = self.session.get(url, timeout=60, headers=headers)
                response.raise_for_status()
                
                # Rate limiting
                time.sleep(self.request_delay)
                
                return response.json()
                
            except Exception as e:
                logging.warning(f"Request failed (attempt {attempt + 1}/{retries}): {e}")
                if attempt < retries - 1:
                    logging.info(f"Waiting {self.retry_delay} seconds before retry...")
                    time.sleep(self.retry_delay)
                else:
                    logging.error(f"All retries failed for: {url}")
                    return None
    
    def load_existing_categories(self) -> List[Dict]:
        """Load categories from existing file if available"""
        if os.path.exists('categories.json'):
            try:
                with open('categories.json', 'r', encoding='utf-8') as f:
                    categories = json.load(f)
                logging.info(f"Loaded {len(categories)} categories from existing file")
                return categories
            except Exception as e:
                logging.warning(f"Failed to load existing categories: {e}")
        return []
    
    def get_categories(self) -> List[Dict]:
        """Get all channel categories"""
        # Try to load existing data first
        categories = self.load_existing_categories()
        if categories:
            return categories
        
        # If no existing data, fetch from API
        logging.info("Fetching channel categories from API...")
        url = f"{self.server}/player_api.php?username={self.username}&password={self.password}&action=get_live_categories"
        
        categories = self.make_api_request(url)
        if categories:
            logging.info(f"Found {len(categories)} categories")
            # Save for future use
            with open('categories.json', 'w', encoding='utf-8') as f:
                json.dump(categories, f, indent=2, ensure_ascii=False)
            return categories
        return []
    
    def get_streams_for_category(self, category_id: str, category_name: str) -> List[Dict]:
        """Get all streams for a specific category with better error handling"""
        logging.info(f"Fetching streams for category: {category_name} (ID: {category_id})")
        url = f"{self.server}/player_api.php?username={self.username}&password={self.password}&action=get_live_streams&category_id={category_id}"
        
        streams = self.make_api_request(url)
        if streams:
            logging.info(f"Found {len(streams)} streams in {category_name}")
            return streams
        else:
            logging.warning(f"No streams found for category: {category_name}")
            return []
    
    def build_stream_url(self, stream_id: str) -> str:
        """Build stream URL for a given stream ID"""
        return f"{self.server}/live/{self.username}/{self.password}/{stream_id}.ts"
    
    def create_m3u_playlist(self, all_streams: List[Dict], filename: str = None) -> str:
        """Create M3U playlist from all streams"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"iptv_complete_playlist_{timestamp}.m3u"
        
        filepath = os.path.join(self.output_dir, filename)
        
        logging.info(f"Creating M3U playlist: {filepath}")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write M3U header
            f.write("#EXTM3U\n")
            f.write(f"# Generated by Robust IPTV Scraper on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Server: {self.server}\n")
            f.write(f"# Total Channels: {len(all_streams)}\n\n")
            
            current_category = None
            
            for stream in all_streams:
                # Write category header if category changed
                if stream.get('category_name') != current_category:
                    current_category = stream.get('category_name')
                    f.write(f"\n# {current_category}\n")
                
                # Write stream info
                stream_name = stream.get('name', 'Unknown')
                stream_url = self.build_stream_url(stream.get('stream_id', ''))
                
                f.write(f"#EXTINF:-1 tvg-id=\"{stream.get('stream_id', '')}\" tvg-name=\"{stream_name}\" tvg-logo=\"{stream.get('stream_icon', '')}\" group-title=\"{current_category}\",{stream_name}\n")
                f.write(f"{stream_url}\n")
        
        logging.info(f"M3U playlist created successfully: {filepath}")
        return filepath
    
    def scrape_with_resume(self) -> Dict:
        """Scrape all channels with resume capability"""
        logging.info("Starting robust channel scrape...")
        
        # Get all categories
        categories = self.load_existing_categories()
        if not categories:
            categories = self.get_categories()
            if not categories:
                logging.error("Failed to get categories")
                return {}
        
        all_streams = []
        total_categories = len(categories)
        
        # Check for existing progress
        progress_file = os.path.join(self.output_dir, "scrape_progress.json")
        completed_categories = set()
        
        if os.path.exists(progress_file):
            try:
                with open(progress_file, 'r') as f:
                    progress = json.load(f)
                    completed_categories = set(progress.get('completed_categories', []))
                    all_streams = progress.get('all_streams', [])
                logging.info(f"Resuming from previous session. Completed categories: {len(completed_categories)}")
            except Exception as e:
                logging.warning(f"Failed to load progress: {e}")
        
        for i, category in enumerate(categories, 1):
            category_id = category.get('category_id')
            category_name = category.get('category_name', 'Unknown')
            
            # Skip if already completed
            if category_id in completed_categories:
                logging.info(f"Skipping completed category {i}/{total_categories}: {category_name}")
                continue
            
            logging.info(f"Processing category {i}/{total_categories}: {category_name}")
            
            # Get streams for this category
            streams = self.get_streams_for_category(category_id, category_name)
            
            # Add category info to each stream
            for stream in streams:
                stream['category_name'] = category_name
                stream['category_id'] = category_id
            
            all_streams.extend(streams)
            completed_categories.add(category_id)
            
            # Save progress after each category
            progress = {
                'completed_categories': list(completed_categories),
                'all_streams': all_streams,
                'last_updated': datetime.now().isoformat()
            }
            with open(progress_file, 'w') as f:
                json.dump(progress, f, indent=2)
            
            # Save category streams individually
            if streams:
                safe_filename = f"category_{category_id}_{category_name.replace(' ', '_').replace('/', '_')}.json"
                filepath = os.path.join(self.output_dir, safe_filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(streams, f, indent=2, ensure_ascii=False)
            
            logging.info(f"Total streams collected so far: {len(all_streams)}")
            
            # Add extra delay between categories to be extra safe
            time.sleep(5)
        
        # Save complete data
        complete_data = {
            'server': self.server,
            'username': self.username,
            'scrape_date': datetime.now().isoformat(),
            'total_categories': len(categories),
            'total_streams': len(all_streams),
            'categories': categories,
            'streams': all_streams
        }
        
        filepath = os.path.join(self.output_dir, "complete_data.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(complete_data, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Scraping completed! Total streams: {len(all_streams)}")
        return complete_data
    
    def run(self) -> str:
        """Run the complete scraping process"""
        logging.info("=" * 50)
        logging.info("ROBUST IPTV SCRAPER STARTED")
        logging.info("=" * 50)
        
        # Scrape all channels
        data = self.scrape_with_resume()
        
        if not data or not data.get('streams'):
            logging.error("No streams found!")
            return None
        
        # Create M3U playlist
        m3u_file = self.create_m3u_playlist(data['streams'])
        
        logging.info("=" * 50)
        logging.info("ROBUST IPTV SCRAPER COMPLETED")
        logging.info(f"M3U Playlist: {m3u_file}")
        logging.info(f"Total Channels: {len(data['streams'])}")
        logging.info(f"Total Categories: {len(data['categories'])}")
        logging.info("=" * 50)
        
        return m3u_file

def main():
    """Main function for command line usage"""
    if len(sys.argv) != 4:
        print("Usage: python3 robust_iptv_scraper.py <username> <password> <server>")
        print("Example: python3 robust_iptv_scraper.py your_username your_password http://your-provider.com")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    server = sys.argv[3]
    
    scraper = RobustIPTVScraper(username, password, server)
    m3u_file = scraper.run()
    
    if m3u_file:
        print(f"\n✅ Success! M3U playlist created: {m3u_file}")
    else:
        print("\n❌ Failed to create M3U playlist")

if __name__ == "__main__":
    main() 