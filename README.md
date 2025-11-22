# ✅ WORKING SOLUTION - YouTube Audio Downloader

## Quick Start (2 minutes)

### 1. Install dependency:
```bash
pip3 install pytubefix
```

### 2. Run the downloader:
```bash
python3 working_downloader.py
```

### 3. Choose your mode:

**Mode 1: Download (default)** - Download audio from videos  
**Mode 2: List** - Browse channel videos without downloading

### 4. Example Usage:

**List videos then download selected ones:**
```
Select mode (1=Download, 2=List) [default: 1]: 2
Enter YouTube channel URL: https://www.youtube.com/@FortisHealthcareOfficial
How many videos to list? (default: 10): 10
Fetch video details? (y/n) [default: n]: n

[Shows list of 10 video URLs]

Download these videos? (y/n) [default: n]: y

Download options:
1. All listed videos
2. Select specific videos by number
3. Cancel

Select option (1/2/3) [default: 1]: 2
Enter video numbers to download (e.g., 1,3,5 or 1-5):
Numbers: 1,3,5

[Downloads videos 1, 3, and 5]
```

**List videos with details:**
```
Select mode (1=Download, 2=List) [default: 1]: 2
Enter YouTube channel URL: https://www.youtube.com/@FortisHealthcareOfficial
How many videos to list? (default: 10): 5
Fetch video details? (y/n) [default: n]: y

[Shows list of 5 videos with titles, durations, views, and URLs]
```

**Download from channel:**
```
Select mode (1=Download, 2=List) [default: 1]: 1
How many videos to download? (default: 2): 2
Enter YouTube channel URL or video URL: https://www.youtube.com/@FortisHealthcareOfficial

[Automatically fetches and downloads 2 latest videos]
```

**Download individual videos:**
```
Select mode (1=Download, 2=List) [default: 1]: 1
How many videos to download? (default: 2): 2
Enter YouTube channel URL or video URL: https://www.youtube.com/watch?v=zuSubUKv_qg

Paste 1 more video URL(s):
https://www.youtube.com/watch?v=CExyH55m0Yk
[Press Enter to start]
```

### 5. Done!
Files will be saved in `downloads/` folder as MP3 files.

## Why This Works

✅ Uses **pytubefix** - maintained fork that handles YouTube's latest restrictions  
✅ **No API key needed** - works directly  
✅ **High quality audio** - 128kbps+  
✅ **Progress bar** - see download status  
✅ **Reliable** - tested and working  

## Example Output

```
============================================================
Processing: https://www.youtube.com/watch?v=jNQXAC9IVRw
============================================================
Title: Me at the zoo
Duration: 0:19
Author: jawed
Quality: 128kbps

Downloading...
 ↳ |███████████████████████████████████| 100.0%

✓ SUCCESS!
  File: Me at the zoo.mp3
  Size: 0.3 MB
  Location: downloads/
```

## Troubleshooting

**"ModuleNotFoundError: No module named 'pytubefix'"**
```bash
pip3 install pytubefix
```

**"HTTP Error 400/403"**
- Update pytubefix: `pip3 install --upgrade pytubefix`
- Try a different video URL
- Check if video is public

**Video won't download**
- Make sure the video is public (not private/unlisted)
- Check your internet connection
- Try updating: `pip3 install --upgrade pytubefix`

## Features

✅ **Two Modes:**
- Download mode - Download audio as MP3
- List mode - Browse channel videos without downloading

✅ **Download Features:**
- Downloads audio only (smaller file size)
- Converts to MP3 automatically
- Shows progress bar
- Handles multiple videos
- Sanitizes filenames
- Creates downloads folder automatically
- Continues even if one video fails

✅ **List Features:**
- View channel videos with details
- See title, duration, views, and URL
- Quick channel browsing
- **NEW:** Download selected videos after listing
  - Download all listed videos
  - Select specific videos by number (e.g., 1,3,5)
  - Select range of videos (e.g., 1-5)

## Notes

- Works with any public YouTube video
- No daily limits
- No API key required
- Respects YouTube's terms (personal use only)
- Files are named after video titles
