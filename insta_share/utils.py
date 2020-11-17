import cv2


def resize_photo_insta(photo):
    img = cv2.imread(photo, cv2.IMREAD_UNCHANGED)
    width = 800
    height = 800
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    image_path = "./insta_image.jpg"
    cv2.imwrite(image_path, resized)

    return image_path
