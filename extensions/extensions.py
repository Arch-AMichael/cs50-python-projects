def main():
    answer = input("File name: ")
    extension = check(answer)
    print(f"{extension})


def check(x):
    if ".gif" in x:
        print (f"image/gif")
    elif ".jpeg" in x or ".jpg" in x:
        print (f"image/jpeg")
    elif ".png" in x:
        print (f"image/png")
    elif ".txt" in x:
        print (f"text/plain)
    elif "" in x:
        print (f"image/gif")
    else:


