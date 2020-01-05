import  face_recognition
from PIL import Image
from major import Major as m
ki = face_recognition.load_image_file("C:\\Users\\vishnu\\Desktop\\faces\\known\\pk.jpg")
kl = face_recognition.face_locations(ki)

ke=face_recognition.face_encodings(ki,kl)

