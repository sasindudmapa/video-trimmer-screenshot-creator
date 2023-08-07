import os
from moviepy.editor import *
from PIL import Image
import shutil


video_default_path = './videos'
screenshot_default_path = './screenshots'

def get_video_path():
    video_path_list = []

    video_list = os.listdir(f'{video_default_path}')
    
    for video_name in video_list:
        vid_path = f'{video_default_path}/{video_name}'
        video_path_list.append(vid_path)
        
    return video_path_list
    
def take_screenshot(video_path, timestamps):
    video_name = video_path.split("/")[-1]
    video_file = VideoFileClip(video_path)

    screenshot_dir = f'{screenshot_default_path}/{video_name}'
    os.makedirs(screenshot_dir, exist_ok=True)


    for timestamp in timestamps:
        screenshot_name = f'{screenshot_dir}/{timestamp}.png'
        frame = video_file.get_frame(timestamp)
        Image.fromarray(frame).save(screenshot_name)


video_paths = get_video_path()

for video_path in video_paths:
    vi_name = video_path.split("/")[-1]
    print(f"video is {vi_name}")
    timestamps = []

    taking_input_timestamps = True

    while taking_input_timestamps:
        screenshot_time = input("timestamp or type n to close: ")
        if(screenshot_time == "n"):
            taking_input_timestamps = False
        else:
            timestamps.append(int(screenshot_time))


    take_screenshot(video_path, timestamps)






    


