import cv2
import os


def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)


def readFiles(folder, list):
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in [f for f in filenames if f.endswith(".jpg")]:
            full_path = os.path.join(dirpath, filename)
            list.append(full_path)
    list.sort()


# ORIGINAL IMAGEs
originalFolder = "./original"
originalImageList = []

readFiles(originalFolder, originalImageList)


# EDITED IMAGES

editedFolder = "./edited"
editedlImageList = []

readFiles(editedFolder, editedlImageList)


imagePairs = list(zip(originalImageList, editedlImageList))

for i, (a, b) in enumerate(imagePairs):

    img = cv2.imread(a)
    img2 = cv2.imread(b)
    im_h_resize = hconcat_resize_min([img, img2])
    cv2.imwrite(f'./{i}.jpg', im_h_resize)
