import os
import shutil

def copy_files(src, dst):
    if not os.path.isdir(src):
        raise Exception(f"{src} does not exist or is not a directory")
    if not os.path.isdir(dst):
        raise Exception(f"{dst} does not exist or is not a directory")
        
    for fname in os.listdir(src):
        srcname = f"{src}/{fname}"
        dstname = f"{dst}/{fname}"
        if os.path.isdir(srcname):
            if not os.path.isdir(dstname):
                os.mkdir(dstname)
            copy_files(srcname, dstname)
        else:
            shutil.copyfile(srcname, dstname)