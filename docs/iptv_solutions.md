# IPTV M3U Playlist Download Solutions

## Current Status
✅ **Credentials are valid** - API endpoint returned channel categories  
❌ **M3U endpoint returns empty content** - Likely due to geographic restrictions  

## Your IPTV Details
- **Username:** 08b167da9c
- **Password:** f185f13b14
- **Server:** http://hi-world.me
- **M3U URL:** http://cf.layerseventv.com/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts

## Solution 1: Try Different URL Variations

### Option A: Use the working server domain
```bash
curl -L "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts" -o playlist.m3u
```

### Option B: Try different output formats
```bash
# Try without "plus"
curl -L "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u&output=ts" -o playlist.m3u

# Try different output types
curl -L "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=m3u8" -o playlist.m3u
```

### Option C: Try with different parameters
```bash
# Add user agent
curl -L -H "User-Agent: VLC/3.0.0" "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts" -o playlist.m3u

# Try with referer
curl -L -H "Referer: http://hi-world.me/" "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts" -o playlist.m3u
```

## Solution 2: Use a VPN (Recommended)

The most likely issue is **geographic restrictions**. Try:

1. **Install a VPN** (NordVPN, ExpressVPN, etc.)
2. **Connect to a different country** (try UK, US, or European servers)
3. **Try the download again**

```bash
# After connecting to VPN, run:
curl -L "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts" -o playlist.m3u
```

## Solution 3: Use IPTV Apps Directly

Instead of downloading the M3U file, use IPTV apps that can connect directly:

### For Android:
- **IPTV Smarters Pro**
- **Tivimate**
- **Perfect Player**

### For Windows:
- **VLC Media Player** (can open M3U URLs directly)
- **PotPlayer**
- **Kodi** with IPTV Simple Client

### For Mac:
- **VLC Media Player**
- **IINA**

## Solution 4: Manual M3U Creation

Since the API works, you could potentially create an M3U file manually:

```bash
# Get channel list from API
curl "http://hi-world.me/player_api.php?username=08b167da9c&password=f185f13b14&action=get_live_categories" > channels.json

# Then manually construct M3U file with stream URLs
```

## Solution 5: Contact Your Provider

If none of the above work:

1. **Contact your IPTV provider** for the correct M3U URL
2. **Ask if there are geographic restrictions**
3. **Request alternative access methods**
4. **Check if your subscription is still active**

## Testing Commands

### Test your credentials:
```bash
curl "http://hi-world.me/player_api.php?username=08b167da9c&password=f185f13b14&action=get_live_categories"
```

### Test M3U URL with verbose output:
```bash
curl -v "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts"
```

### Test with different user agents:
```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts"
```

## Quick Download Script

Save this as `download_iptv.sh`:

```bash
#!/bin/bash
echo "🎬 IPTV M3U Downloader"
echo "======================"

# Try multiple variations
urls=(
    "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts"
    "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u&output=ts"
    "http://hi-world.me/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=m3u8"
)

for url in "${urls[@]}"; do
    echo "Trying: $url"
    if curl -L "$url" -o playlist.m3u 2>/dev/null && [ -s playlist.m3u ]; then
        echo "✅ Success! Downloaded to playlist.m3u"
        echo "File size: $(wc -c < playlist.m3u) bytes"
        echo "Channels: $(grep -c '#EXTINF' playlist.m3u)"
        exit 0
    else
        echo "❌ Failed"
    fi
done

echo "❌ All attempts failed. Try using a VPN."
```

Make it executable: `chmod +x download_iptv.sh`
Run it: `./download_iptv.sh`

## Most Likely Solution

**Use a VPN** - This is the most common solution for IPTV geographic restrictions. Connect to a VPN server in a different country and try the download again. 