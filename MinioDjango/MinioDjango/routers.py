from FileManagement.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register("image", ImageView)
