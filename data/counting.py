import os, os.path


def main():
    #print len([name for name in os.listdir('.') if os.path.isfile(name)])
    path, dirs, files = next(os.walk("./seg_out"))
    file_count = len(files)
    print(file_count)


main()
