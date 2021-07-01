import zipfile

def cracker(wordlist, zip):
    index = 0
    with open(wordlist, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    index += 1
                    zip.extractall(pwd=word)
                    print("password found",word)
                    return True
                except:
                    continue
    return False

target = input("Enter Zip file name with Path > ")
wordlist = input("Enter Wordlist name with Path > ")

zip = zipfile.ZipFile(target)

if cracker(wordlist,zip) == False:
    print("Password not found")