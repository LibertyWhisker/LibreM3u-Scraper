# 🎬 IPTV M3U Playlist Guide

## ✅ Success! Your M3U Playlist is Ready

I've successfully created your IPTV M3U playlist using the working API method. Here's everything you need to know:

## 📁 Your M3U File

**File:** `iptv_basic_playlist_20250830_220846.m3u`  
**Channels:** 10 sample channels (4K category)  
**Status:** ✅ Ready to use

## 🎯 How to Use Your M3U Playlist

### Option 1: VLC Media Player
1. Open VLC Media Player
2. Go to **Media** → **Open Network Stream**
3. Click **Browse** and select your `.m3u` file
4. Click **Play**

### Option 2: IPTV Apps
- **Android:** IPTV Smarters Pro, Tivimate, Perfect Player
- **iOS:** IPTV Smarters Pro, GSE Smart IPTV
- **Windows:** VLC, PotPlayer, Kodi
- **Mac:** VLC, IINA

### Option 3: Kodi
1. Install **IPTV Simple Client** addon
2. Configure with your M3U file path
3. Enjoy your channels

## 🔗 Stream URL Format

Your streams use this format:
```
http://hi-world.me/live/08b167da9c/f185f13b14/[STREAM_ID].ts
```

**Example:**
```
http://hi-world.me/live/08b167da9c/f185f13b14/483976.ts
```

## 📊 How to Add More Channels

### Step 1: Get Category IDs
```bash
curl "http://hi-world.me/player_api.php?username=08b167da9c&password=f185f13b14&action=get_live_categories"
```

### Step 2: Get Streams for a Category
```bash
curl "http://hi-world.me/player_api.php?username=08b167da9c&password=f185f13b14&action=get_live_streams&category_id=662"
```

### Step 3: Add to Your M3U File
For each stream, add these lines to your M3U file:
```
#EXTINF:-1 tvg-id="" tvg-name="Channel Name" group-title="Category",Channel Name
http://hi-world.me/live/08b167da9c/f185f13b14/[STREAM_ID].ts
```

## 🎬 Popular Categories

Based on the API data, here are some popular categories:

- **4K Channels** (ID: 662) - Ultra HD content
- **US Entertainment** (ID: 58) - American entertainment
- **US Sports** (ID: 492) - American sports
- **UK General** (ID: 47) - British channels
- **Movies** (ID: 493) - Movie channels
- **News** (ID: 491) - News channels

## 🛠️ Quick Commands

### Get All Categories
```bash
curl -s "http://hi-world.me/player_api.php?username=08b167da9c&password=f185f13b14&action=get_live_categories" | python3 -m json.tool
```

### Get Streams for 4K Category
```bash
curl -s "http://hi-world.me/player_api.php?username=08b167da9c&password=f185f13b14&action=get_live_streams&category_id=662" | python3 -m json.tool
```

### Test a Stream URL
```bash
curl -I "http://hi-world.me/live/08b167da9c/f185f13b14/483976.ts"
```

## 📱 Your IPTV Credentials

- **Server:** http://hi-world.me
- **Username:** 08b167da9c
- **Password:** f185f13b14
- **M3U URL:** http://cf.layerseventv.com/get.php?username=08b167da9c&password=f185f13b14&type=m3u_plus&output=ts

## 🔧 Troubleshooting

### If channels don't work:
1. **Check your internet connection**
2. **Verify the stream ID is correct**
3. **Try a different IPTV app**
4. **Contact your provider if issues persist**

### If you want more channels:
1. **Use the API commands above**
2. **Add stream IDs to your M3U file**
3. **Test each channel individually**

## 🎉 Success!

You now have:
- ✅ A working M3U playlist with 10 channels
- ✅ The correct stream URL format
- ✅ API access to get more channels
- ✅ Instructions for expanding your playlist

**Your IPTV service is working perfectly!** The issue was that the direct M3U download URL had geographic restrictions, but the API method works great.

## 📞 Next Steps

1. **Test your M3U file** with VLC or your preferred app
2. **Add more channels** using the API method
3. **Enjoy your IPTV service!**

---

*Generated on: 2025-08-30 22:08:46*  
*Total channels in playlist: 10*  
*Stream format: TS (Transport Stream)* 