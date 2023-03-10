from tkinter import*
from tkinter import ttk, messagebox
import random, time, datetime

root = Tk()
root.geometry("1350x700+0+0")
root.title("Online Ordering System")
# root.configure(background='black')


# ======================== Variable Declaration ===================================
CustomerRef = IntVar()
Tax = IntVar()
SubTotal = IntVar()
TotalCost = IntVar()
CostofFerreroRocher = StringVar()
CostofFudgeBrownie = StringVar()
CostofChocolateOreo = StringVar()
CostofStrawberry = StringVar()
CostofDelivery = StringVar()
CustomerName = StringVar()
CustomerPhone = IntVar()
CustomerEmail = StringVar()
TimeofOrder = StringVar()
DateofOrder = StringVar()
Discount = IntVar()
UnitPriceFerreroRocher  = StringVar()
UnitPriceFudgeBrownie = StringVar()
UnitPriceChocolateOreo = StringVar()
UnitPriceStrawberry = StringVar()
QtyFerreroRocher = IntVar()
QtyFudgeBrownie = IntVar()
QtyChocolateOreo = IntVar()
QtyStrawberry = IntVar()
# cost_fer = StringVar()
# cost_fudg = StringVar()
# cost_choco = StringVar()
# cost_straw = StringVar()
# ref_paid = StringVar()
# SubTotal_info = StringVar()

# ==================================================================
fer = ('₹' + str('%.2f' % (1099.00)))
piz = ('₹' + str('%.2f' % (139.00)))
chilli = ('₹' + str('%.2f' % (129.00)))
smot = ('₹' + str('%.2f' % (169.00)))
dis = ('₹' + str('%.2f' % (49.00)))


# order_ref = random.randint(20000, 109467)

# ============================ Functions ============================
def Exit():
    qExit = messagebox.askyesno("Ordering System", "Do you want to exit the system")
    if qExit > 0:
        root.destroy()
        return

def time_c():
    Timeof_Order = time.strftime("%H:%M:%S")
    return Timeof_Order

def Reset():
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    TimeofOrder.set(time_c())
    DateofOrder.set(time.strftime("%d/%m/%Y"))
    QtyFerreroRocher.set(0)
    QtyFudgeBrownie.set(0)
    QtyChocolateOreo.set(0)
    QtyStrawberry.set(0)
    CostofFerreroRocher.set(0)
    CostofFudgeBrownie.set(0)
    CostofChocolateOreo.set(0)
    CostofStrawberry.set(0)
    UnitPriceFerreroRocher.set(fer)
    UnitPriceFudgeBrownie.set(piz)
    UnitPriceChocolateOreo.set(chilli)
    UnitPriceStrawberry.set(smot)
    Discount.set(dis)
 
def OrderRef():
    Refpay = random.randint(76472, 209467)
    # Refpaid = ("MB" + str(Refpay))
    CustomerRef.set(Refpay)
    return Refpay

def CostofOrder():
    Qty1 = float(QtyFerreroRocher.get())
    Qty2 = float(QtyFudgeBrownie.get())
    Qty3 = float(QtyChocolateOreo.get())
    Qty4 = float(QtyStrawberry.get())

    UnitPrice1 = 1099.00
    UnitPrice2 = 139.00
    UnitPrice3 = 129.00
    UnitPrice4 = 169.00

    CostofCake1 = '₹', str('%.2f' % (Qty1 * UnitPrice1))
    CostofCake2 = '₹', str('%.2f' % (Qty2 * UnitPrice2))
    CostofCake3 = '₹', str('%.2f' % (Qty3 * UnitPrice3))
    CostofCake4 = '₹', str('%.2f' % (Qty4 * UnitPrice4))

    CostofFerreroRocher.set(CostofCake1)
    CostofFudgeBrownie.set(CostofCake2)
    CostofChocolateOreo.set(CostofCake3)
    CostofStrawberry.set(CostofCake4)

    CostCake1 = (Qty1 * UnitPrice1)
    CostCake2 = (Qty2 * UnitPrice2)
    CostCake3 = (Qty3 * UnitPrice3)
    CostCake4 = (Qty4 * UnitPrice4)

    AllCost = ((Qty1 * UnitPrice1) + (Qty2 * UnitPrice2) + (Qty3 * UnitPrice3) + (Qty4 * UnitPrice4))
    TaxAll = ('₹' + str('%.2f' % ((AllCost) * 0.18)))
    Tax.set(TaxAll)

    SubTotalp = ('₹' + str('%.2f' % (AllCost)))
    SubTotal.set(SubTotalp)

    TotalCostp = ('₹' + str('%.2f' % ((AllCost + ((AllCost) * 0.18)) - 49)))
    TotalCost.set(TotalCostp)
    return

def Save():
    CustomerRef_info = OrderRef()
    CustomerName_info = CustomerName.get()
    CustomerPhone_info = CustomerPhone.get()
    CustomerEmail_info = CustomerEmail.get()
    QtyFerreroRocher_info = QtyFerreroRocher.get()
    QtyFudgeBrownie_info = QtyFudgeBrownie.get()
    QtyChocolateOreo_info = QtyChocolateOreo.get()
    QtyStrawberry_info = QtyStrawberry.get()
    UnitPriceFerreroRocher_info = fer
    UnitPriceFudgeBrownie_info = piz
    UnitPriceChocolateOreo_info = chilli
    UnitPriceStrawberry_info = smot
    all_cost = ((QtyFerreroRocher_info * 1099.00) + (QtyFudgeBrownie_info * 139) + (QtyChocolateOreo_info * 129) + (QtyStrawberry_info * 169))

    SubTotal_info = ('₹' + str('%.2f' % (all_cost)))

    Tax_info =  ('₹' + str('%.2f' % ((all_cost) * 0.18)))

    TotalCost_info = ('₹' + str('%.2f' % ((all_cost + ((all_cost) * 0.18)) - 49)))

    CostofFerreroRocher_info = ('₹' + str('%.2f' % (QtyFerreroRocher_info * 1099.00)))
    CostofFudgeBrownie_info = ('₹' + str('%.2f' % (QtyFudgeBrownie_info * 139)))
    CostofChocolateOreo_info = ('₹' + str('%.2f' % (QtyChocolateOreo_info * 129)))
    CostofStrawberry_info = ('₹' + str('%.2f' % (QtyStrawberry_info * 169)))
    Discount_info = dis
    TimeofOrder_info = time_c()
    DateofOrder_info = time.strftime("%d/%m/%Y")

    print(CustomerRef_info ,CustomerName_info, CustomerEmail_info, CustomerPhone_info, QtyFerreroRocher_info, QtyFudgeBrownie_info, QtyChocolateOreo_info, QtyStrawberry_info, UnitPriceFerreroRocher_info, UnitPriceFudgeBrownie_info, UnitPriceChocolateOreo_info, UnitPriceStrawberry_info, TotalCost_info, SubTotal_info, Tax_info, CostofFerreroRocher_info, CostofFudgeBrownie_info, CostofStrawberry_info, CostofChocolateOreo_info, TimeofOrder_info ,Discount_info, DateofOrder_info)

    file = open('user.txt', 'a', encoding='utf-8')
    file.write('Order Id: ' + str(CustomerRef_info)) 
    file.write('\n')
    file.write('Date: ' + DateofOrder_info) 
    file.write('\t')
    file.write('Time: ' + TimeofOrder_info) 
    file.write('\n')
    file.write('Name: ' + CustomerName_info) 
    file.write('\t')
    file.write('Phone: ' + str(CustomerPhone_info)) 
    file.write('\t')
    file.write('Email: ' + CustomerEmail_info) 
    file.write('\n')
    file.write('Ferrero Rocher Truffle Cake: ' + str(QtyFerreroRocher_info))
    file.write('\t')
    file.write('Price: ' + fer) 
    file.write('\n')
    file.write('Pizza Style Momos: ' + str(QtyFudgeBrownie_info)) 
    file.write('\t')
    file.write('Price: ' + UnitPriceFudgeBrownie_info) 
    file.write('\n')
    file.write('Chilli Chaap Roll: ' + str(QtyChocolateOreo_info)) 
    file.write('\t')
    file.write('Price: ' + UnitPriceChocolateOreo_info) 
    file.write('\n')
    file.write('Smoothie: ' + str(QtyStrawberry_info)) 
    file.write('\t')
    file.write('Price: ' + UnitPriceStrawberry_info) 
    file.write('\n')
    file.write('Discount: ' + Discount_info) 
    file.write('\t')
    file.write('Tax: ' + str(Tax_info)) 
    file.write('\n')
    file.write('Sub Total: ' + str(SubTotal_info)) 
    file.write('\n')
    file.write('Total: ' + str(TotalCost_info)) 
    file.write('\n')
    file.write('\n')
    file.write('\n')
    file.write('\n')
    file.close()
#===================Initialize variables===============================
CostofFerreroRocher.set(0)
CustomerPhone.set("")
CostofFudgeBrownie.set(0)
CostofChocolateOreo.set(0)
CostofStrawberry.set(0)
CostofDelivery.set(0) 
UnitPriceFerreroRocher.set(fer)
UnitPriceFudgeBrownie.set(piz)
UnitPriceChocolateOreo.set(chilli)
UnitPriceStrawberry.set(smot)
QtyFerreroRocher.set(0)
QtyFudgeBrownie.set(0)
QtyChocolateOreo.set(0)
QtyStrawberry.set(0)
Discount.set(dis)
TimeofOrder.set(time_c())  # Time
DateofOrder.set(time.strftime("%d/%m/%Y"))  # Date

# ======================== Main Frame ================================
Tops = Label(root, width=1350, height=50, bd=13, relief="groove")
Tops.pack(side=TOP, fill=X)
LF = Frame(root, width=700, height=650, bd=16, relief="groove")
LF.pack(side=LEFT,fill=Y)
RF = Frame(root, width=600, height=650, bd=16, relief="groove")
RF.pack(side=RIGHT, fill=Y)

Tops.configure(background='brown')
LF.configure(background='brown')
RF.configure(background='brown')

LeftInsideLF = Frame(LF, width=700, height=100, bd=8, relief="raise", bg='navajo white')
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF = Frame(LF, width=700, height=600, bd=8, relief="raise", bg='navajo white')
LeftInsideLFLF.place(x=0, y=210, height=350)


RightInsideLF = Frame(RF, width=604, height=200, bd=8, relief="raise", bg='navajo white')
RightInsideLF.pack(side=TOP)
RightInsideLFLF = Frame(RF, width=306, height=400, bd=8, relief="raise", bg='navajo white')
RightInsideLFLF.place(x=0, y=200, height=355)
RightInsideRFRF = Frame(RF, width=300, height=400, bd=8, relief="raise", bg='navajo white')
RightInsideRFRF.place(x=395, y=200, height=355)


# ========================Project Title =======================================
lblInfo = Label(Tops, font=('Footlight MT Light', 45, 'bold'), text="Panaderia De Pasteles", bd=10, fg='yellow', bg='brown')
lblInfo.pack(side=TOP)

# ======================== Top left Frame =====================================
lblCustomerName = Label(LeftInsideLF, font=('Baskerville Old Face', 14, 'bold'), text='Customer Name', fg='black', bd=10, anchor='w', bg='navajo white')
lblCustomerName.grid(row=0, column=0)
txtCustomerName = Entry(LeftInsideLF, font=('Helvetica', 14), bd=20, width=43, bg='azure2', justify='left', textvariable=CustomerName)
txtCustomerName.grid(row=0, column=1, padx=7)

lblCustomerPhone = Label(LeftInsideLF, font=('Baskerville Old Face', 14, 'bold'), text='Customer Phone', fg='black', bd=10, anchor='w', bg='navajo white')
lblCustomerPhone.grid(row=1, column=0)
txtCustomerPhone = Entry(LeftInsideLF, font=('Helvetica', 14), bd=20, width=43, bg='azure2', justify='left', textvariable=CustomerPhone)
txtCustomerPhone.grid(row=1, column=1)

lblCustomerEmail = Label(LeftInsideLF, font=('Baskerville Old Face', 14, 'bold'), text='Customer Email', fg='black', bd=10, anchor='w', bg='navajo white')
lblCustomerEmail.grid(row=2, column=0)
txtCustomerEmail = Entry(LeftInsideLF, font=('Helvetica', 14), bd=20, width=43, bg='azure2', justify='left', textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2, column=1)

# ======================== Top Right Frame ===================================
lblDateofOrder = Label(RightInsideLF, font=('Baskerville Old Face', 13, 'bold'), text='Date of Order', bd=10, fg='black', bg='navajo white',anchor='w')
lblDateofOrder.grid(row=0, column=0)
txtDateofOrder = Entry(RightInsideLF, font=('Helvetica', 12, 'bold'), bd=20, width=42, bg='azure2', justify='left', textvariable=DateofOrder) 
txtDateofOrder.grid(row=0, column=1, padx=5) 

lblTimeofOrder = Label(RightInsideLF, font=('Baskerville Old Face', 13, 'bold'), text='Time of Order', bd=10, fg='black', bg='navajo white',anchor='w')
lblTimeofOrder.grid(row=1, column=0)
txtTimeofOrder = Entry(RightInsideLF, font=('Helvetica', 12, 'bold'), bd=20, width=42, bg='azure2', justify='left', textvariable=TimeofOrder) 
txtTimeofOrder.grid(row=1, column=1)  

lblCustomerRef = Label(RightInsideLF, font=('Baskerville Old Face', 13, 'bold'), text='Customer Ref', bd=10, fg='black', bg='navajo white',anchor='w')
lblCustomerRef.grid(row=2, column=0)
txtCustomerRef = Entry(RightInsideLF, font=('Helvetica', 12, 'bold'), bd=20, width=42, bg='azure2', justify='left', textvariable=CustomerRef) 
txtCustomerRef.grid(row=2, column=1)  

# ======================== Right Frame ================================================
lblMethodOfPayment = Label(RightInsideLFLF, font=('Baskerville Old Face', 12, 'bold'), text='Method of Payment', bd=16, fg='black', bg='navajo white', anchor="w")
lblMethodOfPayment.grid(row=0, column=0)

cmdMethodOfPayment = ttk.Combobox(RightInsideLFLF, font=('arial', 10, 'bold'), state="readonly")
cmdMethodOfPayment['value'] = (' ', 'Cash', 'Debit Card', 'Visa Card', 'Master Card')
cmdMethodOfPayment.set('Cash')
cmdMethodOfPayment.grid(row=0, column=1)

lblDiscount = Label(RightInsideLFLF, font=('Baskerville Old Face', 13, 'bold'), text="Discount", fg='black', bd=16, anchor='w', bg='navajo white')
lblDiscount.grid(row=1, column=0)
txtDiscount = Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=16, width=18, bg='azure2', justify='left', textvariable=Discount)
txtDiscount.configure(state='disabled')
txtDiscount.grid(row=1, column=1, pady=8, padx=3)

lblTax = Label(RightInsideLFLF, font=('Baskerville Old Face', 13, 'bold'), text="Tax", fg='black', bd=16, anchor='w', bg='navajo white')
lblTax.grid(row=2, column=0)
txtTax = Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=16, width=18, bg='azure2', justify='left', textvariable=Tax)
txtTax.grid(row=2, column=1, pady=8)

lblSubTotal = Label(RightInsideLFLF, font=('Baskerville Old Face', 13, 'bold'), text="Sub Total", fg='black', bd=16, anchor='w', bg='navajo white')
lblSubTotal.grid(row=3, column=0)
txtSubTotal = Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=16, width=18, bg='azure2', justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1, pady=8)

lblTotalCost = Label(RightInsideLFLF, font=('Baskerville Old Face', 13, 'bold'), text="Total Cost", fg='black', bd=16, anchor='w', bg='navajo white')
lblTotalCost.grid(row=4, column=0)
txtTotalCost = Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=16, width=18, bg='azure2', justify='left', textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1, pady=8)

# ======================== Bottom Left Frame ===========================
# =========== labels =============
lblItemOrder = Label(LeftInsideLFLF, font=('High Tower Text', 15, 'bold'), text='Item Order', fg='black', bd=20, bg='navajo white')
lblItemOrder.grid(row=0, column=0)

lblQty = Label(LeftInsideLFLF, font=('High Tower Text', 15, 'bold'), text='Qty', fg='black', bd=20, bg='navajo white')
lblQty.grid(row=0, column=1)

lblUnitPrice = Label(LeftInsideLFLF, font=('High Tower Text', 15, 'bold'), text='Unit Price', fg='black', bd=20, bg='navajo white')
lblUnitPrice.grid(row=0, column=2)

lblCostofItem = Label(LeftInsideLFLF, font=('High Tower Text', 15, 'bold'), text='Cost of Item', fg='black', bd=20, bg='navajo white')
lblCostofItem.grid(row=0, column=3)

# ============= Products Label ================
lblFerrero = Label(LeftInsideLFLF, font=('Georgia', 12), text='Ferrero Rocher Truffle Cake', fg='black', bd=8, bg='navajo white')
lblFerrero.grid(row=1, column=0)

lblFudge = Label(LeftInsideLFLF, font=('Georgia', 12), text='Pizza Style Momos', fg='black', bd=8, bg='navajo white')
lblFudge.grid(row=2, column=0)

lblchocolate = Label(LeftInsideLFLF, font=('Georgia', 12), text='Chilli Chaap Roll', fg='black', bd=8, bg='navajo white')
lblchocolate.grid(row=3, column=0)

lblStrawberry = Label(LeftInsideLFLF, font=('Georgia', 12), text='Smoothie', fg='black', bd=8, bg='navajo white')
lblStrawberry.grid(row=4, column=0)
# ============= Product Text ============
txtQtyFerrero = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=QtyFerreroRocher)
txtQtyFerrero.grid(row=1, column=1)

txtQtyFudge = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=QtyFudgeBrownie)
txtQtyFudge.grid(row=2, column=1)

txtQtyChocolate = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=QtyChocolateOreo)
txtQtyChocolate.grid(row=3, column=1)

txtQtyStrawberry = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=QtyStrawberry)
txtQtyStrawberry.grid(row=4, column=1)

# =====================
txtUnitPriceFerrero = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=UnitPriceFerreroRocher)
txtUnitPriceFerrero.grid(row=1, column=2)

txtUnitPriceFudge = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=UnitPriceFudgeBrownie)
txtUnitPriceFudge.grid(row=2, column=2)

txtUnitPriceChocolate = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=UnitPriceChocolateOreo)
txtUnitPriceChocolate.grid(row=3, column=2)

txtUnitPriceStrawberry = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=UnitPriceStrawberry)
txtUnitPriceStrawberry.grid(row=4, column=2)

# ======================
txtCostofFerrero = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=CostofFerreroRocher)
txtCostofFerrero.grid(row=1, column=3)

txtCostofFudge = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=CostofFudgeBrownie)
txtCostofFudge.grid(row=2, column=3)

txtCostofChocolate = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=CostofChocolateOreo)
txtCostofChocolate.grid(row=3, column=3)

txtCostofStrawberry = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=13, bg="azure2", justify='left', textvariable=CostofStrawberry)
txtCostofStrawberry.grid(row=4, column=3)

# ======================== Buttons Right Frame ===========================
btnTotalCost = Button(RightInsideRFRF,pady=8, bd=8, fg="black", font=('Footlight MT Light', 14, 'bold'), width=12,
                text="Total Cost", bg="lightsalmon", command=CostofOrder).grid(row=0, column=0,padx=9, pady=2)
btnReset = Button(RightInsideRFRF,pady=8, bd=8, fg="black", font=('Footlight MT Light', 14, 'bold'), width=12, 
                text="Reset", bg="lightsalmon", command=Reset).grid(row=1, column=0, pady=2)
btnOrderRef = Button(RightInsideRFRF,pady=8, bd=8, fg="black", font=('Footlight MT Light', 14, 'bold'), width=12, 
                text="Order Ref", bg="lightsalmon", command=OrderRef).grid(row=2, column=0, pady=2)
btnSave = Button(RightInsideRFRF,pady=8, bd=8, fg="black", font=('Footlight MT Light', 14, 'bold'), width=12, 
                text="Save", bg="lightsalmon", command=Save).grid(row=3, column=0, pady=2)
btnExit = Button(RightInsideRFRF,pady=8, bd=8, fg="black", font=('Footlight MT Light', 14, 'bold'), width=12, 
                text="Exit", bg="lightsalmon", command=Exit).grid(row=4, column=0, pady=2)

root.mainloop()