if __name__ == "__main__" :
   l = [2,3,5,7,9,11,13,15,16,17,19,21,23,25]
   print("Pages present in the book are:\n",l)
   i = 1
   k = 1
   m = []
   while i <= 25:
      if i not in l:
         m.append(i)
      i = i + 1
   print("The missing page numbers from the book are as follows \n",m)

