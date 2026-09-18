import Foundation

let path = "/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner/Ders Notları/Yetişkin Hastalıkları Uygulaması/02_Sunumlar/Konu1_Obezite_Sunum.html"
let url = URL(fileURLWithPath: path)

guard let versions = NSFileVersion.otherVersionsOfItem(at: url) else {
    print("No other versions found.")
    exit(0)
}

print("Found \(versions.count) versions:")
for (index, version) in versions.enumerated() {
    print("[\(index)] Date: \(String(describing: version.modificationDate))")
    let destPath = "/Users/canerozyildirim/.gemini/antigravity/brain/01100986-60f3-414a-aebe-02298ee852cd/scratch/Konu1_version_\(index).html"
    let destURL = URL(fileURLWithPath: destPath)
    do {
        if FileManager.default.fileExists(atPath: destPath) {
            try FileManager.default.removeItem(at: destURL)
        }
        try FileManager.default.copyItem(at: version.url, to: destURL)
        print(" -> Copied to \(destPath)")
    } catch {
        print(" -> Error copying version \(index): \(error)")
    }
}
