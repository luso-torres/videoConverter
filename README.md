# Video Converter

Through the library moviepy, this project was designed to test some of the core functionalities of video editing, with each function explained below.

## Adding your file

In order to edit the video, you should load it with the function VideoFileClip

```python
from moviepy import VideoFileClip

clip = VideoFileClip("path\to\your\file")
```


## Cutting a video

Cuts can be made by inserting the file with the command:

```python
clip_cut = clip.subclipped(10,20)
```
where subclipped is a functions that has arguments the initial time and final time.

## Video Preview

After reading the file, you can check the content using the method preview:
```python
clip.preview()
```

## Adding FadeIn and FadeOut

If you are interest to insert transitions to your clip, you can do this by importing the functions FadeIn and FadeOut:

```python
from moviepy.video.fx import FadeIn,FadeOut
clip_intro = FadeIn(1).apply(clip)
clip_end = FadeOut(1).apply(clip)
```
Here, you must insert the transition time (0 to 1 second) and use the method apply to clip.

## Saving the file

To save the file, you have to import the function concate_videoclips:

```python
from moviepy import VideoFileClip, concatenate_videoclips
final_clip = clip_end
final_clip.write_videofile("combined.mp4")  
```
Here, the method requires as argument the name of the output file.
