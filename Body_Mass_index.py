def body_mass_index():
        weight=float(input("Enter the weight kilograms : "))
        height=float(input("Enter the height meters : "))
        c=(weight/(height*height))
        b_m_i=float(round(c,2))
        print("The Body mass index {}.".format(b_m_i))
        if b_m_i<18.5:
                print("Your weight is {}\nYou are under weight".format(b_m_i))
        elif 18.5<=b_m_i<25.0:
                print("Your weight is {}\nyou are normal".format(b_m_i))
        elif 25.0<=b_m_i<30.0:
                print("Your weight is {}\nyou are over weight".format(b_m_i))
        elif 30.0<=b_m_i:
                print("Your weight is {}\nyou have obesity".format(b_m_i))
body_mass_index()
