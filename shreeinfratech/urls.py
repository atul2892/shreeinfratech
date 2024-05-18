from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('subscribtion/',views.subscribtion),
    path('about/',views.about),
    path('about-ravi/',views.aboutRavi),
    path('organisation/',views.organisation),
    path('executive/',views.executive),
    path('project/',views.project),
    path('commitment/',views.commitment),
    # path('enquiry/',views.enquiry),
    path('contact/',views.contact),
    # path('website/',views.website),
    # path('graphic-designing/',views.graphicDesigning),
    # path('digital-marketing/',views.digitalMarketing),
    # path('seo/',views.seo),
    # path('paid-advertising/',views.paidAdvertising),
    # path('digital-pr/',views.digitalPr),
    # path('social-media/',views.socialMedia),
    # path('email-marketing/',views.emailMarketing),
]
