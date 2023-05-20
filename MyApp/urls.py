from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register('cricketer', views.CricketerViewsets)



urlpatterns = [
    path('', include(router.urls)),
    path('stud_list',views.stud_list, name='stud_list'),
    path('stud_get/<str:pk>',views.stud_get, name='stud_get'),
    path('stud_create', views.stud_create, name='stud_create'),
    path('stud_update/<str:pk>', views.stud_update, name='stud_update'),
    path('stud_delete/<str:pk>', views.stud_delete, name='stud_delete'),
    path('stud_details/<str:pk>', views.stud_details,name='stud_details'),
    path('student_cv', views.student_cv,name='student_cv'),
    path('studentlist', views.StudentList.as_view()),
    path('student/<str:pk>', views.Student.as_view()),
    path('studmixinlist', views.StudMixinList.as_view()), 
    path('studmixindetails/<str:pk>', views.StudMixinDetails.as_view()),    
    path('studgenericlist', views.StudGenericList.as_view()),    
    path('studgenericdetails/<str:pk>', views.StudGenericDetails.as_view()), 
    path('cricketerlist', views.CricketerList.as_view()),   
    path('cricketerview', views.CricketerView.as_view()),   
    path('cricketerfilters/<str:pk>', views.CricketerFilters.as_view()),   
    path('votingMixinlist', views.VotingMixinList.as_view()),   
    path('cricketerviewsets', views.CricketerViewsets.as_view({'get':'list'})),   
]
urlpatterns = format_suffix_patterns(urlpatterns)

