print("Let's check if your number is prime or not, okey?")
while True:
   notprime = False
   enter = int(input("\n\nEnter your number:\t"))
   for i in range(2,enter):
      if enter % i == 0:
         notprime = True
      else:
         pass
   if enter == 1 or enter == 0:
      notprime = True
   if notprime:
      print("\n\n███╗░░██╗░█████╗░\n████╗░██║██╔══██╗\n██╔██╗██║██║░░██║\n██║╚████║██║░░██║\n██║░╚███║╚█████╔╝\n╚═╝░░╚══╝░╚════╝░\t\tyour number is NOT prime.")  
   else:
      print("\n\n██╗░░░██╗███████╗░██████╗\n╚██╗░██╔╝██╔════╝██╔════╝\n░╚████╔╝░█████╗░░╚█████╗░\n░░╚██╔╝░░██╔══╝░░░╚═══██╗\n░░░██║░░░███████╗██████╔╝\n░░░╚═╝░░░╚══════╝╚═════╝░\t\tyour number is prime.")
