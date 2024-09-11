from django.shortcuts import render, redirect


def main(request):
    context = {}
    return render(request, 'index.html', context)