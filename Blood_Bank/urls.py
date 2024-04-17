
from django.contrib import admin
from django.urls import path
from blood_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('admin_home', admin_home, name='admin_home'),
    path('about', About, name='about'),
    path('contact', Contact, name='contact'),
    path('gallery', Gallery, name='gallery'),
    path('login/', Login_User, name='login'),
    path('profile', profile, name='profile'),
    path('admin_login', admin_login, name='admin_login'),
    path('signup', Signup_User, name='signup'),
    path('logout/', Logout, name='logout'),
    path('change_password', Change_Password, name='change_password'),
    path('view_user', view_user, name='view_user'),
    path('edit_profile/<int:pid>', edit_profile, name='edit_profile'),
    path('add_category', add_category, name='add_category'),
    path('view_category', view_category, name='view_category'),
    path('delete_category/<int:pid>', delete_category, name='delete_category'),
    path('edit_category/<int:pid>', edit_category, name='edit_category'),
    path('search_blood', search_blood, name='search_blood'),
    path('donate_blood', donate_blood, name='donate_blood'),
    path('request_blood', request_blood, name='request_blood'),
    path('donator_blood', donator_blood, name='donator_blood'),
    path('history', history, name='history'),
    path('my_order', my_order, name='my_order'),
    path('all_order', all_order, name='all_order'),
    path('change_status/<int:pid>/', change_status, name='change_status'),
    path('change_order_status/<int:pid>', change_order_status, name='change_order_status'),
    path('pay_now/<int:pid>', pay_now, name='pay_now'),
    path('delete_order/<int:pid>', delete_order, name='delete_order'),
    path('delete_user/<int:pid>', delete_user, name='delete_user'),
]
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
