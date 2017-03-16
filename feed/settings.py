from django.contrib.contenttypes.models import ContentType

SHOWN_EVENTS = ['post', 'comment', 'friendship']
CTYPES = [ContentType.objects.get(model=event) for event in SHOWN_EVENTS]
