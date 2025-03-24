
from rest_framework.throttling import UserRateThrottle

class CustomRateThrottle(UserRateThrottle):
    # rate = '4/day'
    scope = 'jack'    