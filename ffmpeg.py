import subprocess

#subprocess.run(["ffmpeg", "-i", "input/test.webm", "-vcodec", "copy", "input/test_trans.mp4"])

#subprocess.run(["ffmpeg", "-i", "input/test1.mp4", "-vcodec", "mjpeg", "input/image_%03d.jpg"])

subprocess.run(["ffmpeg", "-r", "30", "-i", "cartoonized_images/%06d.jpg", "-vcodec", "libx264", "-r", "60", "cartoonized_images/out.mp4"])