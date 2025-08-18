import shutil
import os

bkp_dir = "tmp_backup/"

def backup_file(src, dest_dir):
    # extract file name from source
    name = os.path.basename(src)              # e.g. data.txt
    base, ext = os.path.splitext(name)        # split into ("data", ".txt")
    dest = os.path.join(dest_dir, f"{base}_bkp{ext}")  # tmp_backup/data_bkp.txt

    shutil.copy(src, dest)
    print(f"Backup created: {dest}")

# Example usage
path = "challenges"   # source file
backup_file(path, bkp_dir)

print(os.listdir(bkp_dir))