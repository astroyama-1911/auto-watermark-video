import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings

# Change the path to the directory where ImageMagick is installed
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})

def add_text_with_opacity(video_path, output_path, text, position, font_size, color, opacity, stroke_color, stroke_width):
    try:
        # Load the video
        video = VideoFileClip(video_path)
        
        # Create a text clip with stroke
        text_clip = TextClip(text, fontsize=font_size, color=color, font='Arial-Bold',
                             stroke_color=stroke_color, stroke_width=stroke_width)
        
        # Set the opacity
        text_clip = text_clip.set_opacity(opacity)
        
        # Position the text
        text_clip = text_clip.set_position(position).set_duration(video.duration)
        
        # Create the final video with the text
        final_video = CompositeVideoClip([video, text_clip])
        
        # Export the video with audio encoded in AAC
        final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
    except Exception as e:
        print(f"Error processing video {video_path}: {e}")

def process_videos_in_folder(folder_path, text, position, font_size, color, opacity, stroke_color, stroke_width):
    # Check if the output folder exists, otherwise create it
    output_folder = os.path.join(folder_path, "output")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"output_{filename}")
            print(f"Processing {video_path} and saving as {output_path}")
            add_text_with_opacity(video_path, output_path, text, position, font_size, color, opacity, stroke_color, stroke_width)

# Function parameters
folder_path = 'path/to/your/video/folder'  # Replace with your folder path containing the videos
text = 'Your Text'  # The text you want to add
position = ('center', 'center')  # Position of the text (e.g., 'center' to center)
font_size = 1  # Font size of the text
color = 'white'  # Text color
opacity = 0.5  # Text opacity (0.5 for 50%)
stroke_color = 'black'  # Outline color
stroke_width = 2  # Outline width
