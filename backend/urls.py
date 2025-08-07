from django.contrib import admin
from django.urls import path, include

# Criação dos endpoints para serem usados na api, é realizado importação das funções e as lógicas pelo views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
