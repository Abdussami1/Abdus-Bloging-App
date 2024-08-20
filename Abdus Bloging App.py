# Making a bloging app named as 'Abdus Bloging App'

print("Welcome to Abdus Bloging App")

#Asking if user has an acount here
x=input("Do you have an acount here(Enter 'y' for yes and 'n' for no):- ")
if x=='y' or x=='Y':
    for mistake in range(1):
        name= input("Enter your name:- ")
        password= input("Enter your password:- ")
        f= open("User_info.txt","r")
        info= f.readlines()
        for i in info:
            if i[0:-2]==name:
                ind=info.index(i)
                for j in info:
                    m=info[ind+1]
                    if m[0:-2]==password:
                        print("Login successful!")

                        # Main Blog page
                        exi= 2
                        while exi != 1:
                            print("1. Want to write a blog.")
                            print("2. Want to see your blogs.")
                            print("3. Want to see someone else blogs.")

                            # Taking user purpose for using Abdus Bloging App
                            purpose=int(input("Enter your purpose number:- "))
                            if purpose == 1:
                                choice = 'y'
                                while choice == 'y' or choice == 'Y':

                                    # Taking a blog topic from user
                                    topic=input("Enter your blog topic:- ")

                                    # Taking blog contents from user
                                    content=input("Enter your blog content:- ")

                                    # Saving blog written by user
                                    n= name+".txt"
                                    file= open(n,"a+")
                                    file.seek(0)
                                    file.write("\n")
                                    file.write("This blog is written by ")
                                    file.write(name)
                                    file.write("\n")
                                    file.write(topic)
                                    file.write("\n")
                                    file.write("\n")
                                    file.write(content)
                                    file.write("\n")
                                    file.close()
                                    choice= input("Do you want to write another blog(Enter 'Y' for yes and 'n' for no):- ")
                                    print("Thanks for wirtting a blog in Abdus Bloging App.")
                                    exi=int(input("Do you want to exit(Enter 1 for yes and any other number for no):- "))
                            elif purpose== 2:
                                n=name+".txt"
                                file= open(n,"r")
                                my_blogs= file.readlines()
                                for i in my_blogs:
                                    print(i)
                                    file.close()
                                exi=int(input("Do you want to exit(Enter 1 for yes and any other number for no):- "))
                            elif purpose== 3:
                                Bloger= open("Blogers_name.txt","r")
                                n=Bloger.readlines()
                                l=[0]
                                no=0
                                for i in n:
                                    print(no+1,".",i[0:-2])
                                    ap=l.append(no+1)
                                    no+=1
                                ch=int(input("Whose blog do you want to see:- "))
                                for i in l:
                                    if ch==i+1:
                                        nam=n[i]
                                        Bloger_name=nam[0:-2]+".txt"
                                        fil=open(Bloger_name,"r")
                                        fr=fil.readlines()
                                        for j in fr:
                                            print(j)
                                        fil.close()
                                Bloger.close()
                                exi=int(input("Do you want to exit(Enter 1 for yes and any other number for no):- "))
                        if exi==1:
                            break

if x=='n' or x=='N':
    name=input("Enter your name:- ")
    password= input("Make your acount password:- ")
    age= input("Enter your age:- ")
    mob_no= input("Enter your mobile number:- ")
    city= input("Enter your city:- ")
    state= input("Enter your state:- ")
    country= input("Enter your country:- ")
    profession= input("Enter your profession:- ")
    f= open("User_info.txt","a+")
    f.write(name)
    f.write(" ")
    f.write('\n')
    f.write(password)
    f.write(" ")
    f.write('\n')
    f.write(age)
    f.write('\n')
    f.write(mob_no)
    f.write('\n')
    f.write(city)
    f.write('\n')
    f.write(state)
    f.write('\n')
    f.write(country)
    f.write('\n')
    f.write(profession)
    f.write('\n')
    f.close()
    file=open("Blogers_name.txt","a+")
    file.write(name)
    file.write(" ")
    file.write('\n')
    file.close()
    print("Acount successfully created.")
    for mistake in range(1):
        #Main Blog page
        exi= 2
        while exi != 1:
            print("1. Want to write a blog.")
            print("2. Want to see your blogs.")
            print("3. Want to see someone else blogs.")

            # Taking user purpose for using Abdus Bloging App
            purpose=int(input("Enter your purpose number:- "))
            if purpose == 1:
                choice = 'y'
                while choice == 'y' or choice == 'Y':
                    # Taking a blog topic from user
                    topic=input("Enter your blog topic:- ")
                
                    # Taking blog contents from user
                    content=input("Enter your blog content:- ")
                
                    # Saving blog written by user
                    n= name+".txt"
                    file= open(n,"a+")
                    file.seek(0)
                    file.write("\n")
                    file.write("This blog is written by ")
                    file.write(name)
                    file.write("\n")
                    file.write(topic)
                    file.write("\n")
                    file.write("\n")
                    file.write(content)
                    file.write("\n")
                    file.close()
                    choice= input("Do you want to write another blog(Enter 'Y' for yes and 'n' for no):- ")
                print("Thanks for wirtting a blog in Abdus Bloging App.")
                exi=int(input("Do you want to exit(Enter 1 for yes and any other number for no):- "))
            elif purpose== 2:
                n=name+".txt"
                file= open(n,"r")
                my_blogs= file.readlines()
                for i in my_blogs:
                    print(i)
                file.close()
                exi=int(input("Do you want to exit(Enter 1 for yes and any other number for no):- "))
            elif purpose== 3:
                Bloger= open("Blogers_name.txt","r")
                n=Bloger.readlines()
                l=[0]
                no=0
                for i in n:
                     print(no+1,".",i[0:-2])
                     ap=l.append(no+1)
                     no+=1
                ch=int(input("Whose blog do you want to see:- "))
                for i in l:
                    if ch==i+1:
                        nam=n[i]
                        Bloger_name=nam[0:-2]+".txt"
                        fil=open(Bloger_name,"r")
                        fr=fil.readlines()
                        for j in fr:
                            print(j)
                        fil.close()
                Bloger.close()
                exi=int(input("Do you want to exit(Enter 1 for yes and any other number for no):- "))
                if exi==1:
                    break

