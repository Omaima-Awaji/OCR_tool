import easyocr

def ocr_tool():

    reader = easyocr.Reader(['en', 'ar'])
    path = input("Please enter image path: ").replace('\\', '/')
    try:

        result = reader.readtext(path)
    except Exception as e:
        print(f"Error reading image: {e}")
        return

    with open("image_text.txt", "w", encoding="utf-8") as file:
        for detection in result:
            print(detection[1])
            file.write(detection[1] + "\n")
    print("Text saved to image_text.txt")

if __name__ == "__main__":
    ocr_tool()