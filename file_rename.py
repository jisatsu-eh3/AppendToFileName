import os

print("This script will append a word to the current name to rename all files in a specific folder.")

files = 1
while files == 1:
    print("")
    path = input(r"Please enter file path to the directory of the files to be renamed(EX: C:\Users\user\Pictures\): ")
    filenames = os.listdir(path)
    print("\nHere are the files found below: ")
    print(filenames)
    print("")
    files = input("If these are the right files enter 0 if you need to re-enter file path enter 1: ")
    try:
        files = int(files)
    except:
        print("The input you provided wasn't a 1 or 0. Script Restarting")
        files = 1
        continue
    if files == 1:
        continue
    elif files == 0:
        break
    else:
        print("invalid input restarting")
        files = 1
        continue

new = 1
while new == 1:
    print("")
    aword = input("Now that we have the correct files to rename. Please provide a word to append to the file names: ")
    print("\nBased on what you entered the new file name for the first file in the directory will be: " + aword + filenames[0])
    new = input("If the above new file name looks good enter 0 if you need to re-enter a different workd to append enter 1: ")
    try:
        new = int(new)
    except:
        print("The input you provided wasn't a 1 or 0.")
        new = 1
        continue
    if new == 1:
        continue
    elif new == 0:
        break
    else:
        print("Invalid input.")
        new = 1
        continue

print("\nRenaming all the files now...")
for i in range(len(filenames)):
    new_filename = aword + filenames[i]
    print("Renaming " + filenames[i] + " to " + new_filename)
    os.rename(path + "\\" + filenames[i], path + "\\" + new_filename)

print("The script finished renaming all your files.")
