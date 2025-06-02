# downloadanymusic
Sure! Here's a clean and simple `README.md` file tailored for your **YouTube Music Downloader (without FFmpeg)** project:

---

## 🎵 YouTube Music Downloader (No FFmpeg Required)

A simple Python script to download the best available audio from YouTube videos using [`yt_dlp`](https://github.com/yt-dlp/yt-dlp). This version **does not use FFmpeg**, so audio is downloaded in its original format (usually `.webm` or `.m4a`).

---

### 📦 Features

* ✅ Downloads best-quality audio from a YouTube video
* 🚫 No FFmpeg required
* 🎧 Saves file with the original video title
* 🛡️ Simple error handling and input validation

---

### 💻 Requirements

* Python 3.7 or higher
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

> FFmpeg is **not required** for this script.

---

### 🔧 Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/yt-music-downloader.git
   cd yt-music-downloader
   ```

2. **Install dependencies**

   ```bash
   pip install yt-dlp
   ```

---

### 🚀 Usage

Run the script:

```bash
python download_music.py
```

Then, paste the YouTube video URL when prompted.

---

### 📁 Output

* Audio files will be saved in the same directory.
* File names will match the video title.
* Formats may vary depending on YouTube's source (e.g., `.webm`, `.m4a`).

---

### 📝 Example

```
🎵 Enter the YouTube music URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
🔍 Downloading best available audio (no conversion)...
✅ Audio downloaded successfully!
```

---

### ⚠️ Notes

* This tool downloads **only individual videos**, not playlists.
* If you want MP3 output, you must use FFmpeg (not included in this version).
* Download responsibly and ensure you respect YouTube's Terms of Service.

---

### 📄 License

This project is licensed under the MIT License.
