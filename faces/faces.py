def main():
    Inquiry = input("Message ")
    emoji = convert(Inquiry)
    print (f"{emoji}")

def convert(text):
    txt_split =  text.replace(" :)",  "🙂").replace(" :(",  "☹️")
    return txt_split




main()
