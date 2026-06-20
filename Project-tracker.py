import os

SOURCE_FOLDER = "/storage/emulated/0/My code/Ai"

def get_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.exists(fp):
                total += os.path.getsize(fp)
    return total

def count_files(path):
    count = 0
    for root, dirs, files in os.walk(path):
        count += len(files)
    return count

def get_folder_stats(folder):
    stats = {}
    for root, dirs, files in os.walk(folder):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            stats[ext] = stats.get(ext, 0) + 1
    return stats

def pretty_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} TB"

def main():
    print("\n===== 📊 ERNX PROJECT DASHBOARD =====\n")

    total_files = count_files(SOURCE_FOLDER)
    total_size = get_size(SOURCE_FOLDER)
    stats = get_folder_stats(SOURCE_FOLDER)

    print(f"📁 Folder: {SOURCE_FOLDER}")
    print(f"📄 Total Files: {total_files}")
    print(f"💾 Total Size: {pretty_size(total_size)}\n")

    print("📊 File Types Breakdown:")
    for ext, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        name = ext if ext else "no-extension"
        print(f"  {name}: {count}")

    print("\n====================================\n")

if __name__ == "__main__":
    main()
