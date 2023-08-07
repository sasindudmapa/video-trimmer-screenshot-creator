import os
from moviepy.editor import *
import shutil


video_default_path = './videos'

def get_video_path():
    video_path_list = []

    video_list = os.listdir(f'{video_default_path}')
    
    for video_name in video_list:
        vid_path = f'{video_default_path}/{video_name}'
        video_path_list.append(vid_path)
        
    return video_path_list
    




def trim_video(video_path):
    video_name = video_path.split('/')[-1]
    video_file = VideoFileClip(video_path)
    video_len = video_file.duration
    trimming_seg_len = int(video_len/number_of_segs)
    edited_vid_seg_len = clip_len

    trimmed_parts = []


    # print(trimming_seg_len, edited_vid_seg_len)
    for clip_num in range(number_of_segs):
        start = clip_num * trimming_seg_len
        end = start + edited_vid_seg_len
        tem_clip = video_file.subclip(start, end)
        trimmed_parts.append(tem_clip)

    # print(video_name)

    final_clip = concatenate_videoclips(trimmed_parts)
    final_clip.write_videofile(f'./edited/{video_name}')



number_of_segs = int(input("The number of parts that the video should be cropped into: "))
clip_len = int(input("Length of a single video clip(seconds): "))

video_paths = get_video_path()

for video_path in video_paths:
    trim_video(video_path)






    


