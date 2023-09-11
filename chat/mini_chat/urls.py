from django.urls import include, path
from rest_framework import routers
from mini_chat import views

router = routers.DefaultRouter()
router.register(r'users', views.UserList)
router.register(r'conversations', views.ConversationList)
router.register(r'privatemessages', views.PrivateMessageList)
router.register(r'chatrooms', views.ChatRoomList)
router.register(r'chatroommessages', views.ChatRoomMessageList)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index)
    
]
