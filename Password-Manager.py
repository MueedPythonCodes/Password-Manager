import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import random


#  ///////////////////////// MAIN MENU ////////////////////////////////////

def mainmenu():
    """Displays the Home Page of Password Manager/your Main Menu"""
    window = tkinter.Tk()
    window.title("Main Menu")
    window.geometry("440x360")  # Fixed window size
    window.iconbitmap("final_project_pic1.ico")


    def save_password():
        """Displays the Save Password interface"""
        window.destroy()
        save_file()

    def retrieve_password():
        """Displays the Retrieve Password interface"""
        window.destroy()
        retrieve_file()

    def update_password():
        """Displays the Update Password interface"""
        window.destroy()
        update_file()

    def exit():
        """This Function will Close the Application"""
        window.destroy()

    # Load and resize the image
    image = Image.open("login_pm2.jpg")
    image = image.resize((220, 250)) 
    photo = ImageTk.PhotoImage(image)

    frame = tkinter.Frame(window, bg="black")
    frame.pack()

    first_label = tkinter.Label(frame, text="Welcome to Password Manager", background="red", foreground="white", font=("Arial", 16, "bold"))
    first_label.grid(row=0, column=0, columnspan=2, pady=20)

    save_button = tkinter.Button(frame, text="Save Password", command=save_password, font=("Arial", 12))
    save_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

    retrieve_button = tkinter.Button(frame, text="Retrieve Password", command=retrieve_password, font=("Arial", 12))
    retrieve_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

    update_button = tkinter.Button(frame, text="Update Password", command=update_password, font=("Arial", 12))
    update_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    exit_button = tkinter.Button(frame, text="Exit", font=("Arial", 12), command=exit)
    exit_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

    image_label = tkinter.Label(frame, image=photo)
    image_label.grid(row=1, column=1, rowspan=4, padx=20, pady=20, sticky="e")

    window.mainloop()


# //////////////////////////////////////////////////////////////////////////////////////



#  /////////////////////////////// Function for Encryption ////////////////////
 
def encrypt(user):
        """This function will encrypt user password in order to maintain the Security of the user"""
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',\
            'x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',\
                'u','v','w','x','y','z']

        key=""
        shift=5
        user_text=user
        for i in user_text:
            if i in alphabet:
                pos = alphabet.index(i)
                new = pos+shift
                key = key+alphabet[new]
            else:
                key += i
        return key


#  ******************************************************


#  /////////////////////////////  Function For Decryption    ////////////////////////////////////


def dec_pass(saved_pass):
    """This function will decrypt your password in order to diplay the actual password the user has saved"""
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',\
        'x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',\
            'u','v','w','x','y','z']

    key=""
    shift=5
    user_text=saved_pass
    for i in user_text:
        if i in alphabet:
            pos = alphabet.index(i)
            new = pos-shift
            key = key+alphabet[new]
        else:
            key += i
    return key



# *********************************************************







#  /////////////////////////// Save File /////////////////////////////////

def save_file():
    """This function contains the Save File GUI , a back function
       and a save_password function to save password and a read_file function
       for checking whether the user having same user name and same app name already exists or not"""
    
    
    def back():
        """It will return the control back to the Home Page"""
        window.destroy()
        mainmenu()



    def gen_pass():
        """This will automatically generate a password"""
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


        no_of_letters=4
        no_selected=2
        
        generated_pass=""
        for l in range(0,no_of_letters):
            generated_pass += random.choice(letters)

        for i in range(0,no_selected):
            generated_pass += random.choice(numbers)


        s3_entry.delete(0,tkinter.END)
        s3_entry.insert(0,generated_pass)



    def read_file(lst):
        """This function checks whether the user with same name and app name already exits or not"""
        with open("save_data.txt", "r") as r:
            read = r.readlines()
            for line in read:
                line1 = eval(line)              # Convert the string representation of list to actual list
                if lst[0] == line1[0] and lst[1] == line1[1]:
                    return False

            return True


    def save_password():
        """This function will save your app name, user name and password into the text file"""
        app_name = s1_entry.get()
        user_name = s2_entry.get()
        user_password = s3_entry.get()
        for _ in range(0,1):
            if s1_entry.get()=="":
                messagebox.showerror("Error","Don't let the App Name field empty")
                break
            if s2_entry.get()=="":
                messagebox.showerror("Error","Don't let the User Name field empty")
                break
            if s3_entry.get()=="":
                messagebox.showerror("Error","Don't let the Password field empty")
                break
            
            final_pass=encrypt(user_password)
            lst = [app_name.lower(), user_name.lower(), final_pass]
            check = read_file(lst)
            
            if check:
                with open("save_data.txt","a") as s_file:
                    s_file.writelines(str(lst)+"\n")                    #here i am typecasting list to add a new line character after it 
                messagebox.showinfo("Save Status", "Password successfully saved")
            else:
                messagebox.showerror("Saving Error", "User already exists")




    window=tkinter.Tk()
    window.title("Save Password")
    window.geometry("250x300")
    window.iconbitmap("final_project_pic1.ico")

    frame=tkinter.Frame(window,bg="black")
    frame.grid(row=0, column=0,sticky="news")    

    s_label=tkinter.Label(frame,text="Save Your Password Here",bg="red",fg="white",font="bold")
    s_label.grid(row=0, columnspan=2, padx=10, pady=20)

    s1_label=tkinter.Label(frame,text="App Name",bg="black",fg="white")
    s1_label.grid(row=1, column=0,sticky="w", padx=10, pady=10)

    s1_entry=tkinter.Entry(frame)
    s1_entry.grid(row=1, column=1, padx=20, pady=10)

    s2_label=tkinter.Label(frame,text="User Name",bg="black",fg="white")
    s2_label.grid(row=2, column=0,sticky="w",  padx=10, pady=10)

    s2_entry=tkinter.Entry(frame)
    s2_entry.grid(row=2, column=1, padx=20, pady=10)

    s3_label=tkinter.Label(frame,text="Password",bg="black",fg="white")
    s3_label.grid(row=3, column=0,sticky="w",  padx=10, pady=10)

    s3_entry=tkinter.Entry(frame,show="*")
    s3_entry.grid(row=3, column=1, padx=20, pady=10)

    btn_generate=tkinter.Button(frame,text="Generate Password",command=gen_pass)
    btn_generate.grid(row=4,columnspan=2, sticky="e",padx=20 ,pady=15)

    btn_back=tkinter.Button(frame, text="  Back  ",bg="#C70039",fg="white",command=back)
    btn_back.grid(row=5,column=0, sticky="w",padx=20,pady=20)

    btn_get=tkinter.Button(frame, text="Save Password",bg="#C70039",fg="white",command=save_password)
    btn_get.grid(row=5,column=1,sticky="e", padx=20,pady=20)


    window.mainloop()



# ////////////////////////////////////////////////////////////////////////////////////




#  ////////////////////////////// Retrieve File ////////////////////////////////

def retrieve_file():
    """This function contains the Retrieve File GUI , a back function
       and a retrieve function for retrieving password"""
    
    def back():
        """It will return the control back to the Home Page"""
        window.destroy()
        mainmenu()


    def retrieve_password():
        """This Function will Retrieve your Password that you have already saved"""

        user = user_entry.get().lower()
        app = app_entry.get().lower()
        flag = False
        with open("save_data.txt", "r") as rfile:
            rfile = rfile.readlines()
            for line in rfile:
                data = eval(line)  # Convert the string representation of list to actual list
                saved_app = data[0]
                saved_user = data[1]
                saved_password = data[2]
                d_save_pass=dec_pass(saved_password)
                if app == saved_app and user == saved_user:
                    output_pass_label.config(text=f"Password: {d_save_pass}")
                    flag = True
                    break
                else:
                    output_pass_label.config(text="")

        if not flag:
            messagebox.showerror(title="App/User Name Status", message="App/User name not exits")


    window=tkinter.Tk()
    window.geometry("250x230")
    window.title("Retrieve Password")
    window.iconbitmap("final_project_pic1.ico")

    frame=tkinter.Frame(window,bg="black")
    frame.grid(row=0, column=0)

    r_label=tkinter.Label(frame,text="Retrieve Your Password",bg="red",fg="white",font="bold")
    r_label.grid(row=0, columnspan=2, padx=10, pady=10)

    user_label = tkinter.Label(frame, text="User name", bg="black", fg="white")
    user_label.grid(row=1, column=0, padx=10, pady=10)

    user_entry = tkinter.Entry(frame)
    user_entry.grid(row=1, column=1, padx=10, pady=10)

    app_label = tkinter.Label(frame, text="App name", background="black", fg="white")
    app_label.grid(row=2, column=0, padx=20, pady=10)

    app_entry = tkinter.Entry(frame, background="white")
    app_entry.grid(row=2, column=1, padx=20, pady=10)

    output_pass_label = tkinter.Label(frame, background="black", fg="white")        #    Empty Label Initially
    output_pass_label.grid(row=3, columnspan=2, padx=20, pady=10)

    btn_back=tkinter.Button(frame, text="  Back  ",bg="#C70039",fg="white",command=back)
    btn_back.grid(row=4,column=0, sticky="w",padx=20,pady=20)

    btn_get=tkinter.Button(frame, text="Get Password",bg="#C70039",fg="white",command=retrieve_password)
    btn_get.grid(row=4,column=1,sticky="e", padx=20,pady=20)


    window.mainloop()


# ////////////////////////////////////////////////////////////////////////////////////////////





#  ////////////////////////////// Update File ///////////////////////////////////////////////

def update_file():
    """This function will update the password if the user exits"""

    def back():
        """It will return the control back to the Home Page"""
        window.destroy()
        mainmenu()



    def update_password():
        """This function checks whether the user already exists or not 
           and if user exists the Password will be Updated"""
        app_name = app_update_entry.get().lower()
        user_name = user_update_entry.get().lower()
        old_password = old_pass_entry.get()
        new_password = new_updated_entry.get()
        fin_new_pass=encrypt(new_password)
        updated_data = []
        flag = False
        with open("save_data.txt" , "r") as file:
            for line in file:
                lst = eval(line)
                r=dec_pass(lst[2])
                if lst[0] == app_name and lst[1] == user_name and r==old_password:
                    updated_data.append(f"['{app_name}', '{user_name}', '{fin_new_pass}']\n")
                    flag = True
                    
                else:
                    updated_data.append(line)
                    
                    
        for _ in range(0,1):
            if fin_new_pass=="":
                messagebox.showerror("Error","New Password can't be empty")
                break

            with open("save_data.txt", "w") as w_file:
                w_file.writelines(updated_data)

            if flag:
                messagebox.showinfo("Update Status", "Password Updated")
            else:
                messagebox.showerror("Update Status", "User not found")



    window=tkinter.Tk()
    window.geometry("270x270")
    window.title("Update Password")
    window.iconbitmap("final_project_pic1.ico")

    frame=tkinter.Frame(window,background="black")
    frame.grid(sticky="e")

    top_label=tkinter.Label(frame,text="Update Your Password Here",background="red",fg="white",font=10)
    top_label.grid(row=0,columnspan=2, pady=10)

    a_label=tkinter.Label(frame,text="App Name ",background="black",foreground="#0ab2fa")
    a_label.grid(row=1,column=0, padx=20, pady=10)

    app_update_entry=tkinter.Entry(frame)
    app_update_entry.grid(row=1,column=1,padx=10, pady=10)

    user_label=tkinter.Label(frame,text="User Name ",background="black",foreground="#0ab2fa")
    user_label.grid(row=2,column=0,padx=20, pady=10)

    user_update_entry=tkinter.Entry(frame)
    user_update_entry.grid(row=2,column=1,padx=10, pady=10)

    old_label=tkinter.Label(frame,text="Old Password ",background="black",foreground="#0ab2fa")
    old_label.grid(row=3,column=0,padx=20, pady=10)

    old_pass_entry=tkinter.Entry(frame,show="*")
    old_pass_entry.grid(row=3,column=1,padx=10, pady=10)

    new_label=tkinter.Label(frame,text="New Password ",background="black",foreground="#0ab2fa")
    new_label.grid(row=4,column=0,padx=20, pady=10)

    new_updated_entry=tkinter.Entry(frame,show="*")
    new_updated_entry.grid(row=4,column=1,padx=10, pady=10)

    btn_back=tkinter.Button(frame,text="  Back  ",background="#C70039",foreground="white",command=back)
    btn_back.grid(row=5,column=0,pady=20)

    btn_update=tkinter.Button(frame,text="Update Password",background="#C70039",foreground="white", command=update_password)
    btn_update.grid(row=5,column=1,pady=20)

    window.mainloop()



# /////////////////////////////////////////////////////////////////////////////



if __name__ == "__main__":
    mainmenu()
