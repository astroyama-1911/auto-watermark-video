# Auto Watermark Video
This Python script allows you to add text with opacity to videos using OpenCV and export the modified videos.
This can be useful for adding watermarks, subtitles, or any other textual overlay with transparency.

## Requirements
- [Python 3.x](https://www.python.org)
- OpenCV (opencv-python) (`pip install opencv-python`)

## Usage
- Clone this repository or download the video_text_overlay.py script.
- Open the terminal or command prompt.
- Navigate to the directory containing the video_text_overlay.py script.
- Run the script with the following command :
`python video_text_overlay.py`

## Parameters
You can customize the following parameters in the script:

`folder_path` : Path to the folder containing your video files.

`text` : The text you want to overlay on the videos.

`position` : Position of the text (x, y) coordinates on the video.

`font_size` : Font size of the text.

`color` : Color of the text in BGR format (e.g., white is (255, 255, 255)).

`opacity` : Opacity of the text (0.0 to 1.0).

### Example :

```
folder_path = 'path/to/your/video/folder' 
text = 'Your Text' 
position = (50, 50)  # (x, y) 
font_size = 1  # Scale factor for font size 
color = (255, 255, 255)  # White color 
opacity = 0.5  # 50% opacity 
```

## Note
- Make sure your video files are in the supported format (e.g., .mp4).
- The script will save the modified videos in the same folder with a prefix output_.
