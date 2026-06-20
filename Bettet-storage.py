import os
import shutil

SOURCE_FOLDER = "/storage/emulated/0/My code/Ai"

# ====== مجلدات التنظيم ======
CODES_FOLDER = os.path.join(SOURCE_FOLDER, "CODES")
IMAGES_FOLDER = os.path.join(SOURCE_FOLDER, "IMAGES")
OTHERS_FOLDER = os.path.join(SOURCE_FOLDER, "OTHERS")

# ====== 40 لغة برمجة ======
CODE_TYPES = {
    "python": [".py", ".pyw", ".pyi"],
    "javascript": [".js", ".mjs", ".cjs"],
    "typescript": [".ts", ".tsx"],
    "html": [".html", ".htm", ".xhtml"],
    "css": [".css", ".scss", ".sass", ".less"],
    "php": [".php", ".phtml"],
    "java": [".java", ".jsp"],
    "c": [".c", ".h"],
    "cpp": [".cpp", ".cxx", ".cc", ".hpp", ".hxx"],
    "csharp": [".cs", ".csx"],
    "go": [".go"],
    "rust": [".rs"],
    "swift": [".swift"],
    "kotlin": [".kt", ".kts"],
    "dart": [".dart"],
    "ruby": [".rb", ".erb"],
    "perl": [".pl", ".pm"],
    "lua": [".lua"],
    "r": [".r", ".rmd"],
    "matlab": [".m"],
    "shell": [".sh", ".bash", ".zsh", ".fish"],
    "powershell": [".ps1", ".psm1"],
    "sql": [".sql"],
    "json": [".json", ".jsonl"],
    "yaml": [".yml", ".yaml"],
    "xml": [".xml", ".svg"],
    "markdown": [".md", ".mdx"],
    "gdscript": [".gd"],
    "kotlin": [".kt", ".kts"],
    "scala": [".scala", ".sc"],
    "elixir": [".ex", ".exs"],
    "erlang": [".erl", ".hrl"],
    "clojure": [".clj", ".cljs"],
    "haskell": [".hs"],
    "julia": [".jl"],
    "groovy": [".groovy", ".gvy"],
    "objectivec": [".m", ".mm"],
    "assembly": [".asm", ".s", ".nasm"],
    "vba": [".vba", ".vbs"],
    "pascal": [".pas", ".pp"]
}

# ====== 20 نوع صور ======
IMAGE_TYPES = [
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg", ".ico",
    ".tiff", ".tif", ".psd", ".ai", ".eps", ".raw", ".cr2", ".nef",
    ".orf", ".sr2", ".heic", ".avif"
]

def get_code_type(ext):
    ext = ext.lower()
    for folder, exts in CODE_TYPES.items():
        if ext in exts:
            return folder
    return None

def is_file_valid(path):
    try:
        return os.path.getsize(path) > 0
    except:
        return False

def safe_move(src, dst_folder):
    os.makedirs(dst_folder, exist_ok=True)

    filename = os.path.basename(src)
    dst = os.path.join(dst_folder, filename)

    # تجنب الكتابة فوق الملفات الموجودة
    counter = 1
    base, ext = os.path.splitext(filename)
    while os.path.exists(dst):
        dst = os.path.join(dst_folder, f"{base}_{counter}{ext}")
        counter += 1

    shutil.move(src, dst)
    return dst

def organize():
    print("🚀 Starting ERNX File Organizer v2...")

    os.makedirs(CODES_FOLDER, exist_ok=True)
    os.makedirs(IMAGES_FOLDER, exist_ok=True)
    os.makedirs(OTHERS_FOLDER, exist_ok=True)

    for root, dirs, files in os.walk(SOURCE_FOLDER):
        # تجاهل مجلدات النظام
        if root in [CODES_FOLDER, IMAGES_FOLDER, OTHERS_FOLDER]:
            continue

        for file in files:
            file_path = os.path.join(root, file)

            # تجاهل السكريبت نفسه
            if file_path == os.path.abspath(__file__):
                continue

            ext = os.path.splitext(file)[1].lower()

            if not is_file_valid(file_path):
                print(f"⏭ Skipped empty: {file}")
                continue

            # الصور
            if ext in IMAGE_TYPES:
                dst = safe_move(file_path, IMAGES_FOLDER)
                print(f"🖼 IMG -> {file}")
                continue

            # الأكواد
            code_type = get_code_type(ext)
            if code_type:
                target_dir = os.path.join(CODES_FOLDER, code_type)
                dst = safe_move(file_path, target_dir)
                print(f"💻 CODE -> {file} -> {code_type}")
                continue

            # الباقي
            dst = safe_move(file_path, OTHERS_FOLDER)
            print(f"📦 OTHER -> {file}")

    print("\n✅ DONE: Organization complete!")

if __name__ == "__main__":
    organize()
