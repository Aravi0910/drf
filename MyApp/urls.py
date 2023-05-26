from django.urls import path, include, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register('cricketer', views.CricketerModelViewset)
router.register('voter', views.VoterViewset)



urlpatterns = [
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
    path('cricketerviewsets', views.CricketerViewset.as_view({'get':'list', 'get':'retrieve'})),
    path('cricketermodelviewset', views.CricketerModelViewset.as_view({'get':'list', 'get':'retrieve', 'post':'create'})),
    path('voterviewset', views.VoterViewset.as_view({'get':'list', 'get':'retrieve', 'post':'create', 'delete':'destroy'})),
    path('', include(router.urls)),
    path('trail', views.Trail.as_view(), name = 'trail'),  
    # path('user_viewset', views.UserViewset.as_view({'get':'list', 'post':'create'}), name = 'user_viewset'),  
    # JWT 
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name = 'token_refresh'),  
    # Throttling
    path('throttlingview', views.ThrottlingView.as_view(), name = 'throttlingview'),  
    # Filter
    path('filterlist', views.FilterList.as_view(), name = 'filterlist'),  
    path('cricketerfilterlist', views.CricketerFilterList.as_view(), name = 'cricketerfilterlist'),  
    
 ]
#urlpatterns = format_suffix_patterns(urlpatterns)

