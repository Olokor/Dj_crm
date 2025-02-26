from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete, Lead_List, LandingPage, Lead_Detail, \
    Lead_Create, Lead_update

app_name = "leads"

urlpatterns = [
    path("", Lead_List.as_view(), name="home"),
    path("landing/", LandingPage.as_view(), name="landing"),
    path("<int:pk>/", Lead_Detail.as_view(), name="lead_detail"),
path("<int:pk>/update", Lead_update.as_view(), name="lead_update"),
path("<int:pk>/delete", lead_delete, name="lead_delete"),
    path("create/", Lead_Create.as_view(), name="lead_create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)