from django.urls import path
from  . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('contact1',views.contact1,name='contact1'),
    path('industries',views.industries,name='industries'),
    path('services',views.services,name='services'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_register',views.admin_register,name='admin_register'),
    path('admin_register1',views.admin_register1,name='admin_register1'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_consignee',views.add_consignee,name='add_consignee'),
    path('add_consignee1',views.add_consignee1,name='add_consignee1'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('add_customer1',views.add_customer1,name='add_customer1'),
    path('add_dispatch',views.add_dispatch,name='add_dispatch'),
    path('add_dispatch1',views.add_dispatch1,name='add_dispatch1'),
    path('add_driver',views.add_driver,name='add_driver'),
    path('add_driver1',views.add_driver1,name='add_driver1'),
    path('add_equipments',views.add_equipments,name='add_equipments'),
    path('add_equipments1',views.add_equipments1,name='add_equipments1'),
    path('add_loadentry',views.add_loadentry,name='add_loadentry'),
    path('add_loadentry1',views.add_loadentry1,name='add_loadentry1'),
    path('add_shipper',views.add_shipper,name='add_shipper'),
    path('add_shipper1',views.add_shipper1,name='add_shipper1'),
    path('add_user',views.add_user,name='add_user'),
    path('add_user1',views.add_user1,name='add_user1'),
    path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    path('edituserpage/<int:id>',views.edituserpage,name='edituserpage'),
    path('del_user/<int:id>',views.del_user,name='del_user'),
    path('consignee',views.consignee,name='consignee'),
    path('dispatch_pay_summary',views.dispatch_pay_summary,name='dispatch_pay_summary'),
    path('dispatch_pay_summary1',views.dispatch_pay_summary1,name='dispatch_pay_summary1'),
    path('dispatch',views.dispatch,name='dispatch'),
    path('driver_pay_report',views.driver_pay_report,name='driver_pay_report'),
    path('driver_pay_report1',views.driver_pay_report1,name='driver_pay_report1'),
    path('driver_pay_summary',views.driver_pay_summary,name='driver_pay_summary'),
    path('driver_pay_summary1',views.driver_pay_summary1,name='driver_pay_summary1'),
    path('driver',views.driver,name='driver'),
    path('equipment',views.equipment,name='equipment'),
    path('load_entry',views.load_entry,name='load_entry'),
    path('shippers',views.shippers,name='shippers'),
    path('user',views.user,name='user'), 
    path('customer',views.customer,name='customer'),
    path('customer_revenue_report',views.customer_revenue_report,name='customer_revenue_report'),
    path('customer_revenue_report1',views.customer_revenue_report1,name='customer_revenue_report1'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('edit_dis/<int:id>',views.edit_dis,name='edit_dis'),
    path('edit_dispatch/<int:id>',views.edit_dispatch,name='edit_dispatch'),
    path('del_dis/<int:id>',views.del_dis,name='del_dis'),
    ]