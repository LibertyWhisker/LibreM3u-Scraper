# M3U Scraper - IPTV Playlist Generator

A robust, interactive application for extracting M3U playlists from Xtreme portal IPTV providers. This tool allows you to generate complete M3U playlists with all available channels from your IPTV subscription.

## 🏗️ Project Structure

```
M3U_Scraper/
├── src/                    # Source code
│   ├── main.py            # Main interactive application
│   ├── robust_iptv_scraper.py  # Core scraping engine
│   └── iptv_scraper.py    # Original scraper (reference)
├── docs/                   # Documentation
│   ├── README.md          # This file
│   ├── APPLICATION_OVERVIEW.md
│   ├── IPTV_M3U_GUIDE.md
│   └── iptv_solutions.md
├── examples/               # Example files
│   └── scraper_config.json.example
├── logs/                   # Log files
├── output/                 # Generated playlists and data
├── temp/                   # Temporary/legacy files
├── requirements.txt        # Python dependencies
├── run.sh                  # Launcher script
└── test_installation.py    # Installation verification
```

## Features

- 🔐 **Interactive Credential Input** - Secure password prompts for Xtreme portal credentials
- 🎯 **Robust Scraping** - Handles connection issues and rate limiting automatically
- 📁 **Progress Tracking** - Resume interrupted scraping sessions
- 🗂️ **Organized Output** - Creates structured M3U playlists with channel categories
- 💾 **Credential Memory** - Remembers username and server (password not stored for security)
- 📊 **Detailed Logging** - Comprehensive logging for troubleshooting
- 🛡️ **Error Handling** - Graceful handling of network issues and API errors

## Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd M3u_Scraper
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Make the script executable (optional)**
   ```bash
   chmod +x run.sh
   ```

4. **Verify installation**
   ```bash
   python3 test_installation.py
   ```

## Usage

### Interactive Mode (Recommended)

Run the main application for an interactive experience:

```bash
# Option 1: Use the launcher script
./run.sh

# Option 2: Run directly
cd src && python3 main.py
```

The application will:
1. Display a welcome banner
2. Prompt for your Xtreme portal credentials
3. Confirm the details before proceeding
4. Generate the M3U playlist
5. Save all data to the `output` directory

### Command Line Mode

For automated usage, you can still use the original scraper directly:

```bash
cd src && python3 robust_iptv_scraper.py <username> <password> <server>
```

Example:
```bash
cd src && python3 robust_iptv_scraper.py your_username your_password http://your-provider.com
```

## Input Requirements

### Xtreme Portal Credentials

You'll need:
- **Username**: Your IPTV provider username
- **Password**: Your IPTV provider password  
- **Server URL**: The Xtreme portal server URL (e.g., `http://your-provider.com`)

### Example Credentials Format

```
Username: your_username_here
Password: your_password_here
Server: http://your-provider.com
```

## Output Files

The application creates several output files in the `output/` directory:

### M3U Playlist
- **Location**: `output/playlist_YYYYMMDD_HHMMSS.m3u`
- **Format**: Standard M3U playlist compatible with most IPTV players
- **Content**: All available channels with proper stream URLs

### Detailed Data
- **Complete Data**: `output/complete_data.json` - Full API response data
- **Category Files**: Individual JSON files for each channel category
- **Progress Tracking**: Resume capability for interrupted sessions

### Logs
- **Log File**: `logs/iptv_scraper.log` - Detailed operation logs
- **Console Output**: Real-time progress updates

## Using the M3U Playlist

1. **Download the generated M3U file** from the `output` directory
2. **Import into your IPTV player**:
   - VLC Media Player
   - Kodi (with IPTV Simple Client)
   - Perfect Player
   - Tivimate
   - Any M3U-compatible player

3. **The playlist includes**:
   - Channel names and categories
   - Direct stream URLs
   - Proper M3U formatting

## Troubleshooting

### Common Issues

**Connection Errors**
- Verify your server URL is correct
- Check your internet connection
- Ensure your IPTV subscription is active

**Authentication Errors**
- Double-check username and password
- Verify your subscription hasn't expired
- Contact your IPTV provider if issues persist

**Rate Limiting**
- The application automatically handles rate limiting
- If you encounter issues, wait a few minutes and try again

### Log Files

Check the `logs/iptv_scraper.log` file for detailed error information:
```bash
tail -f logs/iptv_scraper.log
```

## Security Notes

- **Passwords are never stored** - Only username and server are saved
- **Secure input** - Password prompts use `getpass` for hidden input
- **Local storage only** - All data is stored locally on your machine

## Technical Details

### Supported Providers
- Xtreme portal compatible IPTV providers
- Standard IPTV API endpoints
- M3U playlist format output

### Rate Limiting
- Conservative request delays (3 seconds between requests)
- Automatic retry logic with exponential backoff
- Respectful scraping practices

### Error Recovery
- Resume capability for interrupted sessions
- Progress tracking and recovery
- Graceful error handling

## Development

### Project Organization
- **`src/`** - All source code files
- **`docs/`** - Documentation and guides
- **`examples/`** - Example configuration files
- **`logs/`** - Application logs
- **`output/`** - Generated playlists and data
- **`temp/`** - Legacy and temporary files

### Adding New Features
1. Place new source code in the `src/` directory
2. Update documentation in the `docs/` directory
3. Add examples to the `examples/` directory
4. Update `test_installation.py` if needed

## License

This project is for educational and personal use only. Please respect your IPTV provider's terms of service.

## Support

For issues or questions:
1. Check the log files for error details
2. Verify your credentials and server URL
3. Ensure your IPTV subscription is active
4. Review the troubleshooting section above

---

**Note**: This tool is designed for legitimate IPTV subscriptions. Please ensure you have proper authorization to access the content you're scraping. 