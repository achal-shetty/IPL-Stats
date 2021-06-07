#program to find which team has won the most number of matches at a particular stadium

#introduction

print("Hello!!")
print("This project has been designed by the following members:\n Achal Shetty U\n Achanta Sri Shanmukh\n Abhay M")
x=int(input("Are you ready?\n Press '9' to continue!"))
if x==9:
    print("\nWelcome to this page!, here, you can get all information about which teams have won the most number of IPL matches at a particular stadium")

#options

def lst_std():
    print("\nHere are the list of stadiums:  ")
    print("\n1. M. Chinnaswamy Stadium,Bengaluru,Karnataka\n2. PCA Stadium,Mohali,Punjab\n3. Arun Jaitley Stadium,Delhi\n4. Eden Gardens,Kolkata,West Bengal\n5. Wankhede Stadium, Mumbai, Maharashtra\n6. Sawai Mansingh Stadium, Jaipur Rajasthan\n7. Rajiv Gandhi International Cricket Stadium, Hyderabad, Telangana\n8. M. A. Chidambaram Stadium Chennai, Tamil Nadu\n9. DY Patil Stadium Navi Mumbai, Maharashtra \n10. Barabati Stadium, Cuttack. Odisha")        
    print("\n11. Narendra Modi Stadium, Ahmedabad, Gujarat\n12. VCA Stadium,Nagpur, Maharashtra\n13. HPCA Stadium, Dharamshala, Himachal Pradesh\n14. Jawaharlal Nehru Stadium, Kochi, Kerala\n15. Holkar Stadium, Indore, Madhya Pradesh\n16. ACA-VDCA Stadium, Vishakhapatnam, Andhra Pradesh\n17. Maharashtra Cricket Association, Pune, Maharashtra\n18. Shaheed Veer Narayan Cricket Stadium, Raipur, Chattisgarh\n19. JSCA International Cricket Stadium, Ranchi, Jharkhand\n20. Saurashtra Cricket Association, Rajkot, Gujarat\n21. Green Park Stadium, Kanpur, Uttar Pradesh")
    print("\n22. Dubai International Cricket Stadium, UAE\n23. Sharjah Cricket Stadium,Sharjah, UAE\n24. Sheikh Zayed Cricket Stadium, Abu Dhabi,UAE\n25. Newlands Cricket Ground Cape Town,SA\n26. St George's Park, Port Elizabeth,SA \n27. Kingsmead, Durban,SA\n28. Supersport Park, Centurion,SA\n29. Buffalo Park, East London,SA\n30. New Wanderers Stadium, Johannesburg, SA")

    #user-entry

    n=int(input("\nEnter the number present next to the stadium to know which team has won the most number of matches in that venue:   "))

    if n==1:
        print("\nThe team which has won the most number of IPL matches in M. Chinnaswamy Stadium, Bengaluru is ROYAL CHALLENGERS BANGALORE (RCB)")
        print("Captain- Virat Kohli\nOverall Team Win Percent- 47.13%")
    if n==2:
        print("\nThe team which has won the most number of IPL matches in PCA Stadium, Mohali is KINGS XI PUNJAB (KXIP)")
        print("Captain- KL Rahul\nOverall Team Win Percent-45.78%")
    if n==3:
        print("\nThe team which has won the most number of IPL matches in Arun Jaitley Stadium, Delhi is CHENNAI SUPER KINGS (CSK)")
        print("Captain- Mahendra Singh Dhoni\nOverall Team Win Percent-59.83%")
    if n==4:
        print("\nThe team which has won the most number of IPL matches in Eden Gardens, Kolkata is KOLKATA KNIGHT RIDERS (KKR)")
        print("Captain- Eoin Morgan\nOverall Team Win Percent-52.08%")
    if n==5:
        print("\nThe team which has won the most number of IPL matches in Wankhede Stadium, Mumbai is MUMBAI INDIANS (MI)")
        print("Captain- Rohit Sharma\nOverall Team Win Percent-59.11%")
    if n==6:
        print("\nThe team which has won the most number of IPL matches in Sawai Mansingh Stadium, Jaipur is RAJASTHAN ROYALS (RR)")
        print("Captain- Sanju Samson\nOverall Team Win Percent- 50.62%")
    if n==7:
        print("\nThe team which has won the most number of IPL matches in Rajiv Gandhi International Cricket Stadium, Hyderabad is SUNRISERS HYDERABAD (SRH)")
        print("Captain- David Warner\nOverall Team Win Percent-53.62%")
    if n==8:
        print("\nThe team which has won the most number of IPL matches in MA Chidambaram Stadium, Chennai is CHENNAI SUPER KINGS (CSK)")
        print("Captain- Mahendra Singh Dhoni\nOverall Team Win Percent-59.83%")
    if n==9:
        print("\nThe team which has won the most number of IPL matches in DY Patil Stadium, Navi Mumbai is MUMBAI INDIANS (MI)")
        print("Captain- Rohit Sharma\nOverall Team Win Percent-59.11%")
    if n==10:
        print("\nThe team which has won the most number of IPL matches in Barabati Stadium, Cuttack is KOLKATA KNIGHT RIDERS (KKR)")
        print("Captain- Eoin Morgan\nOverall Team Win Percent-52.08%")
    if n==11:
        print("\nThe team which has won the most number of IPL matches in Narendra Modi Stadium, Ahmedabad is GUJARAT LIONS (GL)")
        print("Captain-Suresh Raina\nOverall Team Win Percent-48.03%")
    if n==12:
        print("\nThe team which has won the most number of IPL matches in VCA Stadium, Nagpur is ROYAL CHALLENGERS BANGALORE(RCB)")
        print("Captain- Virat Kohli\nOverall Team Win Percent- 47.13%")
    if n==13:
        print("\nThe team which has won the most number of IPL matches in HPCA Stadium, Dharamshala is KINGS XI PUNJAB (KXIP)")
        print("Captain- KL Rahul\nOverall Team Win Percent-45.78%")
    if n==14:
        print("\nThe team which has won the most number of IPL matches in Jawaharlal Nehru Stadium, Kochi is Kochi Tuskers Kerala (KTK)")
        print("Captain- Mahela Jayawardane\nOverall Team Win Percent- 35%")
    if n==15:
        print("\nThe team which has won the most number of IPL matches in Holkar Stadium, Indore is ROYAL CHALLENGERS BANGALORE (RCB)")
        print("Captain- Virat Kohli\nOverall Team Win Percent- 47.13%")
    if n==16:
        print("\nThe team which has won the most number of IPL matches in ACA-VDCA Stadium, Vishakhapatnam is DECCAN CHARGERS (DC)")
        print("Captain- Adam Gilchrist\nOverall Team Win Percent- 55.25%")
    if n==17:
        print("\nThe team which has won the most number of IPL matches in Maharashtra Cricket Association, Pune is RISING PUNE SUPERGIANTS (RPS)")
        print("Captain- Mahendra Singh Dhoni\nOverall Team Win Percent-44.13%")
    if n==18:
        print("\nThe team which has won the most number of IPL matches in Shaheed Veer Narayan Stadium, Raipur is SUNRISERS HYDERABAD (SRH)")
        print("Captain- David Warner\nOverall Team Win Percent-53.62%")
    if n==19:
        print("\nThe team which has won the most number of IPL matches in JSCA International Cricket Stadium, Ranchi is CHENNAI SUPER KINGS (CSK)")
        print("Captain- Mahendra Singh Dhoni\nOverall Team Win Percent-59.83%")
    if n==20:
        print("\nThe team which has won the most number of IPL matches in Saurashtra Cricket Association, Rajkot is MUMBAI INDIANS (MI)")
        print("Captain- Rohit Sharma\nOverall Team Win Percent-59.11%")
    if n==21:
        print("\nThe team which has won the most number of IPL matches in Green Park, Kanpur is GUJARAT LIONS (GL)")
        print("Captain-Suresh Raina\nOverall Team Win Percent-48.03%")
    if n==22:
        print("\nThe team which has won the most number of IPL matches in Dubai International Stadium, UAE is SUNRISERS HYDERABAD AND CHENNAI SUPER KINGS (SRH AND CSK)")
        print("SRH Captain- David Warner\nOverall Team SRH Win Percent-53.62%")
        print("CSK Captain- Mahendra Singh Dhoni\nOverall Team CSK Win Percent-59.83%")
    if n==23:
        print("\nThe team which has won the most number of IPL matches in Sharjah Cricket Stadium, UAE is DELHI CAPITALS AND KINGS XI PUNJAB")
        print("DC Captain- Shreyas Iyer\nOverall Team DC Win Percent-44.53%")
        print("KXIP Captain- KL Rahul\nOverall Team KXIP Win Percent-45.78%")
    if n==24:
        print("\nThe team which has won the most number of IPL matches in Sheikh Zayed Cricket Stadium, Abu Dhabi is MUMBAI INDIANS AND KOLKATA KNIGHT RIDERS ")
        print("MI Captain- Rohit Sharma\nOverall Team MI Win Percent-59.11%")
        print("KKR Captain- Eoin Morgan\nOverall Team Overall Team KKR Win Percent-52.08%")
    if n==25:
        print("\nThe team which has won the most number of IPL matches in Newlands Cricket Ground, Cape Town is DECCAN CHARGERS")
        print("Captain- Adam Gilchrist\nOverall Team Win Percent- 55.25%")
    if n==26:
        print("\nThe team which has won the most number of IPL matches in St. George's Park, Port Elizabeth is CHENNAI SUPER KINGS (CSK) ")
        print("Captain- Mahendra Singh Dhoni\nOverall Team Win Percent-44.13%")
    if n==27:
        print("\nThe team which has won the most number of IPL matches in Kingsmead, Durban is ROYAL CHALLENGERS BANGALORE (RCB)")
        print("Captain- Virat Kohli\nOverall Team Win Percent- 47.13%")
    if n==28:
        print("\nThe team which has won the most number of IPL matches in SuperSport Park, Centurion is RAJASTHAN ROYALS (RR)")
        print("Captain- Sanju Samson\nOverall Team Win Percent- 50.62%")
    if n==29:
        print("\nThe team which has won the most number of IPL matches in Buffalo Park, East London is MUMBAI INDIANS (MI)")
        print("Captain- Rohit Sharma\nOverall Team Win Percent-59.11%")
    if n==30:
        print("\nThe team which has won the most number of IPL matches in New Wanderers Stadium, Johannesberg is ROYAL CHALLENGERS BANGALORE (RCB)")
        print("Captain- Virat Kohli\nOverall Team Win Percent- 47.13%")
    if n not in range (1,30):
        print("Sorry! We don't have that stadium you were looking for :(")

lst_std()
for i in range (1,1024):
    print("Do you want to continue??\nY/N")

    a=input()

    if a=='Y':
        lst_std()
    elif a=="N":
        print('Thank You!')
        break
    else:
        print("Invalid Input")



