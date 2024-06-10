# myapp/views.py
import json
from queue import Queue
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Movie, Comment, Watchlist, Profile, Actor, MovieActor, Rank
from .forms import UserRegistrationForm, CommentForm, RankForm
from django.contrib import messages
from django.db import IntegrityError

def home(request):
    movies = Movie.objects.all()
    return render(request, 'myapp/home.html', {'movies': movies})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['email'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
                Profile.objects.create(
                    user=user,
                    country=form.cleaned_data['country'],
                    city=form.cleaned_data['city']
                )
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Profile already exists for this user.')
                return render(request, 'myapp/register.html', {'form': form})
        else:
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'myapp/login.html', {'error': 'Invalid email or password'})

        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'myapp/login.html', {'error': 'Account is inactive'})
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid email or password'})

    return render(request, 'myapp/login.html')

def actors_list(request):
    actors = Actor.objects.all()
    return render(request, 'myapp/actors_list.html', {'actors': actors})

def actor_detail(request, id):
    actor = get_object_or_404(Actor, id=id)
    return render(request, 'myapp/actor_detail.html', {'actor': actor})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    
    # Increment the view count
    movie.views += 1
    movie.save()

    # Update popularity based on views
    movie.popularity = movie.views
    movie.save()

    movie_actors = MovieActor.objects.filter(movie=movie)
    
    # Calculate popularity score
    popularity_score = movie.rating + (movie.popularity * 0.01)
    
    # Calculate popularity rank
    all_movies = Movie.objects.all()
    ranked_movies = sorted(all_movies, key=lambda m: m.rating + (m.popularity * 0.1), reverse=True)
    popularity_rank = ranked_movies.index(movie) + 1

    # Handle comment form
    if request.method == 'POST' and 'comment_form' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
            return redirect('movie_detail', id=movie.id)
    else:
        comment_form = CommentForm()

    # Handle rank form
    if request.method == 'POST' and 'rank_form' in request.POST:
        rank_form = RankForm(request.POST)
        if rank_form.is_valid():
            rank, created = Rank.objects.update_or_create(
                user=request.user,
                movie=movie,
                defaults={'score': rank_form.cleaned_data['score']}
            )
            return redirect('movie_detail', id=movie.id)
    else:
        rank_form = RankForm()

    # Fetch comments and ranks
    comments = Comment.objects.filter(movie=movie).order_by('-timestamp')
    ranks = Rank.objects.filter(movie=movie).order_by('-timestamp')

    context = {
        'movie': movie,
        'movie_actors': movie_actors,
        'popularity_score': popularity_score,
        'popularity_rank': popularity_rank,
        'comment_form': comment_form,
        'rank_form': rank_form,
        'comments': comments,
        'ranks': ranks,
    }
    return render(request, 'myapp/detail.html', context)

def calculate_popularity_rank(movie):
    all_movies = Movie.objects.all()
    ranked_movies = sorted(all_movies, key=lambda m: (m.rating * 10) + (m.popularity * 0.5), reverse=True)
    rank = ranked_movies.index(movie) + 1
    return rank

@login_required
def comment(request, movie_id):
    if request.method == 'POST':
        body = request.POST['comment']
        movie = get_object_or_404(Movie, id=movie_id)
        Comment.objects.create(body=body, user=request.user, movie=movie)
        return redirect('movie_detail', id=movie_id)

@login_required
def watchlist(request):
    movies = Movie.objects.filter(watchlist__user=request.user)
    return render(request, 'myapp/watchlist.html', {'movies': movies})

@csrf_exempt
@login_required
def add_to_watchlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            movie_id = data.get('movie_id')
            movie = get_object_or_404(Movie, id=movie_id)
            Watchlist.objects.get_or_create(user=request.user, movie=movie)
            return JsonResponse({'status': 'success'})
        except Movie.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Movie not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def remove_from_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    Watchlist.objects.filter(user=request.user, movie=movie).delete()
    return redirect('watchlist')

def search(request):
    query = request.GET.get('query', '')
    movie_results = Movie.objects.filter(title__icontains=query)
    actor_results = Actor.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'movie_results': movie_results,
        'actor_results': actor_results
    }

    return render(request, 'myapp/search.html', context)

def search_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        movies = Movie.objects.filter(title__icontains=query).distinct()[:5]
        actors = Actor.objects.filter(name__icontains=query).distinct()[:5]

        movie_results = [{'id': movie.id, 'title': movie.title} for movie in movies]
        actor_results = [{'id': actor.id, 'name': actor.name} for actor in actors]

        results = {
            'movies': movie_results,
            'actors': actor_results
        }
        return JsonResponse({'results': results})

    return JsonResponse({'results': {'movies': [], 'actors': []}})
