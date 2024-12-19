from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # แสดงหน้าแรก

def next_page(request):
    return render(request, 'next.html')  # แสดงหน้าถัดไป
