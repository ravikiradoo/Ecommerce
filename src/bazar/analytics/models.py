from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .signals import object_viewed_signal
from .utils import get_client_ip
from django.db.models import Q
# Create your models here.
User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE)
    ip   = models.CharField(max_length=220,null=True,blank=True)
    content_type= models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id   = models.PositiveIntegerField()
    content_object =GenericForeignKey('content_type','object_id')
    created       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content_object} viewed on {self.created}"
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'

def object_viewed_signal_reciver(sender,instance,request,*args,**kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    objects_viewd = ObjectViewed.objects.create(
                        user = request.user,
                        content_type = c_type,
                        object_id    = instance.id,
                        ip = get_client_ip(request)
    )

object_viewed_signal.connect(object_viewed_signal_reciver)