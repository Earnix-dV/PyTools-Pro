import os
import shutil

# =========================
# SOURCE FOLDER
# =========================
SOURCE_FOLDER = "/storage/emulated/0/My code/Ai"

# =========================
# DESTINATION FOLDERS
# =========================
CODES_FOLDER = os.path.join(SOURCE_FOLDER, "CODES")
IMAGES_FOLDER = os.path.join(SOURCE_FOLDER, "IMAGES")
OTHERS_FOLDER = os.path.join(SOURCE_FOLDER, "OTHERS")

# =========================
# CODE TYPES
# =========================
CODE_TYPES = {
    "html": [".html", ".htm"],
    "css": [".css"],
    "js": [".js"],
    "python": [".py"],
    "c": [".c"],
    "cpp": [".cpp"],
    "java": [".java"],
    "php": [".php"],
    "gdscript": [".gd"],
    "json": [".json"],
    "txt": [".txt"],
    "csv": [".csv"],
}

# =========================
# IMAGE TYPES
# =========================
IMAGE_TYPES = [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"]

# =========================
# HELPERS
# =========================
def get_code_type(ext):
    for folder, exts in CODE_TYPES.items():
        if ext.lower() in exts:
            return folder
    return None


def is_valid_file(path):
    try:
        return os.path.getsize(path) > 0
    except:
        return False


def safe_move(src, dst_folder):
    os.makedirs(dst_folder, exist_ok=True)

    filename = os.path.basename(src)
    dst = os.path.join(dst_folder, filename)

    # إذا الملف موجود، نضيف رقم
    counter = 1
    base, ext = os.path.splitext(filename)

    while os.path.exists(dst):
        dst = os.path.join(dst_folder, f"{base}_{counter}{ext}")
        counter += 1

    shutil.move(src, dst)
    return dst


# =========================
# MAIN ORGANIZER
# =========================
def organize():
    print("🚀 Starting ERNX File Organizer...")

    os.makedirs(CODES_FOLDER, exist_ok=True)
    os.makedirs(IMAGES_FOLDER, exist_ok=True)
    os.makedirs(OTHERS_FOLDER, exist_ok=True)

    for root, dirs, files in os.walk(SOURCE_FOLDER):

        # تجاهل مجلدات النظام اللي نسويها
        if root in [CODES_FOLDER, IMAGES_FOLDER, OTHERS_FOLDER]:
            continue

        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()

            # تجاهل الملف نفسه
            if file_path == os.path.abspath(__file__):
                continue

            # تخطي الملفات الفارغة
            if not is_valid_file(file_path):
                print(f"⏭ Skipped empty: {file}")
                continue

            # =========================
            # IMAGES
            # =========================
            if ext in IMAGE_TYPES:
                dst = safe_move(file_path, IMAGES_FOLDER)
                print(f"🖼 IMAGE -> {file} → {dst}")
                continue

            # =========================
            # CODES
            # =========================
            code_type = get_code_type(ext)
            if code_type:
                target_dir = os.path.join(CODES_FOLDER, code_type)
                dst = safe_move(file_path, target_dir)
                print(f"💻 CODE -> {file} → {code_type}")
                continue

            # =========================
            # OTHERS
            # =========================
            dst = safe_move(file_path, OTHERS_FOLDER)
            print(f"📦 OTHER -> {file}")

    print("\n✅ DONE: Organization complete!")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    organize()
