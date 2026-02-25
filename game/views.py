from django.shortcuts import render


def home(request):
    return render(request, 'game/home.html')

def ballotBlitz(request):
    return render(request, 'game/ballot_blitz.html')

def steadyHand(request):
    return render(request, 'game/steady_hand.html')

