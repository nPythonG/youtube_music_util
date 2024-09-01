# pip install -U "yt-dlp[default]"
#yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=2wJ5Mm_ij8g --ffmpeg-location D:\dev\ffmpeg-2024-08-28-git-b730defd52-essentials_build\bin

import subprocess
import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Example script using argparse.")

    # Add arguments    
    parser.add_argument('--url', type=str, help='Video url')
    parser.add_argument('--playlist', action='store_true', help='Increase output verbosity')
    parser.add_argument('--dir', type=str, help='Audio folder')

    # Parse the arguments
    args = parser.parse_args()

    video_url = args.url
    download_path = args.dir if args.dir else 'audios'
    ffmpeg_path = 'D:\\dev\\ffmpeg-2024-08-28-git-b730defd52-essentials_build\\bin'

    cmd_list = ['yt-dlp', '-x', '--audio-format', 'mp3', f'{video_url}' ,'-o', f'{download_path}/%(title)s.%(ext)s', '--ffmpeg-location', ffmpeg_path]
    if args.playlist:
        cmd_list.append('--yes-playlist')
    else:
        cmd_list.append('--no-playlist')
    
    # Download video using yt-dlp
    subprocess.run(cmd_list)

    print("Download completed!")


if __name__ == "__main__":
    main()



