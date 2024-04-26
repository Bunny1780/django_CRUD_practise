# 頁面模組
from django.shortcuts import render
from random import sample
def main(request):
    return render(request, "pages/index.html")

def about_us(request):
    numbers = sorted(sample(range(1,50), 6))
    return render(request, "pages/about.html",{"lottery_numbers":numbers})
