from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .forms import BlogPostModelForm
from .models import BlogPost


# Crete Retrive Update Delete CRUD 

def blog_post_list_view(request):
	# list out objects
	# qs = BlogPost.objects.all() # queryset -> list of python objects
	qs = BlogPost.objects.all().published()
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = (my_qs | qs).distinct()
		
	template_name  =  'blog/list.html'
	context = {"object_list": qs}
	return render(request, template_name, context)

@staff_member_required
# @login_required
def blog_post_create_view(request):
	# create objects
	form = BlogPostModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit = False)
		obj.user = request.user
		obj.save()
		form = BlogPostModelForm()

	template_name  =  'form.html'
	context = {"form": form}
	return render(request, template_name, context)


def blog_post_detail_view(request, slug):
	# 1 object -> detail view
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name  =  'blog/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, instance= obj)
	if form.is_valid():
		form.save()

	template_name  =  'form.html'
	context = {"form": form, "title": f"Update {obj.title}"}
	return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name  =  'blog/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/blog")
	context = {"object": obj}
	return render(request, template_name, context)







def blog_post_detail_page(request, slug):
	# try:
	# 	obj = BlogPost.objects.get(id = post_id)
	# except BlogPost.DoesNotExist:
	# 	raise Http404
	# except ValueError:
	# 	raise Http404

	# queryset = BlogPost.objects.filter(slug= slug)
	# if queryset.count() == 0:
	# 	raise Http404
	# obj  = queryset.first()
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name  =  'blog/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)
