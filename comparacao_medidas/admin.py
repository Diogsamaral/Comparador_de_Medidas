from django.contrib import admin
from .models import TabelaMedidas, TabelaMedidasCalca, TabelaMedidasJaqueta

admin.site.register(TabelaMedidas)
admin.site.register(TabelaMedidasJaqueta)
admin.site.register(TabelaMedidasCalca)


