from PIL import Image


imC = Image.open("RV.png")

imL = imC.convert("1")

imD = imL.getdata();

for j in range(4):
  for i in range(32):
    val = 0
    for k in range(8):
      x = i
      y = j*8+k
      pix = imD[y*32+x]
      pix = min(1,pix)
      #print pix
      val += (2**k)*pix
    print "0x{0:02X},".format(val)
#imL.show()



