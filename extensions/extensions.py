def main():
    answer = input("File name: ").strip().lower()
    extension = check(answer)
    print(f"{extension}")


def check(x):
    if ".gif" in x:
        print (f"image/gif")
    elif ".jpeg" in x or ".jpg" in x:
        print (f"image/jpeg")
    elif ".png" in x:
        print (f"image/png")
    elif ".txt" in x:
        print (f"text/plain")
    elif ".pdf" in x:
        print (f"application/pdf")
    elif ".zip" in x:
        print (f"application/zip")
    else:
        print(f"application/octet-stream")

main()
