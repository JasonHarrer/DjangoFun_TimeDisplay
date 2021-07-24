from datetime import datetime
from pytz import timezone
from django.shortcuts import render

# Create your views here.

def index(request):
    context = { 'currtime': datetime.now(timezone('America/Chicago')).strftime('%-I:%M%p %Z (%z)'),
                'currdate': datetime.now(timezone('America/Chicago')).strftime('%b %d, %Y')
              }
    return render(request, 'index.html', context)
