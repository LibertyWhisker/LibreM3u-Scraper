# Output Directory

This directory contains generated M3U playlists and data files created by the M3U Scraper application.

## Contents

- **M3U Playlists**: Generated playlist files with stream URLs
- **Category Data**: JSON files containing channel information by category
- **Complete Data**: Full API response data
- **Progress Files**: Resume capability data for interrupted sessions

## Important Notes

⚠️ **This directory is excluded from version control for privacy and security reasons.**

- Generated files contain sensitive stream URLs and channel information
- These files are specific to your IPTV provider and credentials
- The application will create these files when you run it
- Do not manually edit or commit these files

## File Types

- `playlist_YYYYMMDD_HHMMSS.m3u` - Main M3U playlist file
- `complete_data.json` - Complete API response data
- `category_*.json` - Individual category data files
- `scrape_progress.json` - Progress tracking for resume capability

## Usage

Simply run the application and it will automatically populate this directory with the generated files. 