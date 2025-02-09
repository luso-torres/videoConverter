# import moviepy.editor as mp
# clip1 = mp.VideoFileClip("videos/gnu_result.mkv").subclip(10, 20)
# clip1.preview()
from moviepy import VideoFileClip, concatenate_videoclips, vfx
from moviepy.video.fx import FadeIn,FadeOut


clip1 = VideoFileClip("videos\gnu_result.mkv").subclipped(10,20)
clip1 = FadeIn(clip1,1)
clip1 = FadeOut(clip1,1)
clip1.preview()
combined = concatenate_videoclips([clip1])
combined.write_videofile("combined.mp4")
#clip2 = VideoFileClip("two.mp4").subclip