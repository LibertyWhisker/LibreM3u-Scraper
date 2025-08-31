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

## 📺 Example: Program Running

### Interactive Mode Example

Here's what the program looks like when running in interactive mode:

```bash
$ ./run.sh
```

**Terminal Output:**
```
╔══════════════════════════════════════════════════════════════╗
║                    M3U IPTV Scraper v1.0                    ║
║                                                              ║
║  Interactive IPTV Playlist Generator                        ║
║  Extracts M3U playlists from Xtreme portal providers       ║
╚══════════════════════════════════════════════════════════════╝

🔐 Enter your Xtreme portal credentials:

Username: your_username_here
Password: ********
Server URL: http://your-provider.com

✅ Credentials confirmed:
   Username: your_username_here
   Server: http://your-provider.com
   Password: [HIDDEN]

🚀 Starting IPTV scraping process...

2024-01-01 12:00:00,123 - INFO - Initializing IPTV scraper...
2024-01-01 12:00:01,456 - INFO - Testing connection to server...
2024-01-01 12:00:02,789 - INFO - Connection successful! Starting category fetch...
2024-01-01 12:00:03,012 - INFO - Found 629 total categories
2024-01-01 12:00:03,234 - INFO - Processing category 1/629: 4K| UHD ³⁸⁴⁰ᵖ
2024-01-01 12:00:04,567 - INFO - Found 15 streams in 4K| UHD ³⁸⁴⁰ᵖ
2024-01-01 12:00:04,890 - INFO - Total streams collected so far: 15
2024-01-01 12:00:05,123 - INFO - Processing category 2/629: 4K| RELAX UHD ³⁸⁴⁰ᵖ ☼
2024-01-01 12:00:06,456 - INFO - Found 8 streams in 4K| RELAX UHD ³⁸⁴⁰ᵖ ☼
2024-01-01 12:00:06,789 - INFO - Total streams collected so far: 23
2024-01-01 12:00:07,012 - INFO - Processing category 3/629: US| PRIME ᴴᴰ ⁶⁰ᵖᵛ
2024-01-01 12:00:08,345 - INFO - Found 42 streams in US| PRIME ᴴᴰ ⁶⁰ᵖᵛ
2024-01-01 12:00:08,678 - INFO - Total streams collected so far: 65
...
2024-01-01 12:15:23,456 - INFO - Processing category 95/629: CA| DAZN PPV
2024-01-01 12:15:24,789 - INFO - Found 32 streams in CA| DAZN PPV
2024-01-01 12:15:25,012 - INFO - Total streams collected so far: 7,482
2024-01-01 12:15:26,345 - INFO - Processing category 96/629: CA| TSN+ PPV
2024-01-01 12:15:27,678 - INFO - Found 51 streams in CA| TSN+ PPV
2024-01-01 12:15:28,012 - INFO - Total streams collected so far: 7,533
...
2024-01-01 12:29:45,123 - INFO - Processing category 629/629: AR| DOCUMENTARY 4K ▶ وثائقي
2024-01-01 12:29:46,456 - INFO - Found 67 streams in AR| DOCUMENTARY 4K ▶ وثائقي
2024-01-01 12:29:47,789 - INFO - Total streams collected so far: 8,109
2024-01-01 12:29:48,012 - INFO - ✅ Scraping completed successfully!
2024-01-01 12:29:48,345 - INFO - 📊 Final Statistics:
2024-01-01 12:29:48,678 - INFO -    • Total Categories: 629
2024-01-01 12:29:49,012 - INFO -    • Total Streams: 8,109
2024-01-01 12:29:49,345 - INFO -    • Processing Time: 29 minutes 48 seconds
2024-01-01 12:29:49,678 - INFO -    • Average Rate: 4.5 streams/second
2024-01-01 12:29:50,012 - INFO - 🎯 Generating M3U playlist...
2024-01-01 12:29:50,345 - INFO - 📁 Saving files to output directory...
2024-01-01 12:29:51,678 - INFO - ✅ M3U playlist generated: output/playlist_20240101_122951.m3u
2024-01-01 12:29:52,012 - INFO - ✅ Complete data saved: output/complete_data.json
2024-01-01 12:29:52,345 - INFO - ✅ Individual category files saved
2024-01-01 12:29:52,678 - INFO - 🎉 All done! Your IPTV playlist is ready.

📁 Output Files Created:
   • output/playlist_20240101_122951.m3u (8,109 channels)
   • output/complete_data.json (Full API data)
   • output/categories.json (Category list)
   • output/category_*.json (Individual category files)
   • logs/iptv_scraper.log (Detailed logs)

🎯 Next Steps:
   1. Import the M3U file into your IPTV player
   2. Enjoy your organized channel collection!
   3. Check logs/iptv_scraper.log for detailed information
```

### Command Line Mode Example

For automated usage:

```bash
$ cd src && python3 robust_iptv_scraper.py demo_user mypassword123 http://example.com
```

**Terminal Output:**
```
2024-01-01 12:00:00,123 - INFO - Starting IPTV scraper...
2024-01-01 12:00:00,456 - INFO - Username: demo_user
2024-01-01 12:00:00,789 - INFO - Server: http://example.com
2024-01-01 12:00:01,012 - INFO - Testing connection...
2024-01-01 12:00:01,345 - INFO - Connection successful
2024-01-01 12:00:01,678 - INFO - Fetching categories...
2024-01-01 12:00:02,012 - INFO - Found 629 categories
2024-01-01 12:00:02,345 - INFO - Processing category 1/629: 4K| UHD ³⁸⁴⁰ᵖ
2024-01-01 12:00:03,678 - INFO - Found 15 streams
2024-01-01 12:00:04,012 - INFO - Processing category 2/629: 4K| RELAX UHD ³⁸⁴⁰ᵖ ☼
2024-01-01 12:00:05,345 - INFO - Found 8 streams
...
2024-01-01 12:29:45,123 - INFO - Processing category 629/629: AR| DOCUMENTARY 4K ▶ وثائقي
2024-01-01 12:29:46,456 - INFO - Found 67 streams
2024-01-01 12:29:47,789 - INFO - ✅ Scraping completed! Total: 8,109 streams
2024-01-01 12:29:48,012 - INFO - 📁 Saving M3U playlist...
2024-01-01 12:29:48,345 - INFO - ✅ M3U playlist saved: output/playlist_20240101_122948.m3u
```

### Progress Indicators

The program shows real-time progress with:
- **Category counter**: `Processing category X/629`
- **Stream counts**: `Found X streams in Category Name`
- **Running totals**: `Total streams collected so far: X`
- **Time estimates**: Based on current processing rate
- **Completion percentage**: Visual progress indicators

### Error Handling Examples

**Connection Issues:**
```
2024-01-01 12:00:01,234 - WARNING - Connection failed, retrying in 5 seconds...
2024-01-01 12:00:06,567 - INFO - Retry 1/3 successful
```

**Rate Limiting:**
```
2024-01-01 12:15:23,456 - WARNING - Rate limit detected, waiting 10 seconds...
2024-01-01 12:15:33,789 - INFO - Resuming normal operation
```

**Authentication Errors:**
```
2024-01-01 12:00:01,234 - ERROR - Authentication failed: Invalid credentials
2024-01-01 12:00:01,567 - ERROR - Please check your username and password
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