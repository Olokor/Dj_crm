from django.contrib import admin

import leads
from leads.models import Agent, Lead

# Register your models here.
admin.site.register(Lead)
admin.site.register(Agent)