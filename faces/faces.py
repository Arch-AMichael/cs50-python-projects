def main():
    Inquiry = input("Hi how are you today ")
    emoji = convert(Inquiry)
    print (f"{emoji}")

def convert(text):
    txt_split =  text.replace(" :)",  "🙂").replace(" :(",  "☹️")
    return txt_split




main()
