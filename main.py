from yt_dlp import YoutubeDL

# Replace with your YouTube playlist or mix URL 
mix_url = 'https://www.youtube.com/playlist?list=PL4n8lyhIjfuPxeT3JIk1lmtBl4H6f2pta'

# Set up the options to extract video IDs
ydl_opts = {
    'extract_flat': True,
    'skip_download': True,
}

with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(mix_url, download=False)
    video_entries = info_dict.get('entries', [])
    # video_entriesx = []
    # for n in range(11,20) :
    #     video_entriesx.append(video_entries[n])
    # video_ids = [entry.get('id') for entry in video_entriesx]
    video_ids = [entry.get('id') for entry in video_entries]

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=v-i13jGBQEA'])

for video_id in video_ids:
    print(video_id)
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v='+video_id])