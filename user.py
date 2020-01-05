import face_recognition, tkinter.filedialog, pickle
class User:
    
    def encode(self, img):
        face_locs=face_recognition.face_locations(img)
        encodes=face_recognition.face_encodings(img,face_locs)
        return encodes

    def get_known(self):
        li=[]
        dict = pickle.load(open("imp.dat","rb"))
        for j in dict:
            li.append(dict[j])
        return li

    def check_face(self):
        root=tkinter.Tk()
        file=tkinter.filedialog.askopenfile(title="select a file")
        ui = face_recognition.load_image_file(file.name)
        root.destroy()
        encodes=self.encode(ui)
        result=[]
        for i in range(0,len(encodes)):
            result.append( face_recognition.compare_faces(self.get_known(),encodes[i] ))
        print(result)
u=User()
u.check_face()