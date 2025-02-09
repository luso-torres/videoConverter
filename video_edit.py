from moviepy import VideoFileClip, concatenate_videoclips
from moviepy.video.fx import FadeIn, FadeOut

# Load the video file and apply effects
clip1 = VideoFileClip("videos/gnu_result.mkv").subclipped(10, 20) 
clip1 = FadeIn(1).apply(clip1)
# clip1.FadeIn.apply(1)
# FadeOut(1)
clip1 = FadeOut(1).apply(clip1)

final_clip = concatenate_videoclips([clip1])
final_clip.write_videofile("final_clip.mp4")
