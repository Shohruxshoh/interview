from django.urls import path
# from django.contrib.auth.views import LogoutView
from .views import LoginView, CustomerListView, CustomerCreateView, CustomerUpdateView, ExistingPartyListView, \
    ExistingPartyCreateView, ExistingPartyUpdateView, ChineseListView, ChineseCreateView, ChineseDeleteView, \
    UzbekListView, UzbekCreateView, UzbekDeleteView

urlpatterns = [
    path('login/', LoginView.as_view()),
    # path('logout/', LogoutView.as_view()),

    path('customers/', CustomerListView.as_view()),
    path('customer/create', CustomerCreateView.as_view()),
    path('customer/update/<int:pk>', CustomerUpdateView.as_view()),

    path('existing-parties/', ExistingPartyListView.as_view()),
    path('existing-party/create', ExistingPartyCreateView.as_view()),
    path('existing-party/update/<int:pk>', ExistingPartyUpdateView.as_view()),

    path('chineses/', ChineseListView.as_view()),
    path('chineses/create', ChineseCreateView.as_view()),
    path('chineses/delete/<int:pk>', ChineseDeleteView.as_view()),

    path('uzbek/', UzbekListView.as_view()),
    path('uzbek/create', UzbekCreateView.as_view()),
    path('uzbek/delete/<int:pk>', UzbekDeleteView.as_view()),

]
