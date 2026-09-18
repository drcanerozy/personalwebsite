import objc
from Foundation import NSFileVersion, NSURL

path = "/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner/Dersler/Yetişkinlerde Beslenme Tedavisi Uygulaması/Sunumlar/Konu1_Obezite_Sunum.html"
url = NSURL.fileURLWithPath_(path)

versions = NSFileVersion.otherVersionsOfItemAtURL_(url)
if not versions:
    print("No other versions found.")
else:
    for i, v in enumerate(versions):
        print(f"[{i}] {v.modificationDate()}")
        dest_url = NSURL.fileURLWithPath_(f"/Users/canerozyildirim/.gemini/antigravity/brain/01100986-60f3-414a-aebe-02298ee852cd/scratch/Konu1_version_{i}.html")
        from Foundation import NSFileManager
        fm = NSFileManager.defaultManager()
        fm.removeItemAtURL_error_(dest_url, None)
        success, err = fm.copyItemAtURL_toURL_error_(v.URL(), dest_url, None)
        if success:
            print(f" -> Copied version {i}")
        else:
            print(f" -> Failed to copy version {i}: {err}")
