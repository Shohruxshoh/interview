from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    GenericAPIView
from rest_framework.views import APIView

from .models import Customer, ExistingParty, Chinese, Uzbek
from .paginations import StandardResultsSetPagination
from .serializers import CustomerSerializer, ExistingPartySerializer, ChineseSerializer, \
    ChineseCreateSerializer, UzbekSerializer, UzbekCreateSerializer, LoginSerializer
from rest_framework import status
# from django.shortcuts import redirect

"""  Login   """


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            login = serializer.validated_data['login']
            password = serializer.validated_data['password']
            user = authenticate(username=login, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LogoutView(GenericAPIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         print(logout(self.request))
#         content = {
#             'message': "Logout",  # `django.contrib.auth.User` instance.
#             'success': True
#         }
#         return Response(content)


"""  End Login   """

""" Foydalanuvchilarni ro'yxatga olish """


class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]


class CustomerCreateView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


class CustomerUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


"""  End Foydalanuvchilarni ro'yxatga olish   """

"""  Mavjud partiyalar """


class ExistingPartyListView(ListAPIView):
    queryset = ExistingParty.objects.all()
    serializer_class = ExistingPartySerializer
    permission_classes = [IsAdminUser]
    pagination_class = StandardResultsSetPagination


class ExistingPartyCreateView(CreateAPIView):
    queryset = ExistingParty.objects.all()
    serializer_class = ExistingPartySerializer
    permission_classes = [IsAdminUser]


class ExistingPartyUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = ExistingParty.objects.all()
    serializer_class = ExistingPartySerializer
    permission_classes = [IsAdminUser]


"""  End Mavjud partiyalar """

"""  Xitoy baza    """


class ChineseListView(ListAPIView):
    queryset = Chinese.objects.all().select_related("customer_key")
    serializer_class = ChineseSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['party']


class ChineseCreateView(CreateAPIView):
    queryset = Chinese.objects.all()
    serializer_class = ChineseCreateSerializer
    permission_classes = [IsAdminUser]


class ChineseDeleteView(RetrieveDestroyAPIView):
    queryset = Chinese.objects.all().select_related("customer_key")
    serializer_class = ChineseSerializer
    permission_classes = [IsAdminUser]


"""  End Xitoy baza    """

"""  O'zbek baza    """


class UzbekListView(ListAPIView):
    queryset = Uzbek.objects.all().select_related("customer_key", "track_code")
    serializer_class = UzbekSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['party']


class UzbekCreateView(CreateAPIView):
    queryset = Uzbek.objects.all()
    serializer_class = UzbekCreateSerializer
    permission_classes = [IsAdminUser]


class UzbekDeleteView(RetrieveDestroyAPIView):
    queryset = Uzbek.objects.all().select_related("customer_key", "track_code")
    serializer_class = UzbekSerializer
    permission_classes = [IsAdminUser]


"""  End O'zbek baza    """
