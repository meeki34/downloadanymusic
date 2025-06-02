import yt_dlp

def download_yt_music(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': '%(title)s.%(ext)s',  # Save file with the title name
        'quiet': False,
        'no_warnings': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("🔍 Downloading best available audio (no conversion)...")
            ydl.download([url])
            print("✅ Audio downloaded successfully!")
    except Exception as e:
        print(f"❌ Download failed: {e}")

if __name__ == "__main__":
    url = input("🎵 Enter the YouTube music URL: ").strip()
    if url.startswith("http"):
        download_yt_music(url)
    else:
        print("❗ Please enter a valid YouTube URL.")
