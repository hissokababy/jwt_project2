import ffmpeg
import os

from project_video_hosting.settings import VIDEO_RESOLUTIONS

def create_video_segments(video):
    video = 'cool_magnus.mp4'

    resolutions = VIDEO_RESOLUTIONS

    for name, resolution in resolutions.items():
        output_path = f'{name}.m3u8'
        (
            ffmpeg.output
            .input(video)
            .output(output_path,
                    format='hls',
                    hls_time=10,
                    hls_playlist_type='vod',
                    hls_segment_filename=f'{name}_%03d.ts',
                    vf=f'scale={resolution}',
                    **{'b:v': '2000k', 'maxrate': '2140k', 'bufsize': '3000k'}  # Example bitrate settings
                )
            .run()
        )

