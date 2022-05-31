from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .transaction_models import CommonFieldMixinModel
fs = FileSystemStorage(location='/media/fs')

#from .storages import MyLocalStorage, MyRemoteStorage
#def select_storage():
#    return MyLocalStorage() if settings.DEBUG else MyRemoteStorage()


class UploadTbl(CommonFieldMixinModel):
    file =  models.FileField(upload_to='media/files', blank=True, null=True)
    photo = models.ImageField(upload_to='media/images', blank=True, null=True)
    id_prof = models.ImageField(storage=fs, blank=True, null=True)

    
