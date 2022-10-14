import os
import pyAesCrypt



def main():
    bufferSize = 512 * 1024
    password = '1554660qw5'
    ReadPath = ""

    list = get_file_list(ReadPath)

    for file in list:
        pyAesCrypt.decryptFile(file, file.replace(".crypt",""), password, bufferSize)
def get_file_list(path):
    filelist = []
    for root, diirs, files in os.walk(path):
        for file in files:
            if file.endswith(".crypt"):
                filelist.append(os.path.join(root,file))
    return filelist

if __name__ == "__main__":
    main()