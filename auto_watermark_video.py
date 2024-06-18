import os
import cv2
import numpy as np

def add_text_with_opacity(frame, text, position, font, font_size, color, opacity):
    """
    Add text with opacity to a frame.

    Args:
        frame (numpy.ndarray): Input frame.
        text (str): Text to be added.
        position (tuple): Position of the text (x, y).
        font (int): Font type (OpenCV constant).
        font_size (float): Font scale factor.
        color (tuple): Text color in BGR format.
        opacity (float): Opacity of the text (0.0 to 1.0).

    Returns:
        numpy.ndarray: Frame with added text and opacity.
    """
    overlay = frame.copy()
    output = frame.copy()

    # Convert color to BGR
    color_bgr = (color[2], color[1], color[0])

    # Put text on the overlay image
    cv2.putText(overlay, text, position, font, font_size, color_bgr, thickness=2, lineType=cv2.LINE_AA)

    # Add overlay to the frame with opacity
    cv2.addWeighted(overlay, opacity, output, 1 - opacity, 0, output)
    return output

def process_videos_in_folder(folder_path, text, position, font_size, color, opacity):
    """
    Process all videos in the given folder by adding text with opacity.

    Args:
        folder_path (str): Path to the folder containing video files.
        text (str): Text to be added.
        position (tuple): Position of the text (x, y).
        font_size (float): Font scale factor.
        color (tuple): Text color in BGR format.
        opacity (float): Opacity of the text (0.0 to 1.0).
    """
    # Check if the output folder exists, if not, create it
    output_folder = os.path.join(folder_path, "output")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"output_{filename}")
            print(f"Processing {video_path} and saving as {output_path}")

            # Read the video
            cap = cv2.VideoCapture(video_path)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, int(cap.get(cv2.CAP_PROP_FPS)),
                                  (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                   int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

            font = cv2.FONT_HERSHEY_SIMPLEX

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                frame = add_text_with_opacity(frame, text, position, font, font_size, color, opacity)
                out.write(frame)

            cap.release()
            out.release()

# Parameters
folder_path = 'path/to/your/video/folder'  # Replace this with the path to your video folder
text = 'Your Text'  # The text you want to add
position = (50, 50)  # (x, y) position of the text
font_size = 1  # Font scale factor
color = (255, 255, 255)  # Text 
