from django.shortcuts import render,redirect
from django.utils.functional import empty
from . models import admin_reg,consig, cus_rev_rep, dis_pay_sum, dri_pay_rep, dri_pay_sum,usert,feedbackt,customert,dispatcht,drivert,shippert,equipmentst,load_entryt
import easygui
from django.contrib.auth import logout as log
from django.conf import settings as conf_settings
from django.core.mail import send_mail

multi_user_name=''

# Create your views here.
def index(request):
    return render(request,'Landing/index.html')
def about(request):
    return render(request,'Landing/about.html')
def blog(request):
    return render(request,'Landing/blog.html')
def contact(request):
    return render(request,'Landing/contact.html')
def contact1(request):
    if request.method=='POST':
        feedback_dis=feedbackt(first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                email_id=request.POST['email_id'],
                                subject=request.POST['subject'],
                                message=request.POST['message'])
        feedback_dis.save()
        easygui.msgbox("Your Data Has Been Stored Successfully!...",title="Logisteik")
        return redirect(index)
    return render(request,'Landing/contact.html')
def industries(request):
    return render(request,'Landing/industries.html')
def services(request):
    return render(request,'Landing/services.html')
def admin_login(request):
    if request.method=='POST':
        if admin_reg.objects.filter(Email_id=request.POST['Email_id'],Password=request.POST['Password']).exists():
            check=admin_reg.objects.get(Email_id=request.POST['Email_id'],Password=request.POST['Password'])
            global multi_user_name
            multi_user_name=check.Firstname
            ut_data=admin_reg.objects.get(Firstname=multi_user_name)
            easygui.msgbox("Logged in successfully!...",title="Logisteik")
            return redirect(dashboard)
        else:
            context={'msg':'Invalid Email/Password'}
            return render(request,'Landing/adminlogin.html',context)
    return render(request,'Landing/adminlogin.html')
def admin_register(request):
    return render(request,'Landing/adminregister.html')
def admin_register1(request):
    if request.method=='POST':
        admin_reg_dis=admin_reg(Firstname=request.POST['Firstname'],
                                Lastname=request.POST['Lastname'],
                                Email_id=request.POST['Email_id'],
                                Password=request.POST['Password'])
        admin_reg_dis.save()
        subject="Welcome to Logisteik"
        message = 'HI\n Thanks for Signing Up'
        email_from = conf_settings.EMAIL_HOST_USER
        recepient = request.POST.get('Email_id')
        print("check:",recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently = False)
        easygui.msgbox("Your Data Has Been Stored Successfully!...",title="Logisteik")
        return redirect(admin_login)
    return render(request,'Landing/adminregister.html')
def dashboard(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    return render(request,'Dashboard/index.html',{'ut_data':ut_data})
def add_consignee(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    return render(request,'Dashboard/add-consignee.html',{'ut_data':ut_data})
def add_consignee1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=='POST':
        consig_dis=consig(consig_id=request.POST['consig_id'],
                            consig_name=request.POST['consig_name'],
                            consig_add=request.POST['consig_add'],
                            consig_city=request.POST['consig_city'],
                            consig_state=request.POST['consig_state'],
                            consig_country=request.POST['consig_country'],
                            consig_zip=request.POST['consig_zip'],
                            consig_tele=request.POST['consig_tele'],
                            consig_email=request.POST['consig_email'],
                            consig_ext=request.POST['consig_ext'],
                            consig_contact=request.POST['consig_contact'],
                            consig_notes=request.POST['consig_notes'],
                            )
        consig_dis.save()
        easygui.msgbox("Your Data Has Been Stored Successfully!...",title="Logisteik")
        return redirect(consignee)
    return render(request,'Dashboard/add-consignee.html',{'ut_data':ut_data})
def add_customer(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    return render(request,'Dashboard/add-customer.html',{'ut_data':ut_data})
def add_customer1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=='POST':
        cus_dis=customert(cus_id=request.POST['cus_id'],
                            cus_name=request.POST['cus_name'],
                            cus_addr=request.POST['cus_addr'],
                            cus_city=request.POST['cus_city'],
                            cus_state=request.POST['cus_state'],
                            cus_country=request.POST['cus_country'],
                            cus_zip=request.POST['cus_zip'],
                            cus_phone=request.POST['cus_phone'],
                            cus_email=request.POST['cus_email'],
                            cus_mc=request.POST['cus_mc'],
                            cus_notes=request.POST['cus_notes'])
        cus_dis.save()
        easygui.msgbox("You data is stored successfully!...",title="Logisteik")
        return redirect(customer)
    return render(request,'Dashboard/add-customer.html',{'ut_data':ut_data})
def add_dispatch1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=='POST':
        dis_dis=dispatcht(dis_id=request.POST['dis_id'],
                            dis_fname=request.POST['dis_fname'],
                            dis_lname=request.POST['dis_lname'],
                            dis_phone=request.POST['dis_phone'],
                            dis_email=request.POST['dis_email'],
                            dis_rate=request.POST['dis_rate'])
        dis_dis.save()
        easygui.msgbox("Your data has been stored successfully!...",title="Logisteik")
        return redirect(dispatch)
    return render(request,'Dashboard/add-dispatch.html',{'ut_data':ut_data})
def add_dispatch(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    return render(request,'Dashboard/add-dispatch.html',{'ut_data':ut_data})
def add_driver(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    return render(request,'Dashboard/add-driver.html',{'ut_data':ut_data})
def add_driver1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=='POST':
        dri_dis=drivert(did=request.POST['did'],
                        ddob=request.POST['ddob'],
                        dfname=request.POST['dfname'],
                        dlname=request.POST['dlname'],
                        daddr=request.POST['daddr'],
                        dcity=request.POST['dcity'],
                        dstate=request.POST['dstate'],
                        dzip=request.POST['dzip'],
                        dssn=request.POST['dssn'],
                        dphone=request.POST['dphone'],
                        demail=request.POST['demail'],
                        dins=request.POST['dins'],
                        dins1=request.POST['dins1'],
                        difta=request.POST['difta'],
                        dah=request.POST['dah'],
                        dlicnum=request.POST['dlicnum'],
                        dlicexp=request.POST['dlicexp'],
                        dmeddate=request.POST['dmeddate'],
                        dmedexp=request.POST['dmedexp'],
                        ddtest=request.POST['ddtest'],
                        dpt=request.POST['dpt'],
                        dpm=request.POST['dpm'],
                        dem=request.POST['dem'],
                        dper=request.POST['dper'],
                        dstat=request.POST['dstat'],
                        dpp=request.POST['dpp'],
                        dlb=request.POST['dlb'],
                        dtrent=request.POST['dtrent'],
                        dnote=request.POST['dnote'])
        dri_dis.save()
        easygui.msgbox("Your data has been stored successfully!...")
        return redirect(driver)
    return render(request,'Dashboard/add-driver.html',{'ut_data':ut_data})
def add_equipments(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    return render(request,'Dashboard/add-equipments.html',{'ut_data':ut_data})
def add_equipments1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if(request.method=='POST'):
        equi_dis=equipmentst(own_fname=request.POST['own_fname'],
own_lname=request.POST['own_lname'],
unit_no=request.POST['unit_no'],
make=request.POST['make'],
eq_type=request.POST['eq_type'],
year=request.POST['year'],
VIN=request.POST['VIN'],
p_no=request.POST['p_no'],
p_exp=request.POST['p_exp'],
mileage=request.POST['mileage'],
truck=request.POST['truck'],
trailer=request.POST['trailer'],
province=request.POST['province'],
axels=request.POST['axels'],
fuel_type=request.POST['fuel_type'],
weight=request.POST['weight'],
start_date=request.POST['start_date'],
deactive_date=request.POST['deactive_date'],
doti_date=request.POST['doti_date'],
ifta_truck=request.POST['ifta_truck'],
ai_date=request.POST['ai_date'],
ndi_date=request.POST['ndi_date'])
        equi_dis.save()
        easygui.msgbox("your data has been stored successfully!...")
        return redirect(equipment)
    return render(request,'Dashboard/add-equipments.html',{'ut_data':ut_data})
def add_loadentry(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    cus=customert.objects.all()
    disp=dispatcht.objects.all()
    driv=drivert.objects.all()
    ship=shippert.objects.all()
    cons=consig.objects.all()
    return render(request,'Dashboard/add-load-entry.html',{'cus':cus,'disp':disp,'driv':driv,'ship':ship,'cons':cons,'ut_data':ut_data})
def add_loadentry1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=='POST':
        load_dis=load_entryt(load_id=request.POST['load_id'],
                                cus_name=request.POST['cus_name'],
                                cus_load=request.POST['cus_load'],
                                load_type=request.POST['load_type'],
                                load_date=request.POST['load_date'],
                                pickupdate=request.POST['pickupdate'],
                                deliverydate=request.POST['deliverydate'],
                                load_dispatch=request.POST['load_dispatch'],
                                lh_rate=request.POST['lh_rate'],
                                unloading=request.POST['unloading'],
                                reimburse=request.POST['reimburse'],
                                detention=request.POST['detention'],
                                layover=request.POST['layover'],
                                other_c=request.POST['other_c'],
                                total_c=request.POST['total_c'],
                                load_driver=request.POST['load_driver'],
                                truck=request.POST['truck'],
                                trailer=request.POST['trailer'],
                                rate=request.POST['rate'],
                                load_shipper=request.POST['load_shipper'],
                                load_addre=request.POST['load_addr'],
                                load_city=request.POST['load_city'],
                                load_state=request.POST['load_state'],
                                load_country=request.POST['load_country'],
                                load_zip=request.POST['load_zip'],
                                load_weight=request.POST['load_weight'],
                                load_qty=request.POST['load_qty'],
                                ship_con=request.POST['ship_con'],
                                load_note=request.POST['load_note'],
                                cons_name=request.POST['cons_name'],
                                con_con=request.POST['con_con'],
                                con_addr=request.POST['con_addr'],
                                con_city=request.POST['con_city'],
                                con_state=request.POST['con_state'],
                                con_country=request.POST['con_country'],
                                cons_zip=request.POST['cons_zip'])
        load_dis.save()
        easygui.msgbox("Your data has been stored successfully!...")
        return redirect(load_entry)
    return render(request,'Dashboard/add-load-entry.html',{'ut_data':ut_data})
def add_shipper(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    return render(request,'Dashboard/add-shipper.html',{'ut_data':ut_data})
def add_shipper1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=='POST':
        ship_dis=shippert(ship_id=request.POST['ship_id'],
                            ship_name=request.POST['ship_name'],
                            ship_addr=request.POST['ship_addr'],
                            ship_city=request.POST['ship_city'],
                            ship_state=request.POST['ship_state'],
                            ship_country=request.POST['ship_country'],
                            ship_zip=request.POST['ship_zip'],
                            ship_phone=request.POST['ship_phone'],
                            ship_email=request.POST['ship_email'],
                            ship_ext=request.POST['ship_ext'],
                            ship_contact=request.POST['ship_contact'],
                            ship_notes=request.POST['ship_notes'])
        ship_dis.save()
        easygui.msgbox("You data is stored successfully!...",title="Logisteik")
        return redirect(shippers)
    return render(request,'Dashboard/add-shipper.html',{'ut_data':ut_data})
def add_user(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    return render(request,'Dashboard/add-user.html',{'ut_data':ut_data})
def add_user1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=='POST':
        user_dis=usert()
        user_dis.main_name=request.POST.get('main_name')
        user_dis.user_name=request.POST.get('user_name')
        user_dis.user_email=request.POST.get('user_email')
        user_dis.user_phone=request.POST.get('user_phone')
        user_dis.user_password=request.POST.get('user_password')
        user_dis.user_cpassword=request.POST.get('user_cpassword')
        if len(request.FILES) != 0:
            user_dis.user_img=request.FILES['user_img']
        user_dis.save()
        easygui.msgbox("Your data has been stored successfully!...",title="Logisteik")
        return redirect(user)
    return render(request,'Dashboard/add-user.html',{'ut_data':ut_data})
def consignee(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    con=consig.objects.all()
    return render(request,'Dashboard/consignee.html',{'con':con,'ut_data':ut_data})
def customer(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    cus=customert.objects.all()
    return render(request,'Dashboard/customer.html',{'cus':cus,'ut_data':ut_data})
def customer_revenue_report(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    cus=customert.objects.all()
    return render(request,'Dashboard/customer-revenue-report.html',{'cus':cus,'ut_data':ut_data})
def customer_revenue_report1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=="POST":
        dis_crr=cus_rev_rep(cus_name=request.POST['cus_name'],
                            from_date=request.POST['from_date'],
                            to_date=request.POST['to_date'])
        dis_crr.save()
        easygui.msgbox("Your data has been stored successfully!...",title="Logisteik")
        return redirect(dashboard)
    return render(request,'Dashboard/customer-revenue-report.html',{'ut_data':ut_data})
def dispatch_pay_summary(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    disp=dispatcht.objects.all()
    return render(request,'Dashboard/dispatch-pay-summary.html',{'disp':disp,'ut_data':ut_data})
def dispatch_pay_summary1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=="POST":
        dis_dps=dis_pay_sum(dis_fname=request.POST['dis_fname'],
                            from_date=request.POST['from_date'],
                            to_date=request.POST['to_date'])
        dis_dps.save()
        easygui.msgbox("Your data has been stored successfully!...",title="Logisteik")
        return redirect(dashboard)
    return render(request,'Dashboard/dispatch-pay-summary.html',{'ut_data':ut_data})
def dispatch(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    dis=dispatcht.objects.all()
    return render(request,'Dashboard/dispatch.html',{'dis':dis,'ut_data':ut_data})
def driver_pay_report(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    driv=drivert.objects.all()
    return render(request,'Dashboard/driver-pay-report.html',{'driv':driv,'ut_data':ut_data})
def driver_pay_report1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=="POST":
        dis_dpr=dri_pay_rep(dfname=request.POST['dfname'],
                            from_date=request.POST['from_date'],
                            to_date=request.POST['to_date'])
        dis_dpr.save()
        easygui.msgbox("Your data has been stored successfully!...",title="Logisteik")
        return redirect(dashboard)
    return render(request,'Dashboard/driver-pay-report.html',{'ut_data':ut_data})
def driver_pay_summary(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    driv=drivert.objects.all()
    return render(request,'Dashboard/driver-pay-summary.html',{'driv':driv,'ut_data':ut_data})
def driver_pay_summary1(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    if request.method=="POST":
        dis_dpr=dri_pay_sum(dfname=request.POST['dfname'],
                            from_date=request.POST['from_date'],
                            to_date=request.POST['to_date'])
        dis_dpr.save()
        easygui.msgbox("Your data has been stored successfully!...",title="Logisteik")
        return redirect(dashboard)
    return render(request,'Dashboard/driver-pay-summary.html',{'ut_data':ut_data})
def driver(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    dri=drivert.objects.all()
    return render(request,'Dashboard/driver.html',{'dri':dri,'ut_data':ut_data})
def equipment(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    equip=equipmentst.objects.all()
    return render(request,'Dashboard/equipment.html',{'equip':equip,'ut_data':ut_data})
def load_entry(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    load=load_entryt.objects.all()
    return render(request,'Dashboard/load-entry.html',{'load':load,'ut_data':ut_data})
def shippers(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    ship=shippert.objects.all()
    return render(request,'Dashboard/shippers.html',{'ship':ship,'ut_data':ut_data})
def user(request):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    prodects=usert.objects.all()
    return render(request,'Dashboard/user.html',{'prodects':prodects,'ut_data':ut_data})
def edituserpage(request,id):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    user1=usert.objects.get(id=id)
    return render(request,'Dashboard/edit_user.html',{'user1':user1,'ut_data':ut_data})
def edit_user(request,id):
    if request.method == 'POST':
        user2=usert(id=id,
        main_name=request.POST['main_name'],
        user_name=request.POST['user_name'],
        user_email=request.POST['user_email'],
        user_phone=request.POST['user_phone'],
        user_password=request.POST['user_password'],
        user_cpassword=request.POST['user_cpassword'],
        user_img=request.FILES['user_img'])
    user2.save()
    easygui.msgbox("Your data has been updated successfully!...")
    return redirect(user)
def del_user(request,id):
    user1=usert.objects.get(id=id)
    user1.delete()
    return redirect(user)
def adminlogout(request):
    log(request)
    return render(request,'Landing/adminlogin.html')
def edit_dispatch(request,id):
    ut_data=admin_reg.objects.get(Firstname=multi_user_name)
    user1=dispatcht.objects.get(id=id)
    return render(request,'Dashboard/edit_dispatch.html',{'user1':user1,'ut_data':ut_data})
def edit_dis(request,id):
    if request.method=='POST':
        dis_dis=dispatcht(id=id,
                            dis_id=request.POST['dis_id'],
                            dis_fname=request.POST['dis_fname'],
                            dis_lname=request.POST['dis_lname'],
                            dis_phone=request.POST['dis_phone'],
                            dis_email=request.POST['dis_email'],
                            dis_rate=request.POST['dis_rate'])
        dis_dis.save()
        easygui.msgbox("Your data has been updated successfully!...",title="Logisteik")
        return redirect(dispatch)
def del_dis(request,id):
    user1=dispatcht.objects.get(id=id)
    user1.delete()
    return redirect(user)