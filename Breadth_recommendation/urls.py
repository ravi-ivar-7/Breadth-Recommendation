from django.contrib import admin
from django.urls import path,include
#added  to change admin name,title,etc.
admin.site.site_header = "BR"
admin.site.site_title = "BR"
admin.site.index_title = "BR"
#for media and static files purpose
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# for account related 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    # path('accounts/', include('allauth.socialaccount.urls')),
    path('',include('BR.urls')),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'), #login required to change password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]
urlpatterns+=staticfiles_urlpatterns()

#during development only
if settings.DEBUG:
    urlpatterns=urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

