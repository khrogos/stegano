from PIL import Image
import sys

def encode_image(img, msg):
    """
    use the red values to set a message in the image
    limited to 255 characters
    index is encoded on the first pixel
    """
    lenght = len(msg)
    if lenght > 255 :
        return False
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            (r,g,b) = img.getpixel((col,row))
            if row ==0 and col == 0 and index < lenght:
                asc = lenght
            elif index <= lenght:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col,row), (asc, g, b))
            index += 1
    return encoded

def decode_image(img):
    """
    read the pixels to retrieve the encoded message.
    """
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            r,g,b = img.getpixel((col,row))
            if row == 0 and col == 0:
                lenght = r
            elif index <= lenght:
                msg += chr(r)
            index +=1
    return msg

def usage():
    print("stegano.py\n##")
    print("encode a message in a picture\n##")
    print("usage : ")
    print("- encoding")
    print("\tpython stegano.py encode <original file> <message to hide>\n##")
    print("- decoding")
    print("\t python stegano.py decode <file containing the message>")
    sys.exit(1)

if __name__ == '__main__':
    # is there a correct amount of parameters ?
    print len(sys.argv)
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        usage()
    # Are the parameters good ?
    if len(sys.argv) == 3 and sys.argv[1] != "decode":
        usage()
    if len(sys.argv) == 4 and sys.argv[1] != "encode":
        usage()
    if sys.argv[1] == 'encode':
        original_pict = sys.argv[2]
        values = original_pict.split('.')
        encoded_pict = "{0}-{1}.{2}".format(values[0],'encoded',values[1])
        img = Image.open(original_pict)
        secret_message = sys.argv[3]
        img_encoded = encode_image(img, secret_message)
        img_encoded.save(encoded_pict)

    if sys.argv[1] == 'decode':
        encoded_pict = sys.argv[2]
        img = Image.open(encoded_pict)
        print (decode_image(img))
