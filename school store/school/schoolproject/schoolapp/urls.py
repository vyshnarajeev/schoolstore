from django .urls import path
from .import views
app_name='schoolapp'

urlpatterns=[
    path('',views.allProCat,name="allProCat"),
    path('<slug:c_slug>/', views.allProCat, name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name="ProdutCategoryDetail"),
    path('cse',views.cse,name="cse"),
    path('ce',views.ce,name="ce"),
    path('me',views.me,name="me"),
    path('ece',views.ece,name="ece"),
    path('eee',views.eee,name="eee"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('form', views.form, name="form"),
    path('forms', views.forms, name="forms"),

]