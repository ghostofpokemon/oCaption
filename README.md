# Image Captioning Script with OpenAI GPT-4

This Python script processes a collection of images (either from a zip file or a folder) and generates captions using OpenAI's GPT-4 Vision API. The captions are generated in a specific format, either describing the content of the image directly or in a specified style (e.g., "in the style of Family Guy").

## Features

- Process images from a zip file or a directory.
- Generate captions using OpenAI's GPT-4 Vision API.
- Customizable caption format, including the ability to specify a style (e.g., "in the style of TOK").
- Output captions are saved to a CSV file.

## Requirements

- Python 3
- OpenAI API key with access to GPT-4 Vision API
- Required Python packages: `requests`, `imgcat`

## Installation

1. Clone the repository:

git clone https://github.com/ghostofpokemon/oCaption.git


2. Navigate to the project directory:

cd image-captioning

3. Install the required Python packages:

pip install requests imgcat


## Usage

Run the script using Python:

python3 zipCaption.py


When prompted, enter the path to the zip file or image folder, the TOK value (e.g., "TOK", "Family Guy"), and the caption prefix if needed.

## Output

The script will generate captions for each image and save them in a file named `caption.csv` in the current directory. The format of the captions is either "a photo of [subject]" or "in the style of [TOK]".

## Contributing

Contributions to the project are welcome. Please follow the standard GitHub pull request process to propose changes.

## License

[MIT License](LICENSE)

## Contact

For any questions or comments, please open an issue in the GitHub repository.