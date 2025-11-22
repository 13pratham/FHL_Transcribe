#!/usr/bin/env python3
"""
YouTube Audio Downloader - Using pytubefix (maintained fork)
This version handles YouTube's latest restrictions
"""

import os
import re
from pytubefix import YouTube, Channel
from pytubefix.cli import on_progress


def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    return re.sub(r'[<>:"/\\|?*]', '', filename)[:200]


def list_channel_videos(channel_url, max_videos=10):
    """List videos from a channel"""
    try:
        print(f"\nFetching channel videos...")
        print(f"This may take a moment...\n")
        
        channel = Channel(channel_url)
        video_urls = list(channel.video_urls)
        
        if not video_urls:
            print(f"✗ No videos found in channel")
            return []
        
        print(f"{'='*80}")
        print(f"Channel: {channel.channel_name}")
        print(f"Total videos: {len(video_urls)}")
        print(f"{'='*80}\n")
        
        # List video URLs with details
        videos = []
        for i, video_obj in enumerate(video_urls[:max_videos], 1):
            try:
                # Extract video ID from YouTube object
                if hasattr(video_obj, 'video_id'):
                    video_id = video_obj.video_id
                elif hasattr(video_obj, 'watch_url'):
                    video_id = video_obj.watch_url.split('watch?v=')[1].split('&')[0]
                else:
                    obj_str = str(video_obj)
                    if 'videoId=' in obj_str:
                        video_id = obj_str.split('videoId=')[1].split('>')[0]
                    else:
                        continue
                
                url_str = f"https://www.youtube.com/watch?v={video_id}"
                print(f"[{i}] Fetching: {url_str}")
                yt = YouTube(url_str)
                
                videos.append({
                    'number': i,
                    'title': yt.title,
                    'url': url_str,
                    'duration': f"{yt.length // 60}:{yt.length % 60:02d}",
                    'views': yt.views
                })
                
                print(f"    Title: {yt.title}")
                print(f"    Duration: {yt.length // 60}:{yt.length % 60:02d} | Views: {yt.views:,}")
                print(f"    URL: {url_str}\n")
                
            except Exception as e:
                # If fetching details fails, just show the URL
                try:
                    if hasattr(video_obj, 'video_id'):
                        video_id = video_obj.video_id
                    else:
                        obj_str = str(video_obj)
                        video_id = obj_str.split('videoId=')[1].split('>')[0]
                    url_str = f"https://www.youtube.com/watch?v={video_id}"
                except:
                    url_str = "Error extracting URL"
                
                print(f"    ⚠ Could not fetch details: {str(e)[:50]}")
                print(f"    URL: {url_str}\n")
                videos.append({
                    'number': i,
                    'title': 'Unknown',
                    'url': url_str
                })
        
        return videos
    except Exception as e:
        print(f"✗ Error fetching channel: {str(e)}")
        return []


def get_channel_videos(channel_url, max_videos=2):
    """Get video URLs from a channel for downloading"""
    try:
        print(f"\nFetching channel videos...")
        channel = Channel(channel_url)
        video_urls = list(channel.video_urls)
        
        if not video_urls:
            print(f"✗ No videos found")
            return []
        
        print(f"✓ Channel: {channel.channel_name}")
        print(f"  Total videos: {len(video_urls)}")
        print(f"  Selecting first {max_videos} video(s)...\n")
        
        # Extract video IDs and format URLs
        formatted_urls = []
        for video_obj in video_urls[:max_videos]:
            # Extract video ID from YouTube object
            if hasattr(video_obj, 'video_id'):
                video_id = video_obj.video_id
            elif hasattr(video_obj, 'watch_url'):
                video_id = video_obj.watch_url.split('watch?v=')[1].split('&')[0]
            else:
                # Try to extract from string representation
                obj_str = str(video_obj)
                if 'videoId=' in obj_str:
                    video_id = obj_str.split('videoId=')[1].split('>')[0]
                else:
                    continue
            
            url_str = f"https://www.youtube.com/watch?v={video_id}"
            formatted_urls.append(url_str)
        
        return formatted_urls
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return []


def download_audio(video_url, output_path='downloads'):
    """Download audio from a YouTube video"""
    try:
        print(f"\n{'='*60}")
        print(f"Processing: {video_url}")
        print(f"{'='*60}")
        
        # Validate URL
        if not video_url or not isinstance(video_url, str):
            print(f"\n✗ Invalid URL type: {type(video_url)}")
            return False
        
        if not video_url.startswith('http'):
            print(f"\n✗ Invalid URL format: {video_url}")
            return False
        
        # Create YouTube object with progress callback
        yt = YouTube(video_url, on_progress_callback=on_progress)
        
        print(f"Title: {yt.title}")
        print(f"Duration: {yt.length // 60}:{yt.length % 60:02d}")
        print(f"Author: {yt.author}")
        
        # Get best audio stream
        audio_stream = yt.streams.get_audio_only()
        
        if not audio_stream:
            print(f"✗ No audio stream found")
            return False
        
        print(f"Quality: {audio_stream.abr}")
        print(f"\nDownloading...")
        
        # Download
        safe_title = sanitize_filename(yt.title)
        output_file = audio_stream.download(
            output_path=output_path,
            filename=f"{safe_title}.mp3"
        )
        
        file_size = os.path.getsize(output_file) / (1024 * 1024)
        print(f"\n✓ SUCCESS!")
        print(f"  File: {os.path.basename(output_file)}")
        print(f"  Size: {file_size:.1f} MB")
        print(f"  Location: {output_path}/")
        return True
        
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        return False


def main():
    print("\n" + "="*80)
    print("YouTube Audio Downloader")
    print("="*80)
    print("\nModes:")
    print("1. Download - Download audio from videos")
    print("2. List - List videos from a channel (no download)")
    print("="*80 + "\n")
    
    # Ask for mode
    mode = input("Select mode (1=Download, 2=List) [default: 1]: ").strip()
    
    if mode == "2":
        # List mode
        channel_url = input("\nEnter YouTube channel URL: ").strip()
        if not channel_url:
            print("\n✗ No URL provided!")
            return
        
        if '@' not in channel_url and '/c/' not in channel_url and '/channel/' not in channel_url:
            print("\n✗ Invalid channel URL!")
            print("Use: https://www.youtube.com/@ChannelName")
            return
        
        try:
            max_list = int(input("How many videos to list? (default: 10): ").strip() or "10")
        except ValueError:
            max_list = 10
        
        # Ask if they want detailed info or just URLs
        detail_mode = input("Fetch video details? (y/n) [default: n]: ").strip().lower()
        
        if detail_mode == 'y':
            videos = list_channel_videos(channel_url, max_list)
        else:
            # Quick mode - just list URLs
            try:
                print(f"\nFetching channel videos...\n")
                channel = Channel(channel_url)
                video_urls = list(channel.video_urls)
                
                print(f"{'='*80}")
                print(f"Channel: {channel.channel_name}")
                print(f"Total videos: {len(video_urls)}")
                print(f"{'='*80}\n")
                
                # Ensure URLs are properly formatted
                videos = []
                for i, video_obj in enumerate(video_urls[:max_list], 1):
                    # Extract video ID from YouTube object
                    if hasattr(video_obj, 'video_id'):
                        video_id = video_obj.video_id
                    elif hasattr(video_obj, 'watch_url'):
                        video_id = video_obj.watch_url.split('watch?v=')[1].split('&')[0]
                    else:
                        # Try to extract from string representation
                        obj_str = str(video_obj)
                        if 'videoId=' in obj_str:
                            video_id = obj_str.split('videoId=')[1].split('>')[0]
                        else:
                            video_id = obj_str
                    
                    final_url = f"https://www.youtube.com/watch?v={video_id}"
                    print(f"[{i}] {final_url}")
                    
                    # Store the formatted URL
                    videos.append({
                        'number': i,
                        'url': final_url
                    })
            except Exception as e:
                print(f"✗ Error: {str(e)}")
                return
        
        if videos:
            print(f"\n{'='*80}")
            print(f"Listed {len(videos)} video(s)")
            print(f"{'='*80}\n")
            
            # Ask if user wants to download
            download_choice = input("Download these videos? (y/n) [default: n]: ").strip().lower()
            
            if download_choice == 'y':
                # Ask which videos to download
                print("\nDownload options:")
                print("1. All listed videos")
                print("2. Select specific videos by number")
                print("3. Cancel")
                
                option = input("\nSelect option (1/2/3) [default: 1]: ").strip()
                
                if option == '3':
                    print("Download cancelled.")
                    return
                elif option == '2':
                    # Select specific videos
                    print(f"\nEnter video numbers to download (e.g., 1,3,5 or 1-5):")
                    selection = input("Numbers: ").strip()
                    
                    selected_urls = []
                    try:
                        # Parse selection
                        if '-' in selection:
                            # Range selection (e.g., 1-5)
                            start, end = selection.split('-')
                            selected_nums = range(int(start), int(end) + 1)
                        elif ',' in selection:
                            # Comma-separated (e.g., 1,3,5)
                            selected_nums = [int(x.strip()) for x in selection.split(',')]
                        else:
                            # Single number
                            selected_nums = [int(selection)]
                        
                        # Get URLs for selected videos
                        for num in selected_nums:
                            if 1 <= num <= len(videos):
                                selected_urls.append(videos[num-1]['url'])
                        
                        if not selected_urls:
                            print("No valid videos selected.")
                            return
                            
                    except Exception as e:
                        print(f"Invalid selection: {e}")
                        return
                else:
                    # Download all
                    selected_urls = [v['url'] for v in videos]
                
                # Proceed to download
                print(f"\n{'='*80}")
                print(f"Starting download of {len(selected_urls)} video(s)...")
                print(f"{'='*80}")
                
                output_path = 'downloads'
                os.makedirs(output_path, exist_ok=True)
                
                success_count = 0
                for i, url in enumerate(selected_urls, 1):
                    print(f"\n[{i}/{len(selected_urls)}]")
                    print(f"URL to download: {url}")
                    
                    # Validate URL format
                    if not url or url == "Error extracting URL":
                        print("✗ Invalid URL, skipping...")
                        continue
                    
                    if download_audio(url, output_path):
                        success_count += 1
                
                # Summary
                print(f"\n{'='*80}")
                print(f"DOWNLOAD SUMMARY")
                print(f"{'='*80}")
                print(f"Total: {len(selected_urls)} videos")
                print(f"Success: {success_count}")
                print(f"Failed: {len(selected_urls) - success_count}")
                print(f"Location: {output_path}/")
                print(f"{'='*80}\n")
        return
    
    # Download mode (default)
    print("\nDownload Mode")
    print("-" * 80)
    print("Options:")
    print("1. Enter channel URL (auto-fetch videos)")
    print("2. Enter individual video URLs")
    print("="*80 + "\n")
    
    # Ask how many videos to download
    try:
        max_videos = int(input("How many videos to download? (default: 2): ").strip() or "2")
        if max_videos < 1:
            max_videos = 2
    except ValueError:
        max_videos = 2
    
    print(f"\n✓ Will download {max_videos} video(s)\n")
    
    # Create output directory
    output_path = 'downloads'
    os.makedirs(output_path, exist_ok=True)
    
    # Get input
    input_url = input("Enter YouTube channel URL or video URL: ").strip()
    
    if not input_url:
        print("\n✗ No URL provided!")
        return
    
    # Check if it's a channel URL
    urls = []
    if '@' in input_url or '/c/' in input_url or '/channel/' in input_url or '/user/' in input_url:
        # It's a channel URL
        urls = get_channel_videos(input_url, max_videos)
        if not urls:
            print("\n✗ Could not fetch videos from channel!")
            return
    elif 'youtube.com/watch' in input_url or 'youtu.be/' in input_url:
        # It's a single video URL
        urls.append(input_url)
        
        # If they want more than 1 video, ask for more URLs
        if max_videos > 1:
            print(f"\nPaste {max_videos - 1} more video URL(s) (press Enter twice to finish):\n")
            while len(urls) < max_videos:
                url = input().strip()
                if not url:
                    break
                if 'youtube.com/watch' in url or 'youtu.be/' in url:
                    urls.append(url)
                else:
                    print(f"  ⚠ Skipped invalid URL: {url}")
    else:
        print("\n✗ Invalid URL format!")
        return
    
    if not urls:
        print("\n✗ No valid URLs provided!")
        return
    
    # Limit to max_videos
    urls = urls[:max_videos]
    
    print(f"\n{'='*60}")
    print(f"Found {len(urls)} video(s) to download")
    print(f"{'='*60}")
    
    # Download each video
    success_count = 0
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}]")
        if download_audio(url, output_path):
            success_count += 1
    
    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total: {len(urls)} videos")
    print(f"Success: {success_count}")
    print(f"Failed: {len(urls) - success_count}")
    print(f"Location: {output_path}/")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Interrupted by user")
    except Exception as e:
        print(f"\n✗ Error: {e}")
