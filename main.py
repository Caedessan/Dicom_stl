import pydicom
import matplotlib.pyplot as plt
import numpy as np
from stl import mesh
import os
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage import measure

def readnwritedcm(name,i):
    global model_array
    dc=pydicom.dcmread(name)
    ar=dc.pixel_array
    ar[ar<300]=0
    ar[ar>=300]=2048
    model_array[i,:,:]=ar
    #plt.imshow(ar,cmap=plt.cm.bone)
    #img = Image.fromarray(ar)
    #img.save('my.png')
    #img.show()

dirabove=r'C:/Users/caede/Мариморич/'
dirct=os.listdir(dirabove)
filter_dir=[x for x in dirct if x[-4:]=='.dcm']
model_array=np.zeros((len(filter_dir),512,512))
for i,name in enumerate(filter_dir):
    readnwritedcm(dirabove+name,i)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
verts, faces, normals,_ = measure.marching_cubes(model_array)
#mesh = Poly3DCollection(verts[faces])
#mesh.set_edgecolor('k')
#m=mesh.Mesh(verts)
#m.save('model.stl')
with open("model.stl", "w") as f:
    for item in verts:
        f.write(f"v {item[0]} {item[1]} {item[2]}\n")
    for item in normals:
        f.write(f"vn {item[0]} {item[1]} {item[2]}\n")
    for item in faces:
        f.write(
            f"f {item[0]}//{item[0]} {item[1]}//{item[1]} "
            f"{item[2]}//{item[2]}\n"
        )
    f.close()