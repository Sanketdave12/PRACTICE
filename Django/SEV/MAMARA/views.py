from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from MAMARA.models  import notice, Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'base.html')

class NoticeListView(ListView):
    model = notice
    def get_queryset(self):
        if self.request.user.is_superuser:
            return notice.objects.order_by("-id")
        else:
            return notice.objects.filter(Q(branch=self.request.user.profile.branch) | Q(branch__isnull = True)).order_by("-id")


@method_decorator(login_required,name='dispatch')
class NoticeDetailView(DetailView):
    model = notice