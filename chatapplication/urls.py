from django.urls import path
from chatapplication import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),

    # login-section
    # path("auth/login/", LoginView.as_view
    #      (template_name="chatapplication/templates/login.html"), name="login-user"),
    # path("auth/login/", LoginView.as_view(template_name="chatapplication/templates/login.html"), name="login-user"),
    path('login/',LoginView.as_view(template_name='login.html'), name='login-user'),
    path("logout/", LogoutView.as_view(), name="logout-user"),
]