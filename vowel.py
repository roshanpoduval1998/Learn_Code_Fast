def vowel():
        num = int(input("Enter number of input"))
        for x in range(1,num+1):
                x=input("enter the input \n")
                vowel=0
                consonant=0
                for i in x:
                        if (i=="a"or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
                                vowel=vowel+1
                        else:
                                consonant=consonant+1
                print("The vowel are {} ".format(vowel))
                print("The consonant are {} ".format(consonant))
        print("Vowels & Consonants are calculated")        
vowel()
