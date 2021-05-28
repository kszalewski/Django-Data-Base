from django.contrib import admin

from .models import Stanowiska
from .models import Pracownicy
from .models import Projekty
from .models import Zatrudnienie
from .models import Urlopy
from .models import Rekrutacja
from .models import Szkolenia
from .models import Premia

admin.site.register(Stanowiska)
admin.site.register(Pracownicy)
admin.site.register(Projekty)
admin.site.register(Zatrudnienie)
admin.site.register(Urlopy)
admin.site.register(Rekrutacja)
admin.site.register(Szkolenia)
admin.site.register(Premia)