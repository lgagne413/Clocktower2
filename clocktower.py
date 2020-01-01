from random import randint



class clock():
    def __init__(self):
        self.avail ="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,.?!^*()-~\/:;'|#+= \n"

    def encode(self,textin):
          #codein
          #K1=a0(t+a1)+a2
          #K2=b0(t+b1)^3+b2
        codein = ""
        for x in range(0,8):
            codein += str(randint(1,9))
          #print(codein)

        T = int(codein[0])*10 + int(codein[1])
        cA=[]

        for n in range(2,5):
            cA.append(int(codein[n]))
        cB=[]
        for n in range(5,8):
            cB.append(int(codein[n]))

          #textfile = "extext.txt"


        numin = []

          #letters to numbers
        for line in textin:
            for let in line:
                numin.append(self.avail.find(let))

          #print(numin[81])
          #K1X+K2
        numout=[]
        for num in numin:
            K1 = cA[0]*(T+cA[1])+cA[2]
            K2 = cB[0]*(T+cB[1])**3+cB[2]
            while K1 % 83 == 0 or K2 % 83 == 0:
                T+=1
                K1 = cA[0]*(T+cA[1])+cA[2]
                K2 = cB[0]*(T+cB[1])**3+cB[2]

            numout.append((K1*num+K2) % 83)
            T+=1
          #print(numout[81])
        numoutlet = ""
        for num in numout:
            for index in range(len(self.avail)):
                if num == index:
                    numoutlet=numoutlet+self.avail[index]
        numoutlet+=" "
        numoutlet+=codein


        return numoutlet
############################################3
    def decode(self,textin):
      #codein
      #K1=a0(t+a1)+a2
      #K2=b0(t+b1)^3+b2

      [textin, codein] = textin.rsplit(" ",1)
      #print(textin)
      #print(codein)
      numin = []
      for line in textin:
          for let in line:
              numin.append(self.avail.find(let))
      #print(numin)

      T = int(codein[0])*10 + int(codein[1])
      cA=[]
      for n in range(2,5):
          cA.append(int(codein[n]))
      cB=[]
      for n in range(5,8):
          cB.append(int(codein[n]))

      #print(numin[10])
      #num = K1X+K2
      numout=[]
      for num in numin:

          K1 = cA[0]*(T+cA[1])+cA[2]
          K2 = cB[0]*(T+cB[1])**3+cB[2]

          while K1 % 83 == 0 or K2 % 83 == 0:
              T+=1
              K1 = cA[0]*(T+cA[1])+cA[2]
              K2 = cB[0]*(T+cB[1])**3+cB[2]

          Xt = (num-cB[0]*(T+cB[1])**3-cB[2])
          Xb = (cA[0]*(T+cA[1])+cA[2])
          while Xt % Xb != 0:
              num+=83
              #print(num)
              Xt = (num-cB[0]*(T+cB[1])**3-cB[2])

          numout.append(int((Xt/Xb) % 83))
          #print(T,num,numout[-1])
          T+=1

      #print("Decoding Completed")
      #print(numout[10])

      numoutlet = ""
      for num in numout:
          for index in range(len(self.avail)):
              if num == index:
                  numoutlet=numoutlet+self.avail[index]

      #print("File Written")
      #print("Decoding Successful")
      return numoutlet
