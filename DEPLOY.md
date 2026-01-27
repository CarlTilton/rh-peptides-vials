# Deployment Instructions

This **Vial Labeler Tool** is designed as a portable, single-file web application (`index.html`). This architecture ensures maximum compatibility, zero-build setup, and easy portability.

## Deployment Options

### Option 1: Static Web Hosting (Recommended for Sharing)
You can deploy this tool to any static hosting provider for free.

**Netlify / Vercel / GitHub Pages / Cloudflare Pages:**
1.  **Drag and Drop**: For Netlify, simply drag the folder containing `index.html` into their "Sites" dashboard. It will deploy instantly.
2.  **Git Integration**: Push this repository to GitHub/GitLab. Connect your repository to Vercel or Cloudflare Pages. Set the "Build Command" to (leave empty) and "Output Directory" to (leave empty or use default).

### Option 2: Local Use
Since the application has **zero dependencies** and no build step:
1.  Simply double-click `index.html` to open it in your browser (Chrome, Safari, Firefox, Edge).
2.  **Note**: We have optimized the tool to work perfectly even with the `file://` protocol (which often blocks image exports due to security). Features like "Save Image" and "Copy Config" are fully compatible with local usage.

## Development Notes

### Changing the Default Vial Image
The default vial image displayed on load is embedded directly into `index.html` as a Base64 string to prevent "tainted canvas" security errors.

To update this image:
1.  Place your new image (JPG/PNG) in the project folder.
2.  Use the provided Python utility `inject_new_vial.py` (adjust the `IMAGE_PATH` variable inside if needed).
3.  Run `python3 inject_new_vial.py`.
4.  This will automatically re-encode and update `index.html`.

### Dependencies
- **Konva.js**: Loaded via CDN (`https://unpkg.com/konva@9/konva.min.js`). If you need offline support, download this file, place it in the folder, and update the `<script>` src tag in `index.html`.
