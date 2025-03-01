from django.shortcuts import render, get_object_or_404, redirect
from .models import Attraction, Comment, Like, Reply
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Comment
import json

@login_required
@require_POST
def edit_comment(request, comment_id):
    try:
        data = json.loads(request.body)
        content = data.get('content')
        if not content:
            return JsonResponse({'success': False, 'error': 'Content cannot be empty.'})

        comment = Comment.objects.get(id=comment_id, user=request.user)
        comment.content = content
        comment.save()
        return JsonResponse({'success': True})
    except Comment.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Comment not found or you do not have permission to edit this comment.'})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON data.'})

@login_required
@require_POST
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id, user=request.user)
        comment.delete()
        return JsonResponse({'success': True})
    except Comment.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Comment not found or you do not have permission to delete this comment.'})
# Home page view
def index(request):
    attractions = Attraction.objects.all()
    return render(request, 'index.html', {'attractions': attractions})

# Attraction detail view
def attraction_detail(request, id):
    attraction = get_object_or_404(Attraction, id=id)
    comments = attraction.comments.all()
    user_liked = False
    if request.user.is_authenticated:
        user_liked = attraction.likes.filter(user=request.user).exists()
    if request.method == 'POST' and request.user.is_authenticated:

        
        # Handle comment
        content = request.POST.get('content')
        if content:  # Ensure content is not None
            comment = Comment.objects.create(user=request.user, attraction=attraction, content=content)
            return redirect('attraction_detail', id=id)
        else:
            messages.error(request, "Comment content cannot be empty.")
    return render(request, 'attraction_detail.html', {
            'attraction': attraction,
            'comments': comments,
            'user_liked': user_liked
        })
# Like/unlike attraction view

@login_required
def like_attraction(request, id):
    attraction = get_object_or_404(Attraction, id=id)
    if request.method == 'POST':
        like, created = Like.objects.get_or_create(user=request.user, attraction=attraction)
        if not created:
            like.delete()
            liked = False
        else:
            liked = True
        return JsonResponse({'liked': liked, 'likes_count': attraction.likes.count()})
    return JsonResponse({'error': 'Invalid request method.'})

@login_required
def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            reply = Reply.objects.create(user=request.user, comment=comment, content=content)
            return JsonResponse({'success': True, 'reply': reply.content, 'user': reply.user.username, 'created_at': reply.created_at})
    return JsonResponse({'error': 'Invalid request method or empty content.'})

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                # messages.success(request, f'Welcome back, {user.username}! 🎉')
                return redirect('index')  # Or whatever page you want to redirect to
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')

        else:
            messages.error(request, 'Invalid login details. Check your username and password.')
            return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    # Log the user out first
    logout(request)

    # Add a logout success message
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')


# User registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    

    return render(request, 'register.html', {'form': form})


@login_required
def comment_attraction(request, id):
    attraction = get_object_or_404(Attraction, id=id)
    if request.method == 'POST':
        # Check if the user has already commented on this attraction
        if Comment.objects.filter(user=request.user, attraction=attraction).exists():
            return JsonResponse({'already_commented': True})
        else:
            content = request.POST.get('content')
            if content:
                Comment.objects.create(user=request.user, attraction=attraction, content=content)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': 'Comment content cannot be empty.'})
    return JsonResponse({'error': 'Invalid request method.'})


def search_attractions(request):
    query = request.GET.get('q')
    attractions = Attraction.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'attractions': attractions, 'query': query})

