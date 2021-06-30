from django.db import models

# Create your models here.
class admin_reg(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email_id=models.EmailField()
    Password=models.CharField(max_length=15)
    def __str__(self):
        return self.Firstname
class consig(models.Model):
    consig_id=models.CharField(max_length=100)
    consig_name=models.CharField(max_length=100)
    consig_add=models.CharField(max_length=100)
    consig_city=models.CharField(max_length=100)
    consig_state=models.CharField(max_length=100)
    consig_country=models.CharField(max_length=100)
    consig_zip=models.CharField(max_length=100)
    consig_tele=models.CharField(max_length=100)
    consig_email=models.EmailField()
    consig_ext=models.CharField(max_length=100)
    consig_contact=models.IntegerField()
    consig_notes=models.CharField(max_length=100)
    def __str__(self):
        return self.consig_id
class usert(models.Model):
    main_name=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField()
    user_phone=models.IntegerField()
    user_password=models.CharField(max_length=100)
    user_cpassword=models.CharField(max_length=100)
    user_img=models.ImageField(upload_to='image/%Y/%m/%d',null=True,blank=True)
    def __str__(self):
        return self.main_name
class feedbackt(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=300)
    def __str__(self):
        return self.email_id
class customert(models.Model):
    cus_id=models.IntegerField()
    cus_name=models.CharField(max_length=100)
    cus_addr=models.CharField(max_length=100)
    cus_city=models.CharField(max_length=100)
    cus_state=models.CharField(max_length=100)
    cus_country=models.CharField(max_length=100)
    cus_zip=models.IntegerField()
    cus_phone=models.IntegerField()
    cus_email=models.EmailField()
    cus_mc=models.CharField(max_length=100)
    cus_notes=models.CharField(max_length=100)
    def __str__(self):
        return self.cus_name
class dispatcht(models.Model):
    dis_id=models.CharField(max_length=100)
    dis_fname=models.CharField(max_length=100)
    dis_lname=models.CharField(max_length=100)
    dis_phone=models.IntegerField()
    dis_email=models.EmailField()
    dis_rate=models.CharField(max_length=100)
    def __str__(self):
        return self.dis_fname
class shippert(models.Model):
    ship_id=models.IntegerField()
    ship_name=models.CharField(max_length=100)
    ship_addr=models.CharField(max_length=100)
    ship_city=models.CharField(max_length=100)
    ship_state=models.CharField(max_length=100)
    ship_country=models.CharField(max_length=100)
    ship_zip=models.IntegerField()
    ship_phone=models.IntegerField()
    ship_email=models.EmailField()
    ship_ext=models.CharField(max_length=100)
    ship_contact=models.IntegerField()
    ship_notes=models.CharField(max_length=100)
    def __str__(self):
        return self.ship_name
class drivert(models.Model):
    did=models.CharField(max_length=100)
    ddob=models.DateField()
    dfname=models.CharField(max_length=100)
    dlname=models.CharField(max_length=100)
    daddr=models.CharField(max_length=200)
    dcity=models.CharField(max_length=100)
    dstate=models.CharField(max_length=100)
    dzip=models.IntegerField()
    dssn=models.CharField(max_length=100)
    dphone=models.IntegerField()
    demail=models.EmailField()
    dins=models.IntegerField()
    dins1=models.IntegerField()
    difta=models.IntegerField()
    dah=models.CharField(max_length=100)
    dlicnum=models.CharField(max_length=100)
    dlicexp=models.CharField(max_length=100)
    dmeddate=models.CharField(max_length=100)
    dmedexp=models.CharField(max_length=100)
    ddtest=models.CharField(max_length=100)
    dpt=models.CharField(max_length=100)
    dpm=models.CharField(max_length=100)
    dem=models.CharField(max_length=100)
    dper=models.IntegerField()
    dstat=models.CharField(max_length=100)
    dpp=models.IntegerField()
    dlb=models.IntegerField()
    dtrent=models.IntegerField()
    dnote=models.CharField(max_length=200)
    def __str__(self):
        return self.dfname

class equipmentst(models.Model):
    own_fname=models.CharField(max_length=100)
    own_lname=models.CharField(max_length=100)
    unit_no=models.CharField(max_length=100)
    make=models.CharField(max_length=100)
    eq_type=models.CharField(max_length=100)
    year=models.IntegerField()
    VIN=models.CharField(max_length=100)
    p_no=models.CharField(max_length=100)
    p_exp=models.DateField()
    mileage=models.CharField(max_length=100)
    truck=models.CharField(max_length=100)
    trailer=models.CharField(max_length=100)
    province=models.CharField(max_length=100)
    axels=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    start_date=models.DateField()
    deactive_date=models.DateField()
    doti_date=models.DateField()
    ifta_truck=models.CharField(max_length=100)
    ai_date=models.DateField()
    ndi_date=models.DateField()
    def __str__(self):
        return self.own_fname
class load_entryt(models.Model):
    load_id=models.CharField(max_length=100)
    cus_name=models.CharField(max_length=100)
    cus_load=models.CharField(max_length=100)
    load_type=models.CharField(max_length=100)
    load_date=models.DateField()
    pickupdate=models.DateField()
    deliverydate=models.DateField()
    load_dispatch=models.CharField(max_length=100)
    lh_rate=models.IntegerField()
    unloading=models.IntegerField()
    reimburse=models.CharField(max_length=10)
    detention=models.IntegerField()
    layover=models.IntegerField()
    other_c=models.IntegerField()
    total_c=models.IntegerField()
    load_driver=models.CharField(max_length=100)
    truck=models.CharField(max_length=100)
    trailer=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    load_shipper=models.CharField(max_length=100)
    load_addre=models.CharField(max_length=200)
    load_city=models.CharField(max_length=100)
    load_state=models.CharField(max_length=100)
    load_country=models.CharField(max_length=100)
    load_zip=models.IntegerField()
    load_weight=models.CharField(max_length=100)
    load_qty=models.CharField(max_length=100)
    ship_con=models.IntegerField()
    load_note=models.CharField(max_length=200)
    cons_name=models.CharField(max_length=100)
    con_con=models.IntegerField()
    con_addr=models.CharField(max_length=200)
    con_city=models.CharField(max_length=100)
    con_state=models.CharField(max_length=100)
    con_country=models.CharField(max_length=100)
    cons_zip=models.IntegerField()
    def __str__(self):
        return self.cus_name
class cus_rev_rep(models.Model):
    cus_name=models.CharField(max_length=100)
    from_date=models.DateField()
    to_date=models.DateField()
    def __str__(self):
        return self.cus_name
class dis_pay_sum(models.Model):
    dis_fname=models.CharField(max_length=100)
    from_date=models.DateField()
    to_date=models.DateField()
    def __str__(self):
        return self.dis_fname
class dri_pay_rep(models.Model):
    dfname=models.CharField(max_length=100)
    from_date=models.DateField()
    to_date=models.DateField()
    def __str__(self):
        return self.dfname
class dri_pay_sum(models.Model):
    dfname=models.CharField(max_length=100)
    from_date=models.DateField()
    to_date=models.DateField()
    def __str__(self):
        return self.dfname
