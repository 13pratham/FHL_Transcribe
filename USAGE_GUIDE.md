# YouTube Audio Downloader - Usage Guide

## Features

### 1. List Mode (Browse Videos)
List videos from a YouTube channel without downloading.

**Quick List** (URLs only - Fast)
- Shows video URLs
- No API calls per video
- Very fast

**Detailed List** (With info - Slower)
- Shows title, duration, views
- Makes API call per video
- Takes longer but more informative

### 2. Download Mode
Download audio from YouTube videos as MP3 files.

**From Channel URL**
- Automatically fetches latest videos
- Downloads specified number

**From Individual URLs**
- Paste specific video URLs
- Full control over what to download

## Quick Examples

### List 10 videos (URLs only):
```bash
python3 working_downloader.py
```
Then enter:
- Mode: `2`
- URL: `https://www.youtube.com/@FortisHealthcareOfficial`
- Count: `10`
- Details: `n`

### Download 2 videos from channel:
```bash
python3 working_downloader.py
```
Then enter:
- Mode: `1` (or just press Enter)
- Count: `2`
- URL: `https://www.youtube.com/@FortisHealthcareOfficial`

### Download specific videos:
```bash
python3 working_downloader.py
```
Then enter:
- Mode: `1`
- Count: `2`
- First URL: `https://www.youtube.com/watch?v=VIDEO_ID_1`
- Second URL: `https://www.youtube.com/watch?v=VIDEO_ID_2`
- Press Enter twice

## Tips

1. **Use List mode first** to see available videos
2. **Download directly from list** - no need to copy/paste URLs
3. **Use number ranges** for bulk downloads (e.g., 1-10)
4. **Use comma-separated** for specific videos (e.g., 1,5,10)
5. **Start with small numbers** (2-5 videos) to test
6. **Check downloads folder** for your MP3 files

## Workflow Example

### Option A: List then Download (Recommended)

```bash
# Single command workflow
python3 working_downloader.py
> Mode: 2 (List)
> URL: https://www.youtube.com/@ChannelName
> Count: 20
> Details: n
> [See list of 20 videos]
> Download these videos? y
> Select option: 2 (Select specific)
> Numbers: 1,5,10,15
> [Downloads videos 1, 5, 10, and 15]

# Check your downloads folder
ls downloads/
```

### Option B: Traditional Workflow

```bash
# Step 1: List videos to see what's available
python3 working_downloader.py
> Mode: 2
> URL: https://www.youtube.com/@ChannelName
> Count: 20
> Details: n
> Download? n

# Copy the URLs you want

# Step 2: Download those specific videos
python3 working_downloader.py
> Mode: 1
> Count: 3
> Paste the 3 URLs you copied
> Press Enter twice

# Step 3: Check your downloads folder
ls downloads/
```

## Output Locations

- **Downloaded MP3 files**: `downloads/` folder
- **File names**: Based on video titles (sanitized)
- **Audio quality**: 128kbps+ (best available)

## Common Use Cases

### 1. Download latest videos from a channel
```
Mode: 1 (Download)
Count: 5
URL: Channel URL
```

### 2. Browse and selectively download
```
Mode: 2 (List)
Count: 20
Details: n
[See list of videos]
Download? y
Option: 2 (Select specific)
Numbers: 2,5,8,12
[Downloads selected videos]
```

### 3. Download specific videos you already know
```
Mode: 1 (Download)
Count: 3
Paste 3 video URLs
```

## Notes

- List mode doesn't download anything
- Download mode creates MP3 files in `downloads/` folder
- You can run the script multiple times
- Files are named after video titles
- Existing files won't be overwritten (new name will be used)
