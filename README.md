
```markdown
# Video Frame Extraction Script

This script extracts individual frames from a video file and saves them as image files. It uses the OpenCV library to achieve this.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)

## Usage

1. Place the video file (`Video.mp4`) in the same directory as this script.
2. Create a folder named `img` in the same directory. This is where the extracted frames will be saved.
3. Run the script using the following command:

   ```bash
   python extract_frames.py
   ```

4. The script will process the video and save frames as PNG images in the `img` folder.
5. The script will print messages indicating the progress.

## Important Notes

- Ensure the video file is supported by OpenCV (common formats like MP4, AVI, and MOV are generally supported).
- The script assumes that the video file is named `Video.mp4`. You can modify the script to use a different file name if needed.
- Frames are saved as PNG images to avoid additional compression losses. You can adjust the file extension in the script if desired.

## License

This project is licensed under the MIT License

