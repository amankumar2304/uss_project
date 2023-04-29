import streamlit as st
import time
from PIL import Image
import string
import base64 
from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import csv 
import requests
import sys
from streamlit_option_menu import option_menu
import time as tt
import hydralit_components as hc
# from turtle import distance
from streamlit_lottie import st_lottie
import pandas as pd
import random
import string
import git
import os
# from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


st.set_page_config(page_title="Image encryption", page_icon=":maple_leaf:", layout="wide")
def streamlit_menu(example=2):

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "about-us","signup/login","contact-us","forget/reset Password"],  # required
            icons=["house", "book", "envelope", "file","contact"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "000000"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=3)
st.sidebar.success("SECURE-IT.com")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_hsabbeks.json")
lottie_coding_email = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5wr08scz.json")
lottie_sidebar = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_bgclblin.json")

lottie_facebook = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_xwabp3dh.json")
lottie_twiter = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5mhyg2hz.json")
lottie_insta = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_86afyky0.json")
lottie_you = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ej2lfhv2.json")
lottie_bottom= load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_zeoxz8eo.json")
lottie_submit=load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_3ghvm6sn.json")
lottie_login=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_7GoiCvHm8v.json")
lottie_ency=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_9bLBSn/locked.json")
lottie_decy=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_twduwlzj.json")


print("new")
csv.field_size_limit(sys.maxsize)
# import mysql.connector as c
# siglog=False
list2=[]
image_dis=[]
# fields1=['stat']
# feilds2=['name','key','image_code']
with open('stat.csv', mode ='r')as file1:
    csvFile1 = csv.reader(file1) 
    
    # displaying the contents of the CSV file 
    for lines in csvFile1: 
        list2.append(lines)

with open('images.csv', mode ='r')as file2:
    csvFile2 = csv.reader(file2) 
    
    # displaying the contents of the CSV file 
    for lines in csvFile2: 
        image_dis.append(lines)

# print("image_dis"+str(image_dis))                

print("list2 "+str(list2))        
# con = c.connect(host='localhost', user='root',password='5824',database='users_data',port='5824',auth_plugin='mysql_native_password')
feilds=['userid','passwd']
# rows=[['ram','ram34'],['geeta','geeta56']]
list1=[]
userid_list=[]
passwd_list=[]    
# opening the CSV file 
with open('uss.csv', mode ='r')as file: 
      
  # reading the CSV file 
  csvFile = csv.reader(file) 
    
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        list1.append(lines)
# st.write(list1)  
for i in range(1,len(list1)):
    userid_list.append(list1[i][0])
    passwd_list.append(list1[i][1])
print("lsit1"+str(list1))
list1[0].append("enter")  


check = 0

# rad =st.sidebar.radio("Navigation",["Home","About Us","Signup"])


# if con.is_connected:
#     print("Successfully connected")
# cursor = con.cursor(buffered=True)

if selected =="contact-us":
    # st.markdown("## 123A mall road AP building Gurugram Haryana")
    with st.container():
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style.css")
        with st.container():
            st.write("---")
            st.header("Get In Touch With Us!")
            st.write("##")

           # Documention: https://formsubmit.co/aman20492@iiitd.ac.in
            contact_form = """
            <form action="https://formsubmit.co/aman20492@iiitd.ac.in" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st_lottie(lottie_coding_email, height=300, key="email")
    with st.container():
        face_col, twiter_col, insta_col, you_col = st.columns(4)
        with face_col:
            st_lottie(lottie_facebook, height=100, key="lottie_facebook")
        with twiter_col:
            st_lottie(lottie_twiter, height=100, key="lottie_twiter")
        with insta_col:
            st_lottie(lottie_insta, height=100, key="lottie_insta")
        with you_col:
            st_lottie(lottie_you, height=100, key="lottie_you")

          

if selected=="signup/login":
    st.title("SignUp/Login")
    login = st.selectbox("How do you want to login?",["Signup as Customer", "Login as Customer"])

    if login == "Login as Customer":
        
        userid=st.text_input("UserID: ")
        passwd=st.text_input("Password: ", type="password")
        if(userid_list.count(userid)==0 and passwd_list.count(passwd)==0):
            st.error("Userid not Exist try signing up ")
        else:
            c1, c2 = st.columns([7, 1])
            if c2.button("Submit"):
                # st.sidebar.write("WELCOME:\n")
                 

                # print("user", userid)
                check = 1
                bol1 = (userid in userid_list)
                bol2 = (passwd in passwd_list)
                # print(bol1,bol2)
                if (bol1) and (bol2):
                    # st.success("sucessfully logedin....")
                    st_lottie(lottie_login, height=300, key="lottie_login") 
                    st.success("Now u can Encrypt or Decrypt your Images, GO to Home page!!")
                    st.sidebar.write("WELCOME!\n")
                    st.sidebar.write(userid)
                    siglog=True
                    lis1=[]
                    rows1=[]
                    # list1[0].append("entered")
                    lis1.append(1)
                    # lis.append(passwd)
                    rows1.append(lis1)
                    list1[0].append("entered")
                    with open('stat.csv', 'a') as csvfile: 
                    # creating a csv writer object 
                        csvwriter = csv.writer(csvfile) 

                        for i in rows1:
                            csvwriter.writerow(i)
                    
                else:
                        lis1=[]
                        rows1=[]
                        lis1.append(2)
                        # lis.append(passwd)
                        rows1.append(lis1)
                        # list1[0].append("entered")
                        with open('stat.csv', 'a') as csvfile: 
                        # creating a csv writer object 
                            csvwriter = csv.writer(csvfile) 

                            for i in rows1:
                                csvwriter.writerow(i)
                        
                        st.error("user-id or password may not be correct")

    # if(list2[len(list2)-1][0]=='2'):
    #     st.header("CHANGE PASSWORD OR FORGOT PASSWORD:")
    #     # a1,a2,a3,a4,a5=st.columns(5)
    #     # with a4:
    #     if st.button("Forgot-Password"):
    #         with st.container():
    #             def local_css(file_name):
    #                 with open(file_name) as f:
    #                     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    #             local_css("style/style.css")
    #             with st.container():
    #                 st.write("---")
    #                 st.header("Forgot Password!")
    #                 st.write("##")
    #                 user_id=st.text_input("enter your user-id")
    #                 email=st.text_input("enter your email")
    #                 characters = string.ascii_letters + string.digits + string.punctuation

    #                 # Generate a random password
    #                 password = ''.join(random.choice(characters) for i in range(8))
    #                 # email="https://formsubmit.co/"+email
                    
    #                 contact_form = """
    #                 <form action="https://formsubmit.co/{email}" method="POST">
    #                     <input type="hidden" name="_captcha" value="false">
    #                     <input type="hidden" name="{user_id}"  value="false">
    #                     <input type="hidden" name1="{password}"  value="false">
    #                     <button type="submit">Send</button>
    #                 </form>
    #                 """
    #                 left_column, right_column = st.columns(2)
    #                 with left_column:
    #                     st.markdown(contact_form, unsafe_allow_html=True)

        # with a5:            
        # if st.button("Change Password"):
        #     st.header("CHANGE PASSWORD:")
        #     usr=st.text_input("User_id")
        #     passw=st.text_input("Current_Password",type="password")  
        #     bol=False
        #     num=-1
        #     for i in range(1,len(list1)-1):
        #         if(usr==list1[i][0] and passw==list1[i][1]):
        #             #   st.text_input("Enter New PassWord",type="password")
        #             num=i
        #             bol=True
        #             break
        #     if(bol):
        #         newpass=st.text_input("Enter New PassWord",type="password")
        #         # list1[num][1]=newpass\
        #         rows1=[]
        #         liss=[]
        #         liss.append(usr)
        #         liss.append(newpass)
        #         rows1.append(liss)

        #         with open('uss.csv', 'w') as csvfile1: 
        #     # creating a csv writer object 
        #             csvwriter = csv.writer(csvfile1) 

        #             for i in rows1:
        #                 csvwriter.writerow(i)   





                
                    

    if login == "Signup as Customer":

        
        # print(len(data))
        # print(user_id)

        first, last,three = st.columns(3)
        user_name=first.text_input("Name")
        email=last.text_input("E-mail")
        user_id=three.text_input("User-ID (EX-Name_any-4-digit-number)")
        # list1.append(user_id)
        
        passw, phno = st.columns([3, 1])
        passwd=passw.text_input("Password: ", type="password")
        # list2.append(passwd)
        number=phno.text_input("Phone number")

        

        c1, c2 = st.columns([7, 1])
        # st.write()
        # st.write(list2)
        if c2.button("Submit"):
            # st.success("You have been successfully registered")
            st_lottie(lottie_submit, height=300, key="lottie_submit")  
            st.success("Now you can go to HomePage")
        
            st.sidebar.write("WELCOME:\n")
            
            siglog=True
            lis=[]
            rows=[]
            lis.append(user_id)
            lis.append(passwd)
            rows.append(lis)
            # list1[0].append("entered")
            with open('uss.csv', 'a') as csvfile: 
            # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 

                for i in rows:
                    csvwriter.writerow(i)

            lis1=[]
            rows1=[]
            # list1[0].append("entered")
            lis1.append(1)
            # lis.append(passwd)
            rows1.append(lis1)
            # list1[0].append("entered")
            with open('stat.csv', 'a') as csvfile1: 
            # creating a csv writer object 
                csvwriter = csv.writer(csvfile1) 

                for i in rows1:
                    csvwriter.writerow(i)   
    # st_lottie(lottie_bottom, height=300,width=1000, key="lottie_bottom")  

if selected == "about-us":
    st.markdown("""
       ### Our Founders
       ##### Aman Kumar, BTech Computer Science and Biosciences, IIIT Delhi   
       ##### Shelja Agarwal, BTech Computer Science and Social Sciences, IIIT Delhi
       ###
       #### We securely transmit an image across a network connection such that no unauthorized users may be able to decrypt the image.
       #### :pray: :pray: :pray: **TRUST IS IMPORTANT**:pray: :pray: :pray:
       ##### We use Visual Cryptographic techniques to protect the image.
       ##### Share your encrypted pictures with friends and family who can decrypt them using the key.
       ##### Our project looks upon this problem with respect to sharing and saving pictures securely :smile: 
         
    """, True)

    st.subheader("Add your feedback")
    feedback_name = st.text_input("Enter your name: ")
    feedback_text = st.text_area("Write about us: ")
    
    if st.button("submit"):
        query="insert into feedback values('{}','{}')".format(feedback_name, feedback_text)
        st.success("Feedback submitted successfully!")
        

    


if selected=="Home":
    c1, c2 = st.columns([7, 1])
    
    # st.write(list1)
    st.title("""                                FILE ENCRYPTION""")

    image = Image.open('back.png')

    st.image(image, use_column_width=True)

    if(list2[len(list2)-1][0]=='1'):
        
        # c1, c2 = st.columns([7, 1])

        uploaded_files = st.file_uploader("Choose any file u want to encrypt", accept_multiple_files=True)
        what=st.selectbox("Encryption OR Decryption?",["ENCRYPTION", "DECRYPTION"])
        st.write("")
        
        # if(st.button("upload")):
        #     if(what=="ENCRYPTION"):


        block_size = 16
        pad_len=0
        # plain_text=string.ascii_uppercase+string.digits+string.ascii_lowercase

        def sha256(key):
            sha = hashlib.sha256()
            sha.update(key.encode('utf-16'))
            return sha.digest()

        def pad(plain,block):
            pad_len = len(plain) % block
            return plain+((block-pad_len)*chr(block-pad_len)).encode('ascii')

        def unpad(plain,block):
            print(type(plain))
            return plain[0:-(block_size-pad_len)]

        def encrypt(plain,key):
            plain = pad(plain,block_size)
            iv = Random.new().read(block_size)
            cipher = AES.new(key,AES.MODE_CBC,iv)
            final_cipher = cipher.encrypt(plain)
            return base64.b64encode(iv+final_cipher)

        def decrypt(ciphertext,key):
            ciphertext = base64.b64decode(ciphertext)
            iv = ciphertext[:16]
            cipher = AES.new(key,AES.MODE_CBC,iv)
            plaintext = cipher.decrypt(ciphertext[16:])
            return unpad(plaintext,block_size) 


        for uploaded_file in uploaded_files:
            # Set the repository information
            owner = "amankumar2304"
            repo = "uss_project"
            a1=uploaded_file
            path = uploaded_file.name

            # Set the authentication token
            token = "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"

            # Set the file content and commit message
            file_content = a1.read()
            commit_message = "Added file "+uploaded_file.name

            # Encode the file content as base64
            file_content_base64 = base64.b64encode(file_content).decode()

            # Set the API endpoint
            api_endpoint = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

            # Set the request headers and data
            headers = {
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github.v3+json",
            }
            data = {
                "message": commit_message,
                "content": file_content_base64,
            }

            # Make the API request to create the file
            response = requests.put(api_endpoint, headers=headers, json=data)

            # Check if the request was successful
            if response.ok:
                print("File created successfully.")
                st.success("yesss")
            else:
                print("Error creating file.")

            
            enc=bytes()
            # if(st.button("upload")):
                
            if(what=="ENCRYPTION"):
                key =st.text_input("Enter the Encryption key",key=f"widget_{uploaded_file.name}",type="password")
                key1 = sha256(key)
                if(st.button("upload-"+str(uploaded_file.name))):
                    with st.spinner('Wait for it...'):
                        time.sleep(2)
                    st_lottie(lottie_ency, height=300, key="lottie_ency")  
    
                    st.write("filename:", uploaded_file.name)
                    fp = open(uploaded_file.name,'rb')
                    base64_file = base64.b64encode(fp.read())
                    num = 0
                    naam = ""
                    for k in range(len(uploaded_file.name)-1, -1,-1):
                        if(uploaded_file.name[k]=="."):
                            break
                        num+=1
                        naam+=uploaded_file.name[k]
                        print(naam)
                    naam = naam[::-1]
                    # print(naam)
                    s=uploaded_file.name+"encrpted."+str(naam)
                    print(s)
                    enc = encrypt(base64_file,key1)
                    print(type(enc))
                    fp1 = open(s,'wb')

                    # fp1 = open(r"C:/users/{}".format(s),'wb')
                    fp1.write(enc)
                    st.download_button(
                        label="Download file",
                        data=enc,
                        file_name=s,
                        mime="application/octet-stream",
                    )
                    fp.close()
                    fp1.close()
                    rows=[]
                    lis=[]
                    lis.append(uploaded_file.name)
                    lis.append(key)
                    # lis.append(enc)
                    rows.append(lis)
                    with open('images.csv', 'a') as csvfile: 
                    # creating a csv writer object 
                        csvwriter = csv.writer(csvfile) 

                        for i in rows:
                            csvwriter.writerow(i)
                    if key:
                        st.write("Please remeber this and use this key for decryption!!")
            if(what=="DECRYPTION"): 
                lis=[]
                key =st.text_input("Enter the Decryption key",key=f"widget_{uploaded_file.name}",type="password")
                print("img"+str(image_dis))
                
                        # else:
                        #     st.error("WRONG KEY ENTERED!!!")    
                
                if(st.button("upload-"+str(uploaded_file.name))):
                    num = 0
                    naam = ""
                    for k in range(len(uploaded_file.name)-1, -1,-1):
                        if(uploaded_file.name[k]=='.'):
                            break
                        num+=1
                        naam+=uploaded_file.name[k]
                    naam = naam[::-1]
                    for i in range(len(image_dis)):
                    # print(str(image_dis[i][0])+" "+str(uploaded_file.name))
                        
                        s=uploaded_file.name[0:len(uploaded_file.name)-9-num]
                        print(s)

                        if(image_dis[i][0]==s):
                            # if(image_dis[i][1]==key):
                            lis.append(image_dis[i])

                    print("liss= "+str(lis))        
                    with st.spinner('Wait for it...'):
                        time.sleep(2)
                        # st.success('Done!')

                    
                    if(lis[len(lis)-1][1]==key):
                        print("key matched")
                        key = sha256(lis[0][1])
                        fp = open(lis[0][0],'rb')

                        base64_file = base64.b64encode(fp.read())

                        enc = encrypt(base64_file,key)
                        # fp1 = open("encryptedfile.png",'wb')
                        # fp1.write(enc)

                        dec = decrypt(enc,key)
                        fp2 = open(str(lis[0][0])+'decryptedfile.'+naam,'wb')
                        fp2.write(base64.b64decode(dec))
                        st_lottie(lottie_decy, height=300, key="lottie_decy")  

                        st.success("SUCCESSFULLY DECRYPTED")
                        st.download_button(
                            label="Download file",
                            data=base64.b64decode(dec),
                            file_name=str(lis[0][0])+'decryptedfile.'+naam,
                            mime="application/octet-stream",
                        )
                    else:
                        st.error("WRONG KEY ENTERED!!!")    
                    

 


            
    if c2.button("log out"):
        lis=['stat']
        rows1=[]
        rows1.append(lis)
        with open('stat.csv', 'w') as csvfile1: 
            # creating a csv writer object 
                csvwriter = csv.writer(csvfile1) 

                for i in rows1:
                    csvwriter.writerow(i)

if selected=="forget/reset Password":
    log = st.selectbox("Forgot or Change Password",["FORGOT-PASSWORD", "RESET-PASSWORD"])

    if(log=="FORGOT-PASSWORD"):
        with st.container():
                def local_css(file_name):
                    with open(file_name) as f:
                        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


                local_css("style.css")
                with st.container():
                    st.write("---")
                    st.header("Forgot Password!")
                    st.write("##")
                    user_id=st.text_input("enter your user-id")
                    email=st.text_input("enter your email")
                    characters = string.ascii_letters + string.digits + string.punctuation

                    # Generate a random password
                    password = ''.join(random.choice(characters) for i in range(8))
                    # email="https://formsubmit.co/"+email
                    print("email"+str(email))
                    contact_form = """
                    <form action="https://formsubmit.co/{email}" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="hidden" name="{user_id}"  value="false">
                        <input type="hidden" name1="{password}"  value="false">
                        <button type="submit">Send</button>
                    </form>
                    """
                    left_column, right_column = st.columns(2)
                    with left_column:
                        st.markdown(contact_form, unsafe_allow_html=True)
    if(log=="RESET-PASSWORD"):
        st.header("CHANGE PASSWORD:")
        usr=st.text_input("User_id")
        passw=st.text_input("Current_Password",type="password")  
        newpass=""
        bol=False
        num=-1
        bol1 = (usr in userid_list)
        bol2 = (passw in passwd_list)
        
        if bol1 and bol2:
            # for i in range(1,len(list1)):
                # print(list1[i])
                # if(usr==list1[i][0] and passw==list1[i][1]):
                    #   st.text_input("Enter New PassWord",type="password")
                    # print("hello")
            newpass=st.text_input("Enter New PassWord",type="password")
            if(st.button("update")):
                # list1[num][1]=newpass\
                    # if(st.button("submit")):
                rows1=[]
                # print("newpass "+newpass)
                liss=[]
                liss.append(usr)
                liss.append(newpass)
                rows1.append(liss)

                with open('uss.csv', 'a') as csvfile1: 
            # creating a csv writer object 
                    csvwriter = csv.writer(csvfile1) 

                    for i in rows1:
                        csvwriter.writerow(i)  
                    # break
        
                                    
with st.sidebar:
    st_lottie(lottie_sidebar, height=300, key="lottie_sidebar")  
