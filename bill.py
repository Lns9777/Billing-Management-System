from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        
        title=Label(self.root,text="Sudhir Agency Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #****Variables of all products*******#
        self.vita_248g = IntVar()
        self.vita_418g = IntVar()
        self.bis_50_29g = IntVar()
        self.bis_50_63g = IntVar()
        self.bis_50_188g = IntVar()
        self.marie_33g = IntVar()
        self.marie_63g = IntVar()
        self.marie_190g = IntVar()
        self.marie_250g = IntVar()
        self.marie_400g = IntVar()
        self.potazos_24g = IntVar()
        self.maskachaska_24g = IntVar()
        self.golmal_200g = IntVar()
        self.goodday_27g = IntVar()
        self.goodday_60g = IntVar()
        self.goodday_200g = IntVar()
        self.gooddaykaju_28g = IntVar()
        self.gooddaykaju_60g = IntVar()
        self.gooddaykaju_200g = IntVar()
        self.gooddaychoco_60g = IntVar()
        self.milkbikis_264g = IntVar()
        self.burbun_20g = IntVar()
        self.burbun_150g = IntVar()
        self.thinarrowroot_150g = IntVar()
        self.simplecracker_100g = IntVar()
        self.sugarfreecracker_300g = IntVar()
        self.Tglucose_29g = IntVar()
        self.Tglucose_43g = IntVar()
        self.Tglucose_85g = IntVar()
        self.TCchocolate_33g = IntVar()
        self.TCOrange_33g = IntVar()
        self.TCElaichi_33g = IntVar()
        self.TCVanilla_33g = IntVar()
        self.oats_150g = IntVar()

        #=========Total Price & Tax Variable============#
        self.product_price = StringVar()
        self.product_price_CGST = StringVar()
        self.product_price_GST = StringVar()

        #-========= Customer ========-#
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        #Customer Detail Frame
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Cutomer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1,width=16,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphone_lbl = Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt = Entry(F1,width=16,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbill_lbl = Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt = Entry(F1,width=16,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn = Button(F1,text="Search",command=self.find_bill,width=10,bd=7, font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #Product Frame

        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Product Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=980,height=400)
        
        #F3 = LabelFrame(F2,bd=10,relief=GROOVE,text="Vita",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        #F3.place(x=0,y=0,width=340,height=140)
        
        vita_lbl= Label(F2,text='Vita Biscuit(248g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=0,sticky="w")
        vita_txt=Entry(F2,width=10,textvariable=self.vita_248g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        vita_lbl= Label(F2,text='Vita Biscuit(418g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=0,sticky="w")
        vita_txt=Entry(F2,width=10,textvariable=self.vita_418g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        #F4 = LabelFrame(F2,bd=10,relief=GROOVE,text="50-50",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        #F4.place(x=0,y=150,width=340,height=200)
        
        bis_lbl= Label(F2,text='50-50(29g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=0,sticky="w")
        bis_txt=Entry(F2,width=10,textvariable=self.bis_50_29g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        bis_lbl= Label(F2,text='50-50(63g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=0,sticky="w")
        bis_txt=Entry(F2,width=10,textvariable=self.bis_50_63g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=1)
        bis_lbl= Label(F2,text='50-50(188g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=0,sticky="w")
        bis_txt=Entry(F2,width=10,textvariable=self.bis_50_188g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=1)
       
        '''bis_lbl= Label(F2,text='50-50(188g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=0,sticky="w")
        bis_txt=Entry(F2,width=10,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=1)
        bis_lbl= Label(F2,text='50-50(188g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=0,sticky="w")
        bis_txt=Entry(F2,width=10,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=1)'''

        #F5 = LabelFrame(F2,bd=10,relief=GROOVE,text="Marie",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        #F5.place(x=350,y=20,width=280,height=300)
        
        Marie_lbl= Label(F2,text='Marie(33g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=0,sticky="w")
        Marie_txt=Entry(F2,width=10,textvariable=self.marie_33g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=1)
        Marie_lbl= Label(F2,text='Marie(63g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=0,sticky="w")
        Marie_txt=Entry(F2,width=10,textvariable=self.marie_63g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=1)
        Marie_lbl= Label(F2,text='Marie(190g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=0,padx=10,pady=0,sticky="w")
        Marie_txt=Entry(F2,width=10,textvariable=self.marie_190g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=1)
        Marie_lbl= Label(F2,text='Marie(250g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=0,padx=10,pady=0,sticky="w")
        Marie_txt=Entry(F2,width=10,textvariable=self.marie_250g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=1)
        Marie_lbl= Label(F2,text='Marie(400g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=9,column=0,padx=10,pady=0,sticky="w")
        Marie_txt=Entry(F2,width=10,textvariable=self.marie_400g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=1)

        potazos_lbl= Label(F2,text='50-50 Potazos(24g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=10,column=0,padx=10,pady=0,sticky="w")
        potazos_txt=Entry(F2,width=10,textvariable=self.potazos_24g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=10,column=1,padx=10,pady=1)

        maskachaska_lbl = Label(F2,text='50-50 MaskaChaska(24g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=11,column=0,padx=10,pady=0,sticky="w")
        maskachaska_txt=Entry(F2,width=10,textvariable=self.maskachaska_24g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=11,column=1,padx=10,pady=1)

        golmall_lbl = Label(F2,text='Golmal(200g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=3,padx=10,pady=0,sticky="w")
        golamall_txt=Entry(F2,width=10,textvariable=self.golmal_200g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=1)

        goodday_lbl = Label(F2,text='Good-Day Butter(27.5g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=3,padx=10,pady=0,sticky="w")
        goodday_txt=Entry(F2,width=10,textvariable=self.goodday_27g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=1)
        goodday_lbl = Label(F2,text='Good-Day Butter(60g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=3,padx=10,pady=0,sticky="w")
        goodday_txt=Entry(F2,width=10,textvariable=self.goodday_60g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=1)
        goodday_lbl = Label(F2,text='Good-Day Butter(200g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=3,padx=10,pady=0,sticky="w")
        goodday_txt=Entry(F2,width=10,textvariable=self.goodday_200g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=4,padx=10,pady=1)

        goodday_lbl = Label(F2,text='Good-Day kaju(27.5g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=3,padx=10,pady=0,sticky="w")
        goodday_txt=Entry(F2,width=10,textvariable=self.gooddaykaju_28g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=4,padx=10,pady=1)
        goodday_lbl = Label(F2,text='Good-Day kaju(60g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=3,padx=10,pady=0,sticky="w")
        goodday_txt=Entry(F2,width=10,textvariable=self.gooddaykaju_60g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=4,padx=10,pady=1)
        goodday_lbl = Label(F2,text='Good-Day kaju(200g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=3,padx=10,pady=0,sticky="w")
        goodday_txt=Entry(F2,width=10,textvariable=self.gooddaykaju_200g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=4,padx=10,pady=1)

        goodday_lbl = Label(F2,text='Good-Day Choco(60g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=3,padx=10,pady=0,sticky="w")
        goodday_txt=Entry(F2,width=10,textvariable=self.gooddaychoco_60g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=4,padx=10,pady=1)
        
        milkbikis_lbl = Label(F2,text='Milkbikis(264g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=3,padx=10,pady=0,sticky="w")
        milkbikis_txt=Entry(F2,width=10,textvariable=self.milkbikis_264g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=4,padx=10,pady=1)

        burbun_lbl = Label(F2,text='BurBun(20g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=9,column=3,padx=10,pady=0,sticky="w")
        burbun_txt=Entry(F2,width=10,textvariable=self.burbun_20g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=4,padx=10,pady=1)
        burbun_lbl = Label(F2,text='BurBun(150g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=9,column=5,padx=10,pady=0,sticky="w")
        burbun_txt=Entry(F2,width=10,textvariable=self.burbun_150g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=6,padx=10,pady=1)

        thinarrowroot_lbl = Label(F2,text='Thin ArrowRoot(150g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=5,padx=10,pady=0,sticky="w")
        thinarrowroot_txt=Entry(F2,width=10,textvariable=self.thinarrowroot_150g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=6,padx=10,pady=1)

        cracker_lbl = Label(F2,text='Sugar-Free NutriChoice Cracker(300g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=10,column=3,padx=10,pady=0,sticky="w")
        cracker_txt=Entry(F2,width=10,textvariable=self.sugarfreecracker_300g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=10,column=4,padx=10,pady=1)
        cracker_lbl = Label(F2,text='Simple NutriChoice Cracker(100g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=11,column=3,padx=10,pady=0,sticky="w")
        cracker_txt=Entry(F2,width=10,textvariable=self.simplecracker_100g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=11,column=4,padx=10,pady=1)

        oats_lbl = Label(F2,text='Britania Oats(150g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=5,padx=10,pady=0,sticky="w")
        oats_txt=Entry(F2,width=10,textvariable=self.oats_150g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=6,padx=10,pady=1)

        tiger_lbl = Label(F2,text='Tiger-Glucose(28.6g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=5,padx=10,pady=0,sticky="w")
        tiger_txt=Entry(F2,width=10,textvariable=self.Tglucose_29g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=6,padx=10,pady=1)
        tiger_lbl = Label(F2,text='Tiger-Glucose(42.7g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=5,padx=10,pady=0,sticky="w")
        tiger_txt=Entry(F2,width=10,textvariable=self.Tglucose_43g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=6,padx=10,pady=1)
        tiger_lbl = Label(F2,text='Tiger-Glucose(85.3g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=5,padx=10,pady=0,sticky="w")
        tiger_txt=Entry(F2,width=10,textvariable=self.Tglucose_85g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=6,padx=10,pady=1)
        tiger_lbl = Label(F2,text='TigerCream Chocolate(33.4g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=5,padx=10,pady=0,sticky="w")
        tiger_txt=Entry(F2,width=10,textvariable=self.TCchocolate_33g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=6,padx=10,pady=1)
        tiger_lbl = Label(F2,text='TigerCream Orange(33.4g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=5,padx=10,pady=0,sticky="w")
        tiger_txt=Entry(F2,width=10,textvariable=self.TCOrange_33g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=6,padx=10,pady=1)
        tiger_lbl = Label(F2,text='TigerCream Elaichi(33.4g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=5,padx=10,pady=0,sticky="w")
        tiger_txt=Entry(F2,width=10,textvariable=self.TCElaichi_33g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=6,padx=10,pady=1)
        tiger_lbl = Label(F2,text='TigerCream Vanilla(33.4g)',font=("arial",10,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=5,padx=10,pady=0,sticky="w")
        tiger_txt=Entry(F2,width=10,textvariable=self.TCVanilla_33g,font=('arial',10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=6,padx=10,pady=1)

        #************BILL AREA*******************
        F3 = Frame(self.root,bd=10,relief=GROOVE)
        F3.place(x=1000,y=180,width=350,height=400)
        bill_title = Label(F3,text='Bill Area',font="ariel 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F3,orient=VERTICAL)
        self.textarea = Text(F3,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #*************BUTTON***************#
        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=0,y=585,relwidth=1,height=155)
        
        total_price = Label(F4,text='Total Price',bg=bg_color,fg="white",font=('times new roman',16,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F4,width=18,textvariable=self.product_price,font="arial 12 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        total_cgst = Label(F4,text='Total CGST',bg=bg_color,fg="white",font=('times new roman',16,"bold")).grid(row=0,column=3,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F4,width=18,textvariable=self.product_price_CGST,font="arial 12 bold",bd=7,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=5)

        total_gst = Label(F4,text='Total GST',bg=bg_color,fg="white",font=('times new roman',16,"bold")).grid(row=1,column=3,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F4,width=18,textvariable=self.product_price_GST,font="arial 12 bold",bd=7,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=5)
        
        btn_F = Frame(F4,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=585,height=105)
        
        total_btn = Button(btn_F,command=self.Total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 12 bold").grid(row=0,column=0,padx=7,pady=10)
        generate_btn = Button(btn_F,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 12 bold").grid(row=0,column=1,padx=7,pady=10)
        clear_btn = Button(btn_F,command=self.clear_data,text="Clear",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 12 bold").grid(row=0,column=2,padx=7,pady=10)
        exit_btn = Button(btn_F,command=self.Exit_app,text="Exit",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 12 bold").grid(row=0,column=3,padx=7,pady=10)
        
        self.welcome_bill()
    
    def Total(self):
        self.v248=self.vita_248g.get()*40
        self.v418=self.vita_418g.get()*65
        self.b_50_29=self.bis_50_29g.get()*5
        self.b_50_63=self.bis_50_63g.get()*10
        self.b_50_188=self.bis_50_188g.get()*30
        self.m33=self.marie_33g.get()*5
        self.m63=self.marie_63g.get()*10
        self.m190=self.marie_190g.get()*30
        self.m250=self.marie_250g.get()*40
        self.m400=self.marie_400g.get()*55
        self.p24=self.potazos_24g.get()*10
        self.mc24=self.maskachaska_24g.get()*10
        self.g200=self.golmal_200g.get()*30
        self.gday27=self.goodday_27g.get()*5
        self.gday60=self.goodday_60g.get()*10
        self.gday200=self.goodday_200g.get()*35
        self.gkaju28=self.gooddaykaju_28g.get()*5
        self.gkaju60=self.gooddaykaju_60g.get()*10
        self.gkaju200=self.gooddaykaju_200g.get()*35
        self.gchoco60=self.gooddaychoco_60g.get()*10
        self.milkbikis264=self.milkbikis_264g.get()*40
        self.burbun20=self.burbun_20g.get()*5
        self.burbun150=self.burbun_150g.get()*40
        self.tar150=self.thinarrowroot_150g.get()*40
        self.sfc300=self.sugarfreecracker_300g.get()*45
        self.sc100=self.simplecracker_100g.get()*45
        self.oats150=self.oats_150g.get()*75
        self.tg29=self.Tglucose_29g.get()*3
        self.tg43=self.Tglucose_43g.get()*5
        self.tg85=self.Tglucose_85g.get()*10
        self.tc33=self.TCchocolate_33g.get()*5
        self.tco33=self.TCOrange_33g.get()*5
        self.tce33=self.TCElaichi_33g.get()*5
        self.tcv33=self.TCVanilla_33g.get()*5
        self.total_product_price=float(
                                        (self.v248)+
                                        (self.v418)+
                                        (self.b_50_29)+
                                        (self.b_50_63)+
                                        (self.b_50_188)+
                                        (self.m33)+
                                        (self.m63)+
                                        (self.m190)+
                                        (self.m250)+
                                        (self.m400)+
                                        (self.p24)+
                                        (self.mc24)+
                                        (self.g200)+
                                        (self.gday27)+
                                        (self.gday60)+
                                        (self.gday200)+
                                        (self.gkaju28)+
                                        (self.gkaju60)+
                                        (self.gkaju200)+
                                        (self.gchoco60)+
                                        (self.milkbikis264)+
                                        (self.burbun20)+
                                        (self.burbun150)+
                                        (self.tar150)+
                                        (self.sfc300)+
                                        (self.sc100)+
                                        (self.oats150)+
                                        (self.tg29)+
                                        (self.tg43)+
                                        (self.tg85)+
                                        (self.tc33)+
                                        (self.tco33)+
                                        (self.tce33)+
                                        (self.tcv33)
        )  
        self.product_price.set("Rs. "+str(self.total_product_price))
        self.cgst_tax=round((self.total_product_price*0.09),2)
        self.product_price_CGST.set("Rs. "+str(self.cgst_tax))
        self.gst_tax = round((self.total_product_price*0.18),2)
        self.product_price_GST.set("Rs. "+str(self.gst_tax))

        self.Total_bill= float(round(self.total_product_price+
                               self.cgst_tax+
                               self.gst_tax
                               ))
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWELCOME SUDHIR AGENCY\n")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phone.get()}\n")
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")  
        self.textarea.insert(END,f"\n======================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are not filled")
        elif self.product_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product is Purchased")
        else:
            self.welcome_bill()
            if self.vita_248g.get()!=0:
                self.textarea.insert(END,f"\n Vita(248g)\t\t{self.vita_248g.get()}\t\t{self.v248}")
            if self.vita_418g.get()!=0:
                self.textarea.insert(END,f"\n Vita(418g)\t\t{self.vita_418g.get()}\t\t{self.v418}")
            if self.bis_50_29g.get()!=0:
                self.textarea.insert(END,f"\n 50-50(29g)\t\t{self.bis_50_29g.get()}\t\t{self.b_50_29}")
            if self.bis_50_63g.get()!=0:
                self.textarea.insert(END,f"\n 50-50(63g)\t\t{self.bis_50_63g.get()}\t\t{self.b_50_63}")
            if self.bis_50_188g.get()!=0:
                self.textarea.insert(END,f"\n 50-50(188g)\t\t{self.bis_50_188g.get()}\t\t{self.b_50_188}")
            if self.marie_33g.get()!=0:
                self.textarea.insert(END,f"\n Marie Gold(33g)\t\t{self.marie_33g.get()}\t\t{self.m33}")
            if self.marie_63g.get()!=0:
                self.textarea.insert(END,f"\n Marie Gold(63g)\t\t{self.marie_63g.get()}\t\t{self.m63}")
            if self.marie_190g.get()!=0:
                self.textarea.insert(END,f"\n Marie Gold(190g)\t\t{self.marie_190g.get()}\t\t{self.m190}")
            if self.marie_250g.get()!=0:
                self.textarea.insert(END,f"\n Marie Gold(250g)\t\t{self.marie_250g.get()}\t\t{self.m250}")
            if self.marie_400g.get()!=0:
                self.textarea.insert(END,f"\n Marie Gold(400g)\t\t{self.marie_400g.get()}\t\t{self.m400}")
            if self.potazos_24g.get()!=0:
                self.textarea.insert(END,f"\n Potazos(24g)\t\t{self.potazos_24g.get()}\t\t{self.p24}")
            if self.maskachaska_24g.get()!=0:
                self.textarea.insert(END,f"\n MaskaChaska(24g)\t\t{self.maskachaska_24g.get()}\t\t{self.mc24}")
            if self.golmal_200g.get()!=0:
                self.textarea.insert(END,f"\n Golmal(200g)\t\t{self.golmal_200g.get()}\t\t{self.g200}")
            if self.goodday_27g.get()!=0:
                self.textarea.insert(END,f"\n GoodDay(27g)\t\t{self.goodday_27g.get()}\t\t{self.gday27}")
            if self.goodday_60g.get()!=0:
                self.textarea.insert(END,f"\n GoodDay(60g)\t\t{self.goodday_60g.get()}\t\t{self.gday60}")
            if self.goodday_200g.get()!=0:
                self.textarea.insert(END,f"\n GoodDay(200g)\t\t{self.goodday_200g.get()}\t\t{self.gday200}")
            if self.gooddaykaju_28g.get()!=0:
                self.textarea.insert(END,f"\n GoodDayKaju(28g)\t\t{self.gooddaykaju_28g.get()}\t\t{self.gkaju28}")
            if self.gooddaykaju_60g.get()!=0:
                self.textarea.insert(END,f"\n GoodDayKaju(60g)\t\t{self.gooddaykaju_60g.get()}\t\t{self.gkaju60}")
            if self.gooddaykaju_200g.get()!=0:
                self.textarea.insert(END,f"\n GoodDayKaju(200g)\t\t{self.gooddaykaju_200g.get()}\t\t{self.gkaju200}")
            if self.gooddaychoco_60g.get()!=0:
                self.textarea.insert(END,f"\n GoodDayChoco(60g)\t\t{self.gooddaychoco_60g.get()}\t\t{self.gchoco60}")
            if self.milkbikis_264g.get()!=0:
                self.textarea.insert(END,f"\n MilkBikis(264g)\t\t{self.milkbikis_264g.get()}\t\t{self.milkbikis264}")
            if self.burbun_20g.get()!=0:
                self.textarea.insert(END,f"\n BurBun(20g)\t\t{self.burbun_20g.get()}\t\t{self.burbun20}")
            if self.burbun_150g.get()!=0:
                self.textarea.insert(END,f"\n BurBun(150g)\t\t{self.burbun_150g.get()}\t\t{self.burbun150}")
            if self.thinarrowroot_150g.get()!=0:
                self.textarea.insert(END,f"\n ThinArrowRoot(150g)\t\t{self.thinarrowroot_150g.get()}\t\t{self.tar150}")
            if self.sugarfreecracker_300g.get()!=0:
                self.textarea.insert(END,f"\n SugarFreeCracker(300g)\t\t{self.sugarfreecracker_300g.get()}\t\t{self.sfc300}")
            if self.simplecracker_100g.get()!=0:
                self.textarea.insert(END,f"\n SimpleCracker(100g)\t\t{self.simplecracker_100g.get()}\t\t{self.sc100}")  
            if self.oats_150g.get()!=0:
                self.textarea.insert(END,f"\n Britania Oats(300g)\t\t{self.oats_150g.get()}\t\t{self.oats150}")  
            if self.Tglucose_29g.get()!=0:
                self.textarea.insert(END,f"\n Tiger Glucose(29g)\t\t{self.Tglucose_29g.get()}\t\t{self.tg29}")
            if self.Tglucose_43g.get()!=0:
                self.textarea.insert(END,f"\n Tiger Glucose(43g)\t\t{self.Tglucose_43g.get()}\t\t{self.tg43}")
            if self.Tglucose_85g.get()!=0:
                self.textarea.insert(END,f"\n Tiger Glucose(85g)\t\t{self.Tglucose_85g.get()}\t\t{self.tg85}")
            if self.TCchocolate_33g.get()!=0:
                self.textarea.insert(END,f"\n TigerCream Chocolate(33g)\t\t{self.TCchocolate_33g.get()}\t\t{self.tc33}")
            if self.TCOrange_33g.get()!=0:
                self.textarea.insert(END,f"\n TigerCream Orange(33g)\t\t{self.TCOrange_33g.get()}\t\t{self.tco33}")
            if self.TCElaichi_33g.get()!=0:
                self.textarea.insert(END,f"\n TigerCream Elaichi(33g)\t\t{self.TCElaichi_33g.get()}\t\t{self.tce33}")
            if self.TCVanilla_33g.get()!=0:
                self.textarea.insert(END,f"\n TigerCream Vanilla(33g)\t\t{self.TCVanilla_33g.get()}\t\t{self.tcv33}")
            
            self.textarea.insert(END,f"\n--------------------------------------")
            if self.product_price_CGST.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Products CGST\t\t\t{self.product_price_CGST.get()}")
            if self.product_price_GST.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Products GST\t\t\t{self.product_price_GST.get()}")  
            self.textarea.insert(END,f"\n Total Bill :\t\t\tRs. {self.Total_bill}")
            self.textarea.insert(END,f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get("1.0",END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No: {self.bill_no.get()} saved Successfully")
        else:
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present='yes'
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
    
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            
            self.vita_248g.set(0)
            self.vita_418g.set(0)
            self.bis_50_29g.set(0)
            self.bis_50_63g.set(0)
            self.bis_50_188g.set(0)
            self.marie_33g.set(0)
            self.marie_63g.set(0)
            self.marie_190g.set(0)
            self.marie_250g.set(0)
            self.marie_400g.set(0)
            self.potazos_24g.set(0)
            self.maskachaska_24g.set(0)
            self.golmal_200g.set(0)
            self.goodday_27g.set(0)
            self.goodday_60g.set(0)
            self.goodday_200g.set(0)
            self.gooddaykaju_28g.set(0)
            self.gooddaykaju_60g.set(0)
            self.gooddaykaju_200g.set(0)
            self.gooddaychoco_60g.set(0)
            self.milkbikis_264g.set(0)
            self.burbun_20g.set(0)
            self.burbun_150g.set(0)
            self.thinarrowroot_150g.set(0)
            self.simplecracker_100g.set(0)
            self.sugarfreecracker_300g.set(0)
            self.Tglucose_29g.set(0)
            self.Tglucose_43g.set(0)
            self.Tglucose_85g.set(0)
            self.TCchocolate_33g.set(0)
            self.TCOrange_33g.set(0)
            self.TCElaichi_33g.set(0)
            self.TCVanilla_33g.set(0)
            self.oats_150g.set(0)

            #=========Total Price & Tax Variable============#
            self.product_price.set("")
            self.product_price_CGST.set("")
            self.product_price_GST.set("")

            #-========= Customer ========-#
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
root=Tk()
obj = Bill_App(root)
root.mainloop()