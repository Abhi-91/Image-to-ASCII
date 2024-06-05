import PIL.Image
import sys

#ascii characters used to build the output text 
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters    

def main(new_width=100, path=None):
    if path is None:
        print("Please provide a valid pathname to an image.")
        return

    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname to an image")
        return

    # convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    #print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py image_path")
    else:
        main(path=sys.argv[1])
