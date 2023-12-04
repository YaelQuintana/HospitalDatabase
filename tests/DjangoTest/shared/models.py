from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.models import TenantManager, DomainManager

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

class Domain(DomainMixin):
    pass
