import base64
import os
import re

# Paths
IMAGE_PATH = "/Users/carltilton/.gemini/antigravity/brain/6b3b64f4-bf77-46f2-8a96-24a86d66f4c3/uploaded_image_1769487578475.jpg"
HTML_PATH = "index.html"

def inject_vial():
    # 1. Read and Encode Image
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: Image not found at {IMAGE_PATH}")
        return

    with open(IMAGE_PATH, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        # Use jpeg mime type since the source is jpg
        base64_src = f"data:image/jpeg;base64,{encoded_string}"
    
    print(f"Encoded image size: {len(base64_src)} characters")

    # 2. Read HTML
    with open(HTML_PATH, "r", encoding="utf-8") as html_file:
        content = html_file.read()

    # 3. Replace Constant
    # Regex to find: const DEFAULT_VIAL_BASE64 = "..."
    # We use a non-greedy match .*? inside quotes, but base64 can be long so we just match until the closing quote
    pattern = r'(const DEFAULT_VIAL_BASE64 = ")(.*?)(")'
    
    # Check if pattern exists first
    if not re.search(pattern, content):
        print("Error: Could not find DEFAULT_VIAL_BASE64 constant in HTML")
        return

    new_content = re.sub(pattern, f'\\g<1>{base64_src}\\g<3>', content, count=1)

    # 4. Write HTML
    with open(HTML_PATH, "w", encoding="utf-8") as html_file:
        html_file.write(new_content)

    print("Successfully injected new default vial image into index.html")

if __name__ == "__main__":
    inject_vial()
