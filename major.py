import sys, face_recognition as fc, tkinter.filedialog
import os,sys
import pickle
class Major:
    def delete_face(self,name):
        f=input("Are you sure you want to delete "+name+" y/n")
        if f=='y':
            temp=pickle.load(open("imp.dat","rb"))
            del temp[name]
            pickle.dump(temp,open("imp.dat","wb"))
            print("successfully deleted "+name+" from known faces")
        elif f=='n':
            pass
        else:
            print("wrong choice")
            return  
    def add_face(self, name):
        root=tkinter.Tk()
        file=tkinter.filedialog.askopenfile(title="select a face image to add ")     
        image=fc.load_image_file(file.name)
        root.destroy()
        face_loc=fc.face_locations(image)
        face_enc=fc.face_encodings(image,face_loc)[0]
        data = {name:face_enc}
        if os.path.exists(".\imp.dat"):
            data=pickle.load(open("imp.dat","rb"))
            data.update({name:face_enc})
        pickle.dump(data,open("imp.dat","wb"))
    def delete_all(self):
        if os.path.exists(".\imp.dat"):
            data=[]
            pickle.dump(data,open("imp.dat","wb"))
    def run(self):
        ch=0
        while ch!=5:
            print("\n\n1. add_face, \n2.Delete \n3. delete all \n4.View all\n5. exit")
            ch=int(input("enter your choice"))
            if ch == 1:
                name=str(input("enter the name of the person to add:"))
                self.add_face(name)
            elif ch == 2:
                self.delete_face(str(input("Enter the name of the person to be deleted:  ")))
            elif ch == 3:
                self.delete_all()
            elif ch == 4:
                self.view_all()
            elif ch == 5:
                print("GOOD BYE")
                sys.exit(0)
    def view_all(self):
        if os.path.exists(".\imp.dat"):
            dict= pickle.load(open("imp.dat","rb"))
            count=0
            for i in dict:
                count+=1
                print(str(count)+" "+str(i)+" ", end="\n")
        else:
            print("No faces to display ")
            print("\n Select 1 to add faces to the database")
        
m=Major()
m.run()

        
