import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings

# Change the path to the directory where ImageMagick is installed
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})

def add_text_with_opacity(video_path, output_path, text, position, font_size, color, opacity):
    try:
        # Charger la vidéo
        video = VideoFileClip(video_path)
        
        # Créer un clip de texte
        text_clip = TextClip(text, fontsize=font_size, color=color, font='Arial-Bold')
        
        # Ajuster l'opacité
        text_clip = text_clip.set_opacity(opacity)
        
        # Positionner le texte
        text_clip = text_clip.set_position(position).set_duration(video.duration)
        
        # Créer la vidéo finale avec le texte
        final_video = CompositeVideoClip([video, text_clip])
        
        # Exporter la vidéo
        final_video.write_videofile(output_path, codec='libx264')
    except Exception as e:
        print(f"Erreur lors du traitement de la vidéo {video_path}: {e}")

def process_videos_in_folder(folder_path, text, position, font_size, color, opacity):
    # Vérifier si le dossier de sortie existe, sinon le créer
    output_folder = os.path.join(folder_path, "output")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"output_{filename}")
            print(f"Traitement de {video_path} et sauvegarde sous {output_path}")
            add_text_with_opacity(video_path, output_path, text, position, font_size, color, opacity)


# Paramètres de la fonction
folder_path = 'C:\\Users\\Astolfo Oyama\\Desktop\\ajouter watermark video'  # Remplacez ceci par le chemin de votre dossier contenant les vidéos
text = 'https://discord.gg/w9ZShBmMC9'  # Le texte que vous voulez ajouter
position = ('center', 'center')  # Position du texte (par exemple, 'center' pour centrer)
font_size = 20  # Taille de la police du texte
color = 'white'  # Couleur du texte
opacity = 0.2  # Opacité du texte (0.5 pour 50%)

# Traiter toutes les vidéos dans le dossier
process_videos_in_folder(folder_path, text, position, font_size, color, opacity)
