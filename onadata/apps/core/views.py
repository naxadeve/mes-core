from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from .serializers import ActivityGroupSerializer, ActivitySerializer

from .models import Project, Output, ActivityGroup, Activity, Cluster, Beneficiary
from .forms import SignUpForm, ProjectForm, OutputForm, ActivityGroupForm, ActivityForm, ClusterForm, BeneficiaryForm


def logout_view(request):
    logout(request)

    return render()

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'core/index.html'


class SignInView(TemplateView):
	template_name = 'core/sign-in.html'


class SignUpView(TemplateView):
	template_name = 'core/sign-up.html'

	def signup(request):
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password')
				user = authenticate(username=username, password=raw_password)
				login(request, user)
				return redirect('core/sign-in.html')

		else:
			form = SignUpForm()
		return render(request, 'core/sign-up.html', {'form': form})


class ProjectListView(ListView):
	model = Project
	template_name = 'core/project-list.html'


class ProjectDetailView(DetailView):
	model = Project
	template_name = 'core/project-detail.html' 


class ProjectCreateView(CreateView):
	model = Project
	form_class = ProjectForm
	template_name = 'core/project-form.html'
	
	success_url = reverse_lazy('project_list')


class ProjectUpdateView(UpdateView):
	model = Project
	template_name = 'core/project-form.html'
	form_class = ProjectForm
	success_url = reverse_lazy('project_list')


class ProjectDeleteView(DeleteView):
	model = Project
	template_name = 'core/project-delete.html'
	success_url = reverse_lazy('project_list')



class OutputListView(ListView):
	model = Output
	template_name = 'core/output-list.html'


class OutputDetailView(DetailView):
	model = Output
	template_name = 'core/output-detail.html'


class OutputCreateView(CreateView):
	model = Output
	template_name = 'core/output-form.html'
	form_class = OutputForm
	success_url = reverse_lazy('output_list')


class OutputUpdateView(UpdateView):
	model = Output
	template_name = 'core/output-form.html'
	form_class = OutputForm
	success_url = reverse_lazy('output_list')


class OutputDeleteView(DeleteView):
	model = Output
	template_name = 'core/output-delete.html'
	success_url = reverse_lazy('output_list')



class ActivityGroupListVeiw(ListView):
	model = ActivityGroup
	template_name = 'core/activitygroup-list.html'



class ActivityGroupDeleteView(DeleteView):
	model = ActivityGroup
	template_name = 'core/activitygroup-delete.html'
	success_url = reverse_lazy('activitygroup_list')


class ActivityGroupCreateView(CreateView):
	model = ActivityGroup
	template_name = 'core/activitygroup-form.html'
	form_class = ActivityGroupForm
	success_url = reverse_lazy('activitygroup_list')


class ActivityGroupUpdateView(UpdateView):
	model = ActivityGroup
	template_name = 'core/activitygroup-form.html'
	form_class = ActivityGroupForm
	success_url = reverse_lazy('activitygroup_list')


class ActivityGroupDetailView(DetailView):
	model = ActivityGroup
	template_name = 'core/activitygroup-detail.html'




class ActivityListView(ListView):
	model = Activity
	template_name = 'core/activity-list.html'


class ActivityCreateView(CreateView):
	model = Activity
	template_name = 'core/activity-form.html'
	form_class = ActivityForm
	success_url = reverse_lazy('activity_list')


class ActivityDetailView(DetailView):
	model = Activity
	template_name = 'core/activity-detail.html'


class ActivityUpdateView(UpdateView):
	model = Activity
	template_name = 'core/activity-form.html'
	form_class = ActivityForm
	success_url = reverse_lazy('activity_list')


class ActivityDeleteView(DeleteView):
	model = Activity
	template_name = 'core/activity-delete.html'
	success_url = reverse_lazy('activity_list')



class ClusterListView(ListView):
	model = Cluster
	template_name = 'core/cluster-list.html'


class ClusterCreateView(CreateView):
	model = Cluster
	template_name = 'core/cluster-form.html'
	form_class = ClusterForm
	success_url = reverse_lazy('cluster_list') 


class ClusterDetailView(DetailView):
	model = Cluster
	template_name = 'core/cluster-detail.html'


class ClusterUpdateView(UpdateView):
	model = Cluster
	template_name = 'core/cluster-form.html'
	form_class = ClusterForm
	success_url = reverse_lazy('cluster_list')


class ClusterDeleteView(DeleteView):
	model = Cluster
	template_name = 'core/cluster-delete.html'
	success_url = reverse_lazy('cluster_list')


class BeneficiaryListView(ListView):
	model = Beneficiary
	template_name = 'core/beneficiary-list.html'


class BeneficiaryCreateView(CreateView):
	model = Beneficiary
	template_name = 'core/beneficiary-form.html'
	form_class = BeneficiaryForm
	success_url = reverse_lazy('beneficiary_list')


class BeneficiaryDetailView(DetailView):
	model = Beneficiary
	template_name = 'core/beneficiary-detail.html'


class BeneficiaryUpdateView(UpdateView):
	model = Beneficiary
	template_name = 'core/beneficiary-form.html'
	form_class = BeneficiaryForm
	success_url = reverse_lazy('beneficiary_list')	


class BeneficiaryDeleteView(DeleteView):
	model = Beneficiary
	template_name = 'core/beneficiary-delete.html'
	success_url = reverse_lazy('beneficiary_list')


################################################################################################################


class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class ActivityGroupViewSet(viewsets.ModelViewSet):
	queryset =  ActivityGroup.objects.all()
	serializer_class = ActivityGroupSerializer








