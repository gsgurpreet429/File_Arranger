import os
import glob
import time
import shutil


def create_dirs(s, extension_set):
    os.chdir(s)
    for dirs in extension_set:
        try:
            os.makedirs(dirs.upper()+" files")
        except FileExistsError:
            continue


def arrange(s, file_list):
    for file in file_list:
        file_name = file.rsplit(sep='\\', maxsplit=1)
        f_extension = file.rsplit(sep='.', maxsplit=1)
        try:
            if file_name[1] == 'Arranger.py':
                continue
            else:
                shutil.move(file, s + '\\' + f_extension[1].upper() + " files\\"+file_name[1])
        except (IndexError, OSError):
            continue


def main():
    p = input('Please Enter The Source Directory\n')
    s = input('Please Enter The Destination Directory\n')
    n = p + '\\*'

    file_list = glob.glob(n)
    print(file_list)
    extension_set = set()
    for file in file_list:
        extension = file.rsplit(sep='.', maxsplit=1)
        try:
            extension_set.add(extension[1])
        except IndexError:
            continue

    create_dirs(s, extension_set)
    time.sleep(0.1)
    arrange(s, file_list)


if __name__ == "__main__":
    main()
