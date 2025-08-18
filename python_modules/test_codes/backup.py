import shutil
import os
import sys
bkp_dir = "tmp_backup/"
# Ensure backup directory exists
if not os.path.exists(bkp_dir):
    os.makedirs(bkp_dir)
if len(sys.argv) > 1:
    path = sys.argv[1]
    if os.path.exists(path):   # check if path exists
        def backup_file(src, dest):
            name = os.path.basename(path)  # get last part
            print(f"Taking Bakup of: {name}")
            base, ext = os.path.splitext(name)        # split into ("data", ".txt")
            dest = os.path.join(dest, f"{base}_bkp{ext}")  # tmp_backup/data_bkp.txt
            shutil.copy(src, dest)
            print(f"Backup created: {dest}")
        backup_file(path, bkp_dir)
        files = os.listdir(bkp_dir)
        print(files)
    else:
        print(f"Error: Path does not exist → {path}")