def main():
    answer = input("File name: ").strip().lower()
    extension = check(answer)
    print(f"{extension}")


def check(x):
    if ".gif" in x:
        return (f"image/gif")
    elif ".jpeg" in x or ".jpg" in x:
        return (f"image/jpeg")
    elif ".png" in x:
        return (f"image/png")
    elif ".txt" in x:
        return (f"text/plain")
    elif ".pdf" in x:
        return (f"application/pdf")
    elif ".zip" in x:
        return (f"application/zip")
    else:
        return(f"application/octet-stream")

main()
