def main():
    answer = check(get_extension(input("File name: ").strip().lower()))
    print(answer)

def get_extension(filename):
    # Split the filename by dots and take the last part as the extension
    parts = filename.split('.')
    if len(parts) > 1:
        return parts[-1]
    return ""

def check(ext):
    if ext == "gif":
        return "image/gif"
    elif ext == "jpeg" or ext == "jpg":
        return "image/jpeg"
    elif ext == "png":
        return "image/png"
    elif ext == "txt":
        return "text/plain"
    elif ext == "pdf":
        return "application/pdf"
    elif ext == "zip":
        return "application/zip"
    else:
        return "application/octet-stream"

main()

#You can squeeze in your function with your input like this
#   def main():
#       answer = check(get_extension(input("File name: ").strip().lower()))
#       print(answer)

#OR
#Do it the the normal way for clarity
#   def main():
#       answer = input("File name: ").strip().lower()
#       proanswer = get_extension(answer)
#       extension = check(proanswer)
#       print(extension)