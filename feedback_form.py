def feedback_form():
        feedback_input = input("What do you think about our product? ")
        feedback = ["good","medium","bad"]
        if feedback_input == feedback[0]:
                print("its nice to know you liked our product")
        elif feedback_input == feedback[1]:
                print("Please let us know our problem")
                Comment=input("comment:")
                print("Thanks...this comment will help us improve...")
        elif feedback_input == feedback[2]:
                print("sorry to hear that...")
                product_list = ["creta","hallo","tacity"]
                impact_feed=input("which product would you like us to improve? \n")
                if impact_feed == product_list[0]:
                        comment= input("what would you like us to improve in creta? \n")        
                elif impact_feed == product_list[1]:
                        comment= input("what would you like us to improve in hallo? \n")
                elif impact_feed == product_list[2]:
                        comment = input("what would you like us to improve in Tacity? \n")
                elif impact_feed == product_list[0]+","+product_list[1]:
                        comment = input("what would you like us to improve in creta & Hallo? \n")
                elif impact_feed == product_list[1]+","+product_list[2]:
                        comment = input("what would you like us to improve in Hallo & Tacity? \n")
                elif impact_feed == product_list[1]+","+product_list[2]:
                        comment = input("what would you like us to improve in creta & Tacity? \n")
                elif impact_feed == product_list[0]+","+product_list[1]+","+product_list[2]:
                        comment = input("what would you like us to improve in creta & Hallo? \n")
                print("Thanks for the feedback")
feedback_form()



