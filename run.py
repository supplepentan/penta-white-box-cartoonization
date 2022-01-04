import os
import shutil
from cartoonize import cartoonize
import cv2
import subprocess
 
# 既に test_images フォルダーがあれば削除し、test_images フォルダーを作る
if os.path.isdir('test_images'):
    shutil.rmtree('test_images')
os.makedirs('test_images', exist_ok=True)
if os.path.isdir('cartoonized_images'):
    shutil.rmtree('cartoonized_images')
os.makedirs('cartoonized_images', exist_ok=True)
 
def video_2_images(video_file= './test_video/test1.mp4',   # ビデオの指定
                   image_dir='./test_images/', 
                   image_file='%s.jpg'):  
 
    # Initial setting
    i = 0
    interval = 1
    length = 300000  # 最大フレーム数
    
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()  
        if flag == False:  
                break
        if i == length*interval:
                break
        if i % interval == 0:    
           cv2.imwrite(image_dir+image_file % str(int(i/interval)).zfill(6), frame)
        i += 1 
    cap.release()
    subprocess.run(["python", "cartoonize.py"])
    subprocess.run(["python", "ffmpeg.py"])
 
def main():
    video_2_images()
    
if __name__ == '__main__':
    main()