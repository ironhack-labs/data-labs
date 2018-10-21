def insert_dash(num):
    numS=str(num)
    StringNumb=""
    previousN=""
    for n in numS:
      if int(n)==0:
          previousN="even"
          StringNumb=StringNumb+n
                
      elif int(n)%2==0:
          previousN="even"
          StringNumb=StringNumb+n
                            
      elif int(n)%2!=0:
          if previousN == "odd":
              StringNumb=StringNumb+"-"
              StringNumb=StringNumb+n
              previousN = "odd"
          else:
              StringNumb=StringNumb+n
              previousN = "odd"
    return StringNumb