import face_recognition
import pickle
import cv2
import os


if __name__ == "__main__":
    # geting the path of face images in our dataset
    print("collecting faces ....")
    curnt_path = os.getcwd() 
    data_base_path = os.path.join(curnt_path, 'database')
    print(data_base_path)
    #list of paths for every image
    imagePaths = []
    for path, subdirs, files in os.walk(data_base_path,topdown = False):
        for name in files:
            imagePaths.append(os.path.join(path, name))

    # initializing the lists of known encodings with there names
    knownEncodings = []
    knownNames = []
    for (i, imagePath) in enumerate(imagePaths):
	# extract the person name from the image path
        print("processing image num {}/{}".format(i + 1,len(imagePaths)))
        print(imagePath)
        name = imagePath.split(os.path.sep)[-2]
        print(name)
        # load the input image and convert it from BGR (OpenCV ordering)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # detect the (x, y) coordinates of the faces's bounding box
        boxes = face_recognition.face_locations(rgb,model='hog')
        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)
        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and encodings
            knownEncodings.append(encoding)
            knownNames.append(name)
        
    # dump the facial encodings + names to disk
    print("serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    #stock the dataset in encodings.pickle (a file for encodings storage)
    f = open("encodings.pickle", "ab")
    f.write(pickle.dumps(data))
    f.close()
    print("success!")
