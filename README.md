# Image Captioning Tool with OpenAI GPT-4

This Python tool is designed to generate captions for a set of images, utilizing the advanced capabilities of OpenAI's GPT-4 Vision API. It can handle image collections either from a ZIP file or a directory. The tool offers flexibility in captioning, providing options to describe images directly or in a creative style, like "in the style of Family Guy."

## Key Features

- Processes images from ZIP files or directories.
- Utilizes OpenAI's GPT-4 Vision API for caption generation.
- Supports custom caption formats, including style-based descriptions (e.g., "in the style of TOK").
- Captions are conveniently saved in a CSV file for easy access and reference.

![Example Image](https://1800nick.com/cap.jpg)

## System Requirements

- Python 3
- An active OpenAI API key with GPT-4 Vision API access.
- Necessary Python libraries: `requests`, `imgcat`.

## Setup Instructions

1. Clone the GitHub repository:

   ```
   git clone https://github.com/ghostofpokemon/oCaption.git
   ```

2. Change to the tool's directory:

   ```
   cd oCaption
   ```

3. Install the required Python dependencies:

   ```
   pip install requests imgcat
   ```

## How to Use

Set your OpenAI API key as an environment variable:

```
export OPENAI_API_KEY="Your-API-Key-Here"
```

Launch the tool with Python:

```
python3 oCaption.py
```

Follow the prompts to input the path to your image folder or ZIP file, specify the TOK value (such as "TOK" or "Family Guy"), and choose a caption prefix if needed.

## Output Details

The tool generates detailed captions for each processed image, saving them in a `caption.csv` file located in the current working directory. The captions follow the format "a photo of [subject]" or "in the style of [TOK]" based on your preference.

## Contributing to the Project

We welcome contributions! To propose changes, please use the standard GitHub pull request process.

## License Information

This tool is distributed under the [MIT License](LICENSE).

## Support and Contact

For queries or feedback, feel free to open an issue in the GitHub repository.