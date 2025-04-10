from beachcams.classes.EntryPoint import EntryPoint
from beachcams.classes.ImageProvider import ImageProvider
from yt_dlp import YoutubeDL
from beachcams.utils import download_m3u8
import os

class YoutubeImageProvider(ImageProvider):
    
    def run(self, entryPoint: EntryPoint):
        print(entryPoint.url)
        with YoutubeDL({'format': 'bestvideo/best'}) as ydl:
            result = ydl.extract_info(
                entryPoint.url,
                download=False  # We just want to extract the info
            )
        file_path = entryPoint.generate_filename()
        [video_file_path, image_file_path] = download_m3u8(
            stream_url=result["url"],     # Get first m3u8 as valid video
            filepath_without_extension=file_path
        )
        #remove mp4 data
        if os.path.exists(video_file_path):
            os.remove(video_file_path)
        return image_file_path
        