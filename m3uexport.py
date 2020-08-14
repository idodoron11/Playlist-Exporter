import errno
import os
import shutil
import codecs

def main():
    # sourceFolder = "D:\\Users\\idodo\OneDrive - mail.tau.ac.il\\My Music\\MusicBee\\Ido's Library\\Exported Playlists"
    # dstFolder = "C:\\Users\\idodo\\Desktop\\test"
    sourceFolder = input("Specify source folder or source file: ")
    print(sourceFolder)
    dstFolder = input("Specify destination folder: ")
    print(dstFolder)
    filepaths = list()

    if os.path.isfile(sourceFolder) & sourceFolder.endswith(".m3u"):
        filepath = sourceFolder
        filename = os.path.basename(filepath)
        filename = os.path.splitext(filename)[0]
        filepaths.append((filepath, filename))
    elif os.path.isdir(sourceFolder):
        for file in os.listdir(sourceFolder):
            if file.endswith(".m3u"):
                filepath = os.path.join(sourceFolder, file)
                filename = os.path.basename(filepath)
                filename = os.path.splitext(filename)[0]
                filepaths.append((filepath, filename))
    else:
        print("Invalid source folder / source file")

    for (filepath, playlistName) in filepaths:
        try:
            assert (type(filepath) == '_io.TextIOWrapper')
        except AssertionError:
            infile = codecs.open(filepath, encoding='utf-8', mode='r')
        files = infile.readlines()
        infile.close()
        print("Copying playlist " + playlistName + ".")

        successfulyCopied = list()

        for i in range(len(files)):
            filepath = files[i].strip("\n").strip("\r").strip("\xed")
            filename = os.path.basename(filepath)
            filename = filename.split(' ', 1)[1]  # removes the current numbering from file name
            filename = str(i + 1).zfill(2) + " " + filename  # adds new numbering to the beginning
            dstPath = os.path.join(dstFolder, playlistName)
            if not os.path.exists(dstPath):
                try:
                    os.makedirs(dstPath)
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            try:
                shutil.copyfile(filepath, os.path.join(dstPath, filename))
                successfulyCopied.append(filename)

            # If source and destination are same
            except shutil.SameFileError:
                print("Source and destination represents the same file.")

            except FileNotFoundError:
                print("Couldn't find " + filepath + ".")

            except FileExistsError:
                print("File " + filepath + " already exists. Skipped.")

            # If destination is a directory.
            except IsADirectoryError:
                print("Destination is a directory.")

            # If there is any permission issue
            except PermissionError:
                print("Permission denied.")

            # For other errors
            except:
                print("Error occurred while copying file.")

        with codecs.open(os.path.join(dstPath, playlistName + ".m3u"), "w", "utf-8") as m3u:
            try:
                m3u.write("\n".join(successfulyCopied))
            except:
                print("Could not write " + playlistName + ".m3u.")



if __name__ == "__main__":
    main()