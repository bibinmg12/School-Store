from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from school_app.models import Student
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Enter a valid username or password')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if not password:
            messages.info(request, 'Password field is empty')
            return redirect('register')
   
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
                
            else:
                user = User.objects.create_user(username=username,
                                                password=password, )

                user.save()
                print('user created')
            return redirect('login')
        else:
            messages.info(request, 'Password is not matching')
        return redirect('register')
        # return redirect('/')
    return render(request, 'register.html')


def student(request):
    error_message = ''
    success_message = ''
    if request.method == "POST":

        try:
            name = request.POST.get('name')
            birth_date = request.POST.get('birth_date')
            address = request.POST.get('address')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            department = request.POST.get('department')
            purpose = request.POST.get('purpose')
            course = request.POST.get('course')
            note = request.POST.get('Note') is not None
            pen = request.POST.get('pen') is not None
            paper = request.POST.get('paper') is not None

            if not name:
                error_message = 'Please enter your name.'
            elif not birth_date:
                error_message = 'Please select the date'
            elif not address:
                error_message = 'Please enter your address.'
            elif not gender:
                error_message = 'Please select your gender.'
            elif not age:
                error_message = 'Please enter your age'  
            elif not phone:
                error_message = 'Please enter your phone number.'
            elif not email:
                error_message = 'Please enter your email address.'
            elif not department:
                error_message = 'Please enter your department.'
            elif not purpose:
                error_message = 'Please select your purpose.'
            elif not course:
                error_message = 'Please select your course'
            elif not (note or pen or paper):
                error_message = 'Please select at least one material provided.'

            if error_message:
                return render(request, "st_reg.html", {'error_message':error_message})

            
            sn=Student(name=name,birth_date=birth_date,address=address,gender=gender,age=age,phone=phone,email=email,department=department,purpose=purpose,course=course,note=note,pen=pen,paper=paper)
            sn.save()
            print("Student created")
            success_message='Order Confirmed'
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
    return render(request, "st_reg.html" , {'error_message':error_message, 'success_message':success_message})



def logout(request):
    auth.logout(request)
    return redirect('/')
