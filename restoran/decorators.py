from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from crm_food.models import Meal


def is_anonymous(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


def is_chef(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        if not request.user.user_type == 2:
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


def is_administrator(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        if not request.user.user_type == 1:
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


def can_create_food(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        if not (request.user.user_type == 2 or request.user.user_type == 1):
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


def can_update_product(func):
    def wrapper(request, pk, *args, **kwargs):
        # user = request.user
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        food = get_object_or_404(Meal, pk=pk)
        if not (request.user.user_type == 1 or request.user.user_type == 2):
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, pk, *args, **kwargs)
    return wrapper


def can_delete_product(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        if not (request.user.user_type == 2 or request.user.user_type == 1):
            if request.is_ajax():
                return JsonResponse({
                    'error': True,
                    'errors': ['You don\'t have permission to perfom the process!'],
                    'redirect_url': settings.FORBIDDEN_REDIRECT_URL
                })
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper


def can_take_order(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.REDIRECT_URL)
        if request.user.user_type == 3:
            return redirect(settings.FORBIDDEN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return wrapper
