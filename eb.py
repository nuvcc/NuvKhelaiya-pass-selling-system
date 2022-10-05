import pygsheets
from tkinter import *
from tkinter import ttk
import re

class Earlybird:
    def __init__(self,root):
        self.downloaddata()
        self.root=root
        self.root.title("NuvKhelaiya pass management system")
        self.root.geometry("1290x770+0+0")
        self.root.focus_force()

        
        
        self.sheet_type=StringVar()
        
        title=Label(self.root,text="NuvKhelaiya pass selling system : Earlybird passes",bd=10,font =("nunito",40,"bold"),bg="beige",fg="black")
        title.pack(side=TOP,fill=X)
        footer=Label(self.root,text="NuvKhelaiya pass selling system made by TtvTooSmart and chandu",bd=10,font=("nunito",7),bg="beige",fg="black")
        footer.pack(side=BOTTOM,fill=X)

        
        # =========================Variable
        self.uid_var=StringVar()
        self.name_var=StringVar()
        self.phonenumber_var=StringVar()
        self.enrollment_var=StringVar()
        self.payment_var=StringVar()
        self.search_by_var=StringVar()
        self.seller = "shivam"

        
        
        
        # ==========================manage_frame
        
    
        manage_frame=Frame(self.root,bd=4,bg="gray")
        manage_frame.place(x=20,y=120,width=550,height=560)
        
        m_title=Label(manage_frame,text="manage payment", font = ("nunito", 20, "bold"),bg="gray")
        m_title.grid(row=0,columnspan=2,pady=20,padx=110)
        

        # ==============labels in manage frame
        
        
        lbl_name = Label(manage_frame,text="Name", font = ("nunito", 15, "bold"), bg= "gray")
        lbl_name.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_name = Entry(manage_frame,textvariable=self.name_var,font =("nunito",10,"bold"),bd=2,state='readonly')
        txt_name.grid(row=3,column=1,pady=10,padx=50,sticky="w") 
        
        
        lbl_uuid = Label(manage_frame,text="Unique ID number", font = ("nunito", 15, "bold"), bg= "gray")
        lbl_uuid.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_uuid = Entry(manage_frame,textvariable=self.uid_var,font =("nunito",10,"bold"),bd=2,state='readonly')
        txt_uuid.grid(row=2,column=1,pady=10,padx=50,sticky="w") 
        
        
        lbl_phonenumber = Label(manage_frame,text="Phone number", font = ("nunito", 15, "bold"), bg= "gray")
        lbl_phonenumber.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        txt_phonenumber = Entry(manage_frame,textvariable=self.phonenumber_var, font =("nunito",10,"bold"),bd=2,state='readonly')
        txt_phonenumber.grid(row=4,column=1,pady=10,padx=50,sticky="w") 
        
        lbl_enrollment = Label(manage_frame,text="enrollment id", font = ("nunito", 15, "bold"), bg= "gray")
        lbl_enrollment.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        txt_enrollment = Entry(manage_frame,textvariable=self.enrollment_var, font =("nunito",10,"bold"),bd=2,state='readonly')
        txt_enrollment.grid(row=5,column=1,pady=10,padx=50,sticky="w")         
        
        
        lbl_pymnt = Label(manage_frame,text="Payment method", font = ("nunito", 15, "bold"), bg= "gray")
        lbl_pymnt.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        combo_payment_method = ttk.Combobox(manage_frame,textvariable=self.payment_var ,width=17, font = ("nunito",10, "bold"),state='readonly')
        combo_payment_method['values'] = ("UPI", "Cash")
        combo_payment_method.grid(row=6,column=1,pady=10,padx=10)


        # =================buttons in manage_frame

        
        button_frame=Frame(manage_frame,bd=4,bg="gray")
        button_frame.place(x=70,y=500,width=350)
        
        addbtn=Button(button_frame,text="update",width=10,command=self.updatedata).grid(row=0,column=0,padx=60)
        delbtn=Button(button_frame,text="clear",width=10,command=self.clear).grid(row=0,column=1,padx=60)
        
        
        
        
        
        
        # ==============detail_frame
        
        detail_frame=Frame(self.root,bd=4,bg="gray")
        detail_frame.place(x=600,y=120,width=670,height=560)
        
        
        # ===========================labels in detail_frame

        
        lblsearch = Label(detail_frame,text="search:", font = ("nunito", 15, "bold"), bg= "gray")
        lblsearch.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        txt_searchbox = Entry(detail_frame,textvariable=self.search_by_var,font =("nunito",10,"bold"),bd=2)
        txt_searchbox.grid(row=0,column=2,pady=10,padx=10,sticky="w")

               
        searchbtn=Button(detail_frame,text="Search",width=10,command=self.searchdata).grid(row=0,column=3,padx=10,pady=10)
        clearbtn=Button(detail_frame,text="clear",width=10).grid(row=0,column=4,padx=10,pady=10)
        addbtn=Button(detail_frame,text="show all",width=10,command=self.adddata).grid(row=0,column=5,padx=60)
        
        
        # =======================table_frame
        
        table_frame=Frame(detail_frame,bd=4,bg="white")
        table_frame.place(x=15,y=70,width=630,height=460)
        
        
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)        
        self.pass_table=ttk.Treeview(table_frame,columns=("uid","fullname","phonenumber","enrollmentid","paymentstatus"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.pass_table.xview)
        scroll_y.config(command=self.pass_table.yview)
        self.pass_table.heading("uid",text="uid")
        self.pass_table.heading("fullname",text="full name")
        self.pass_table.heading("phonenumber",text="phone number")
        self.pass_table.heading("enrollmentid",text="enrollment id")
        self.pass_table.heading("paymentstatus",text="payment status")
        self.pass_table['show']='headings'
        self.pass_table.column("uid",width=50)
        self.pass_table.column("fullname",width=160)
        self.pass_table.column("phonenumber",width=130)
        self.pass_table.column("enrollmentid",width=130)
        self.pass_table.column("paymentstatus",width=130)
        self.pass_table.pack(fill=BOTH,expand=1)
        
        self.pass_table.bind("<ButtonRelease-1>",self.getdata)
        self.adddata()
        
        
    def downloaddata(self):
        path='creds.json'
        gc=pygsheets.authorize(service_account_file=path)
        sheet=gc.open('nuvkhelaiyaeb')
        self.wk1=sheet[0]
        self.l1 = list(filter(lambda x: len(x), self.wk1.get_all_values(include_tailing_empty=False)))
        return(self.l1)

        
        
    def adddata(self):
        self.pass_table.delete(*self.pass_table.get_children())
        self.downloaddata()    
            
        for dt in self.l1: 
            if len(dt[0]):
                self.pass_table.insert("", 'end',iid=dt[0], text=dt[0],
                    values =(dt[0],dt[1],dt[2],dt[3],dt[4]))
                
            
    def clear(self):
        self.uid_var.set("")
        self.name_var.set("")
        self.phonenumber_var.set("")
        self.enrollment_var.set("")
        self.payment_var.set("")


        
                    
    def getdata(self,ev):
        cursor_row =self.pass_table.focus()
        contents= self.pass_table.item(cursor_row)
        row=contents['values']
        self.uid_var.set(row[0])
        self.name_var.set(row[1])
        self.phonenumber_var.set(row[2])
        self.enrollment_var.set(row[3])
        self.payment_var.set(row[4])

    def updatedata(self):
        updatepayment = self.payment_var.get()
        rownum = 'E' + str(self.uid_var.get())
        pygsheets.Cell(rownum,"-",self.wk1).set_value(updatepayment)  
        self.searchdata()
        with open('readme.txt', 'a') as f:
            namevar = str(self.name_var.get())
            paymentvar = str(self.payment_var.get()) 
            log = '\n' + self.seller + "  " + namevar + "  " + paymentvar + "EB"
            f.write(log)


    def searchdata(self):
        srchedname = self.search_by_var.get()
        self.pass_table.delete(*self.pass_table.get_children())
        self.downloaddata()   
            
        for i in range(len(self.l1)):
                # print(self.l1[i][1])
                if re.search("^"+ (str(srchedname)).lower(), (self.l1[i][1]).lower()):
                    
                    self.pass_table.insert("", 'end',iid=self.l1[i], text=self.l1[i],
                    values =(self.l1[i][0],self.l1[i][1],self.l1[i][2],self.l1[i][3],self.l1[i][4]))
                    
        


if __name__=="__main__":
    root=Tk()
    ob=Earlybird(root)
    root.mainloop()




