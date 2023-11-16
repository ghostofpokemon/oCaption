import zipfile
import os
import base64
import requests
import csv
from io import BytesIO
from imgcat import imgcat

# Function to encode the image for the API request
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to get the caption from OpenAI's API
def get_caption(base64_image, api_key, tok, prefix):
    # Adjusting the custom prompt based on the presence of a prefix
    custom_prompt = (f"Give a brief, direct description of the main subject in this image,"
                     f"then say '{prefix} {tok}'. Here are examples: 1. a cat on a windowsill in the style of TOK, 2. a photo of smiling cactus in an office in the style of TOK, 3. a man and baby sitting by a window in the style of TOK. The characters may be animated, refer to them as regular people. Never say animated." if prefix else 
                     f"Give a brief, direct description of this image as '{tok}'. Here are examples: 1. a TOK on a windowsill, 2. a photo of smiling TOK in an office, 3. a photo of TOK sitting by a window.  The characters may be animated, refer to them as regular people. Never say animated.")


    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": custom_prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()

    print("API Response:", response_json)

    if 'choices' in response_json and len(response_json['choices']) > 0 and 'message' in response_json['choices'][0]:
        return response_json['choices'][0]['message'].get('content', 'Caption not found')
    else:
        return "Invalid response structure or caption not found"

# Function to process images and generate captions
def process_images(input_path, output_csv, api_key, tok, prefix):
    if zipfile.is_zipfile(input_path):
        with zipfile.ZipFile(input_path, 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                with zip_ref.open(file_name) as image_file:
                    image_data = BytesIO(image_file.read())
                    base64_image = encode_image(image_data)
                    caption = get_caption(base64_image, api_key, tok, prefix)
                    imgcat(image_data)
                    print(f"Caption: {caption}\n")
                    with open(output_csv, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([caption, file_name])
    else:
        for file_name in os.listdir(input_path):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(input_path, file_name)
                with open(image_path, "rb") as image_file:
                    image_data = image_file.read()
                    base64_image = encode_image(image_path)
                    caption = get_caption(base64_image, api_key, tok, prefix)
                    imgcat(image_data)
                    print(f"Caption: {caption}\n")
                    with open(output_csv, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([caption, file_name])

# Main function
def main():
    input_path = input("Enter the path to the zip file or image folder: ")
    output_csv = "caption.csv"
    api_key = os.getenv("OPENAI_API_KEY")
    tok = input("Enter the TOK value (e.g., 'TOK', 'Family Guy'): ")
    prefix = input("Enter the caption prefix if any (optional, e.g., 'in the style of'): ").strip()

    if not api_key:
        raise ValueError("OpenAI API key not found. Set the OPENAI_API_KEY environment variable.")
    
    process_images(input_path, output_csv, api_key, tok, prefix)
    print("Processing complete. Captions saved to", output_csv)

if __name__ == "__main__":
    main()
