import os
from moviepy.editor import VideoFileClip

def extract_audio_from_mp4(input_file_path, output_file_path):
    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"Input file {input_file_path} does not exist.")  # Print a message indicating that the input file does not exist
        return  # Exit the function
    
    try:
        # Attempt to create a VideoFileClip object from the input file
        clip = VideoFileClip(input_file_path)
        # Write the audio from the clip to the output file
        clip.audio.write_audiofile(output_file_path)
        print(f"Audio extracted successfully and saved as {output_file_path}")  # Print a success message
    except Exception as e:
        print(f"Error extracting audio: {str(e)}")  # Print an error message if an exception occurs

input_file_path = r"specify the path to the input file here"
output_file_path = r"output.wav"
extract_audio_from_mp4(input_file_path, output_file_path)