# Auto Watermark Video
This Python script allows you to add text with opacity to videos using OpenCV and export the modified videos.
This can be useful for adding watermarks, subtitles, or any other textual overlay with transparency.

## Requirements
- [Python 3.x](https://www.python.org)
- [ImageMagick](https://imagemagick.org/archive/binaries/ImageMagick-7.1.1-33-Q16-x64-dll.exe)

## Usage
- Clone this repository. (`git clone https://github.com/astroyama-1911/auto-watermark-video.git`)
- Open the terminal or command prompt.
- Navigate to the repository folder.
- Install the requirements (`pip install -r requirements.txt`)
- Put your videos in the same folder of the script
- Run the script with the following command :
`python auto_watermark_video.py`

## Parameters
You can customize the following parameters in the script:

`folder_path` : Path to the folder containing the MP4 videos.

`text` : The text you want to add as a watermark.

`position` : Position of the text (e.g., ('center', 'center') for center).

`font_size` : Font size of the text.

`color` : Color of the text.

`opacity` : Opacity of the text (e.g., 0.5 for 50%).

`stroke_color` : Color of the text outline.

`stroke_width` : Width of the text outline.

### Example :

```
folder_path = 'C:\\Users\\YourUsername\\Desktop\\videos'  # Replace with your folder path containing the videos
text = 'Your Text'  # The text you want to add
position = ('center', 'center')  # Position of the text
font_size = 23  # Font size of the text
color = 'white'  # Text color
opacity = 0.5  # Text opacity
stroke_color = 'black'  # Outline color
stroke_width = 2  # Outline width
```

## Note
- Make sure your video files are in the supported format (e.g., .mp4).
- The script will save the modified videos in the same folder with a prefix output_.
