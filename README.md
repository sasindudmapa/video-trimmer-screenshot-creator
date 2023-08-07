# Video Trimmer and Screenshot Creator

The Video Trimmer and Screenshot Creator is a Python project that enables users to manipulate videos by trimming them into segments and generating screenshots at specific times. This tool simplifies video editing and screenshot creation, making it ideal for creating trailers or capturing frames from multiple videos with ease.

## Features

- **Video Trimming:**

  - Cut a long video into multiple segments.
  - Define the number of segments and their lengths.
  - Automatically create a new, smaller video from the segments.
  - Save the resulting video in the "edited" folder.

- **Screenshot Generation:**
  - Capture screenshots from videos at specified times.
  - Store screenshots in a single file with the video's name.
  - Save the collection of screenshots in the "screenshots" folder.

## Getting Started

### Prerequisites

- Python 3.x should be installed on your system.
- Required Python libraries (e.g., OpenCV) for video processing and image capture should be installed.

### Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/sasindudmapa/video-trimmer-screenshot-creator.git
   cd video-trimmer-screenshot-creator
   ```

## Usage

### Video Trimming

1. Run "trimmer.py" from the terminal or command prompt.

2. Provide the number of segments for the full video.

3. Enter the length of each video segment.

4. The script will automatically cut the video into segments and save the smaller video in the "edited" folder.

### Screenshot Generation

1. Execute "screenshot.py" from the terminal or command prompt.

2. Supply the times in the video when screenshots should be taken (comma-separated).

3. The script captures the screenshots and saves them in a single file with the video's name in the "screenshots" folder.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
