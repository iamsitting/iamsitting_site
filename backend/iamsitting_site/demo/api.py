from demo.api_views import PatientViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('patients', PatientViewset)
