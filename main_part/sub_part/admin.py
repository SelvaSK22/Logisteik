from django.contrib import admin
from . models import admin_reg, consig, cus_rev_rep, dis_pay_sum, dispatcht, dri_pay_rep, dri_pay_sum, feedbackt,usert,customert,equipmentst,load_entryt,drivert,shippert
# Register your models here.
admin.site.register(admin_reg)
admin.site.register(consig)
admin.site.register(feedbackt)
admin.site.register(usert)
admin.site.register(dispatcht)
admin.site.register(customert)
admin.site.register(equipmentst)
admin.site.register(load_entryt)
admin.site.register(drivert)
admin.site.register(dri_pay_rep)
admin.site.register(dri_pay_sum)
admin.site.register(dis_pay_sum)
admin.site.register(cus_rev_rep)
admin.site.register(shippert)





