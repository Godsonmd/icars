from django.shortcuts import render,redirect,get_object_or_404
from .models import *
import smtplib
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

INDIAN_STATES = {
    "Andhra Pradesh": (15.9129, 79.7400),
    "Arunachal Pradesh": (28.2180, 94.7278),
    "Assam": (26.2006, 92.9376),
    "Bihar": (25.0961, 85.3131),
    "Chhattisgarh": (21.2787, 81.8661),
    "Goa": (15.2993, 74.1240),
    "Gujarat": (22.2587, 71.1924),
    "Haryana": (29.0588, 76.0856),
    "Himachal Pradesh": (31.1048, 77.1734),
    "Jharkhand": (23.6102, 85.2799),
    "Karnataka": (15.3173, 75.7139),
    "Kerala": (10.8505, 76.2711),
    "Madhya Pradesh": (22.9734, 78.6569),
    "Maharashtra": (19.6633, 75.3003),
    "Manipur": (24.6637, 93.9063),
    "Meghalaya": (25.4670, 91.3662),
    "Mizoram": (23.1645, 92.9376),
    "Nagaland": (26.1584, 94.5624),
    "Odisha": (20.9517, 85.0985),
    "Punjab": (30.7333, 76.7800),
    "Rajasthan": (27.0238, 74.2176),
    "Sikkim": (27.5330, 88.5122),
    "Tamil Nadu": (11.1271, 78.6569),
    "Telangana": (17.0738, 78.6556),
    "Tripura": (23.9400, 91.9882),
    "Uttar Pradesh": (26.8467, 80.9462),
    "Uttarakhand": (30.0668, 79.0193),
    "West Bengal": (22.9868, 87.8550),
}

def out(request):
    if 'logined' in request.session:
        return redirect('profile')
    else:
        return redirect('home')

def tc(request):
    return render(request,'tc.html')
def home(request):
    if 'logined' in request.session:
        del request.session['logined']
    if 'PC' in request.session:
        del request.session['PC']
    if request.method == "POST":
        handle = request.POST.get('handle')
        email = request.POST.get('email')
        password=request.POST.get('password')
        request.session['handle'] = handle
        request.session['email'] = email
        if handle=="customer":
            bans=banc.objects.all()
            for i in bans:
                if i.email == email:
                    alert="Sorry this account was banned !"
                    return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
            if c_reg.objects.filter(email=email).exists() and c_reg.objects.filter(password=password).exists():
                alert="Successfully logined as customer"
                request.session['logined']="customer"
                return HttpResponse("<script>alert('"+alert+"'); window.location.href='/profile';</script>")
            else:
                alert="Login failed"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
        elif handle=="admin":
            if a_reg.objects.filter(email=email).exists() and a_reg.objects.filter(password=password).exists():
                alert="Successfully logined as admin"
                request.session['logined']="admin"
                return HttpResponse("<script>alert('"+alert+"'); window.location.href='/profile';</script>")
            else:
                alert="Login failed"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
        elif handle=="client":
            bans=banr.objects.all()
            for i in bans:
                if i.email == email:
                    alert="Sorry this account was banned !"
                    return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
            if r_reg.objects.filter(email=email).exists() and r_reg.objects.filter(password=password).exists():
                alert="Successfully logined as client"
                request.session['logined']="client"
                return HttpResponse("<script>alert('"+alert+"'); window.location.href='/profile';</script>")
            else:
                alert="Login failed"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
        else:
            alert="Who r u ?"
            return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
    else:
        return render(request,'home.html')
def login(request):
    if 'logined' in request.session:
        del request.session['logined']
    if 'PC' in request.session:
        del request.session['PC']
    if request.method == "POST":
        handle = request.POST.get('handle')
        email = request.POST.get('email')
        password=request.POST.get('password')
        request.session['handle'] = handle
        request.session['email'] = email
        if handle=="customer":
            bans=banc.objects.all()
            for i in bans:
                if i.email == email:
                    alert="Sorry this account was banned !"
                    return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
            if c_reg.objects.filter(email=email).exists() and c_reg.objects.filter(password=password).exists():
                alert="Successfully logined as customer"
                request.session['logined']="customer"
                return HttpResponse("<script>alert('"+alert+"'); window.location.href='/profile';</script>")
            else:
                alert="Login failed"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
        elif handle=="admin":
            if a_reg.objects.filter(email=email).exists() and a_reg.objects.filter(password=password).exists():
                alert="Successfully logined as admin"
                request.session['logined']="admin"
                return HttpResponse("<script>alert('"+alert+"'); window.location.href='/profile';</script>")
            else:
                alert="Login failed"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
        elif handle=="client":
            bans=banr.objects.all()
            for i in bans:
                if i.email == email:
                    alert="Sorry this account was banned !"
                    return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
            if r_reg.objects.filter(email=email).exists() and r_reg.objects.filter(password=password).exists():
                alert="Successfully logined as client"
                request.session['logined']="client"
                return HttpResponse("<script>alert('"+alert+"'); window.location.href='/profile';</script>")
            else:
                alert="Login failed"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
        else:
            alert="Who r u ?"
            return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
    else:
        return render(request,'login.html')
    

from django.utils import timezone
def profile(request):
     if 'PC' in request.session:
        del request.session['PC']
     email=request.session['email']
     new_trainer=None
     if request.session.get('handle') == 'customer':
        user=c_reg.objects.filter(email=email).first()
        trainer_id=user.id
        new_trainer=get_object_or_404(c_reg, id=trainer_id)
     elif request.session.get('handle') == 'client':
        user=r_reg.objects.filter(email=email).first()
        trainer_id=user.id
        new_trainer=get_object_or_404(r_reg, id=trainer_id)
     else:
        user=a_reg.objects.filter(email=email).first()
        trainer_id=user.id
        new_trainer=get_object_or_404(a_reg, id=trainer_id)
     if request.method == 'POST':
        role=request.POST.get('role')
        if role=="profile":
            new_trainer.email = request.POST.get('email')
            new_trainer.name = request.POST.get('name')
            if 'dob' in request.POST:
                new_trainer.dob = request.POST.get('dob')
            if 'phone' in request.POST:            
                new_trainer.phone = request.POST.get('phone')
            if 'drive_l_f' in request.FILES:
                new_trainer.drive_l_f = request.FILES['drive_l_f']
            if 'drive_l_b' in request.FILES:
                new_trainer.drive_l_b = request.FILES['drive_l_b']
            if 'dp' in request.FILES:
                new_trainer.dp = request.FILES['dp']
            new_trainer.save()
            
        if role=="BorR":
            BorR=request.POST.get('BorR')
            request.session['PC']="profile_completed"
            request.session['state']=request.POST.get('state','Kerala')
            return redirect(BorR)
     if 'logined' in request.session:
        logined=request.session['logined']
        now = timezone.now()
        expired_bookingsc = booked.objects.filter(dropdown__lt=now)
        expired_bookingsc.delete()
        expired_bookingst = taxibooking.objects.filter(pickup__lt=now)
        expired_bookingst.delete()
        expired_bookingss = subcription.objects.filter(closedown__lt=now)
        expired_bookingss.delete()
        bookings=booked.objects.all()
        taxies=taxibooking.objects.all()
        subss=subcription.objects.all()
        bookingsc=[]
        bookingst=[]
        bookingss=[]

        if logined=="client":
            
            for booking in bookings:
                if booking.car.owner_d:
                    if new_trainer.id == booking.car.owner_d.id:
                        bookingsc.append(booking)
        elif logined=="customer":
            
            for booking in bookings:
                    if new_trainer.id == booking.person.id:
                        bookingsc.append(booking)
            for booking in taxies:
                    if new_trainer.id == booking.person.id:
                        bookingst.append(booking)
            for booking in subss:
                    if new_trainer.id == booking.person.id:
                        bookingss.append(booking)
        else:
            
            for booking in bookings:
                if booking.car.owner_d:
                    print(booking)
                else:
                    bookingsc.append(booking)
            for booking in taxies:
                        bookingst.append(booking)
            for booking in subss:
                    bookingss.append(booking)

        return render(request,'profile.html',{'user':new_trainer,'profile':logined,'bookings':bookingsc,'taxies':bookingst,'subss':bookingss})
     else:
        alert="Login plzz"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
     



from django.utils import timezone
from django.http import HttpResponseBadRequest


def cancelc(request,bookid):
    carbooking=booked.objects.filter(id=bookid).first()
    carbooking.delete()
    return redirect('profile')
def cancelt(request,bookid):
    tbooking=taxibooking.objects.filter(id=bookid).first()
    tbooking.delete()
    return redirect('profile')
def delete(request,carid):
    carbooking=car.objects.filter(id=carid).first()
    carbooking.delete()
    return redirect('Mycars')
def edit(request,carid):
    carbooking=car.objects.filter(id=carid).first()
    logined=request.session['logined']
    if request.method =="POST":
        if logined=="client":
            carbooking.owner=request.POST.get("owner")
        carbooking.campany=request.POST.get('companyname')
        carbooking.carname=request.POST.get('carname')
        carbooking.noplate=request.POST.get('noplate')
        carbooking.seater=request.POST.get('seater')
        carbooking.gear=request.POST.get('gear')
        carbooking.fuel=request.POST.get('fuel')
        carbooking.rate=request.POST.get('rate')
        carbooking.kms=request.POST.get('kms')
        if 'car_f_photo' in request.FILES:
            carbooking.car_f_photo=request.FILES['car_f_photo']
        carbooking.save()
    return render(request,'editcar.html',{'car':carbooking,'profile':logined})  
def confirmRent(request,carid):
    carid=car.objects.get(id=carid)
    email=request.session['email']
    person=c_reg.objects.filter(email=email).first()
    booking=request.session['booking']
    pickup=booking['pickup']
    dropdown=booking['dropdown']
    pickupt = timezone.datetime.fromisoformat(pickup)
    dropdownt = timezone.datetime.fromisoformat(dropdown)
    carbook=booked(car=carid,person=person,pickup=pickupt,dropdown=dropdownt,pickupl=booking['pickupl'],dropdownl=booking['pickupl'])
    carbook.save()
    return redirect('profile')
def showcars(request):
    if 'booking' in request.session:
        booking=request.session['booking']
        state=request.session['state']
        cars=car.objects.filter(state=state)
        cars=cars.order_by('rate')
        return render(request,'showcars.html',{'cars':cars,'state':state,'pickupl':booking['pickupl'],'pickup':booking['pickup'],'dropdown':booking['dropdown']})
    else:
        alert="Plzz enter your renting details !"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/car-booking';</script>")
def carBook(request):
    if 'PC' in request.session:
        if 'booking' in request.session:
            del request.session['booking']
        state=request.session['state']
        if request.method == 'POST':
            pickupl=request.POST.get('pickupl')
            lat=request.POST.get('lat')
            long=request.POST.get('long')
            if pickupl=="YourL":
                lat=INDIAN_STATES[state][0]
                long=INDIAN_STATES[state][1]
            pickupl=f"https://www.google.com/maps?q={lat},{long}"
            pickup = request.POST.get('pickup')
            dropdown = request.POST.get('dropdown')
            try:               
                booking={
                    'pickupl':pickupl,
                    'pickup':pickup,
                    'dropdown':dropdown,
                }
                request.session['booking']=booking

                return redirect('showcars')  # Redirect to a success page
            except ValueError:
                return HttpResponseBadRequest("Invalid date format. Please use the correct format.")

        return render(request,'car.html',{'state':state})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
    

def taxiBook(request):
    if 'PC' in request.session:
        state=request.session['state']
        email=request.session['email']
        if request.method == 'POST':
            pickupl=request.POST.get('pickupl')
            lat=request.POST.get('lat')
            long=request.POST.get('long')
            
            if pickupl=="YourL":
                lat=INDIAN_STATES[state][0]
                long=INDIAN_STATES[state][1]
            pickupl=f"https://www.google.com/maps?q={lat},{long}"            
            pickup = timezone.datetime.fromisoformat(request.POST.get('pickup'))
            noP = request.POST.get('noP')
            user=c_reg.objects.filter(email=email).first()
            tbook=taxibooking(pickup=pickup,person=user,pickupl=pickupl,noP=noP)
            tbook.save()
            return redirect('profile')
        return render(request,'taxi.html',{'state':state})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
def Rcar(request):
    if 'PC' in request.session:
        logined=request.session['logined']
        state=request.session['state']
        if request.method == 'POST':
            owner=request.POST.get('owner')
            companyname=request.POST.get('companyname')
            carname=request.POST.get('carname')
            noplate=request.POST.get('noplate')
            seater=request.POST.get('seater') 
            gear=request.POST.get('gear')
            fuel=request.POST.get('fuel')
            rate=request.POST.get('rate')
            kms=request.POST.get('kms')
            if 'car_f_photo' in request.FILES:
                car_f_photo=request.FILES['car_f_photo']
            if logined=="admin":
                carD=car(owner=owner,campany=companyname,carname=carname,noplate=noplate,seater=seater,gear=gear,fuel=fuel,rate=rate,kms=kms,state=state,car_f_photo=car_f_photo)
                carD.save()
            else:
                email=request.session['email']
                renter=r_reg.objects.filter(email=email).first()
                carD=car(owner=owner,owner_d=renter,campany=companyname,carname=carname,noplate=noplate,seater=seater,gear=gear,fuel=fuel,rate=rate,kms=kms,state=state,car_f_photo=car_f_photo)
                carD.save()
            alert=carname+" added to cars list"
            return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
        return render(request,'Rcar.html',{'state':state,'profile':logined})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
def CD(request):
    if 'PC' in request.session:
        state=request.session['state']
        c=c_reg.objects.all()
        return render(request,'CD.html',{'state':state,'customers':c})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
def ClD(request):
    if 'PC' in request.session:
        state=request.session['state']
        c=r_reg.objects.all()
        return render(request,'ClD.html',{'state':state,'customers':c})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
def Mycars(request):
    if 'PC' in request.session:
        state=request.session['state']
        logined=request.session['logined']
        email=request.session['email']
        cars=[]
        cc=car.objects.filter(state=state)
        if logined=='admin':
            for c in cc:
                if c.owner_d:
                    print("Hacking...")
                else:
                    cars.append(c)
        else:
            user=r_reg.objects.filter(email=email).first()
            for c in cc:
                if c.owner_d:
                    if user.id == c.owner_d.id:
                        cars.append(c)

        return render(request,'Mycars.html',{'state':state,'cars':cars})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")

def register(request):
    if request.method == "POST":
        handle = request.POST.get('handle')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password=request.POST.get('password')
        if handle=="customer":
            bans=banc.objects.all()
            for i in bans:
                if i.email == email:
                    alert="Sorry this account was banned !"
                    return HttpResponse("<script>alert('"+alert+"');window.location.href='/register';</script>")
            if c_reg.objects.filter(email=email).exists():
                alert="This email is already exists"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/register';</script>")
            else:
                user=c_reg(name=name,email=email,password=password)   
                user.save()             
                alert="Successfully Registered as Customer! Login Now"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
        elif handle=="client":
            bans=banr.objects.all()
            for i in bans:
                if i.email == email:
                    alert="Sorry this account was banned !"
                    return HttpResponse("<script>alert('"+alert+"');window.location.href='/register';</script>")
            if r_reg.objects.filter(email=email).exists():
                alert="This email is already exists"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/register';</script>")
            else:
                user=r_reg(name=name,email=email,password=password)
                user.save()             
                alert="Successfully Registered as Client! Login Now"
                return HttpResponse("<script>alert('"+alert+"');window.location.href='/login';</script>")
        else:
            alert="Who r u ?"
            return HttpResponse("<script>alert('"+alert+"');window.location.href='/register';</script>")
    else:
        return render(request,'register.html')
from .utils import send_otp

def request_otp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = send_otp(phone_number)  # Send OTP to the provided phone number
        request.session['otp'] = otp  # Store OTP in session for verification
        return render(request, 'verify_otp.html')  # Redirect to OTP verification page

    return render(request, 'request_otp.html')
# views.py
def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if entered_otp == str(request.session.get('otp')):
            # OTP is valid
            return render(request, 'success.html')  # Redirect to success page
        else:
            # OTP is invalid
            return render(request, 'verify_otp.html', {'error': 'Invalid OTP'})

    return render(request, 'verify_otp.html')  # Render the OTP verification form
# views.py
import qrcode
from django.shortcuts import render

def generate_qr_code(request):
    link = request.GET.get('link', 'https://www.example.com')
    
    # Generate QR code (same as before)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO object
    from io import BytesIO
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = buffer.getvalue()

    # Encode the image to base64
    import base64
    img_base64 = base64.b64encode(img_str).decode('utf-8')

    return render(request, 'qr_code.html', {'img_base64': img_base64})
def cban(request,cid):
    c=c_reg.objects.filter(id=cid).first()
    newb=banc(email=c.email)
    newb.save()
    c.delete()
    return redirect('CD')
def rban(request,cid):
    c=r_reg.objects.filter(id=cid).first()
    newb=banr(email=c.email)
    newb.save()
    c.delete()
    return redirect('ClD')
def verify(request,cid):
    s=subcription.objects.filter(id=cid).first()
    s.verified="Verified"
    s.save()
    return redirect('CD')
def Hcars(request,cid):
    if 'PC' in request.session:
        cid=r_reg.objects.filter(id=cid).first()
        cars=car.objects.all()
        c=[]
        for cc in cars:
            if cc.owner_d:
                if cc.owner_d.id==cid.id:
                    c.append(cc)
        return render(request,'Hcars.html',{'cars':c})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
def Bcars(request,cid):
    if 'PC' in request.session:
        cid=c_reg.objects.filter(id=cid).first()
        cars=booked.objects.all()
        c=[]
        for cc in cars:
            if cc.person:
                if cc.person.id==cid.id:
                    c.append(cc)
        return render(request,'Ccars.html',{'bookings':c})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
def BT(request,cid):
    if 'PC' in request.session:
        cid=c_reg.objects.filter(id=cid).first()
        cars=taxibooking.objects.all()
        c=[]
        for cc in cars:
            if cc.person:
                if cc.person.id==cid.id:
                    c.append(cc)
        return render(request,'BT.html',{'bookings':c})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
def SB(request,cid):
    if 'PC' in request.session:
        cid=c_reg.objects.filter(id=cid).first()
        cars=subcription.objects.all()
        c=[]
        for cc in cars:
            if cc.person:
                if cc.person.id==cid.id:
                    c.append(cc)
        return render(request,'SB.html',{'bookings':c})
    else:
        alert="Plzz Complete your Profile"
        return HttpResponse("<script>alert('"+alert+"');window.location.href='/profile';</script>")
def sub(request):
    if request.method == "POST":
        prize=int(request.POST.get('prize'))
        closeout=request.POST.get('drop')
        month=int(request.POST.get('month'))
        sub={
            'closeout':closeout,
            'month':month,
            'prize':prize
        }
        request.session['sub']=sub
        return redirect('paymenthandler')
    return render(request,'sub.html')
def paymenthandler(request):
    sub=request.session['sub']
    closedown=sub['closeout']
    email=request.session['email']
    user=c_reg.objects.filter(email=email).first()
    if request.method == "POST":
        tid=request.POST.get("tid")
        suber=subcription(person=user,closedown=closedown,prize=sub['prize'],month=int(sub['month']),transitionID=tid)
        suber.save()
        return redirect('profile')
    return render(request, 'payment.html',sub)

otp_storage = {}
import random
def cchangep(request, cid):
    user = c_reg.objects.filter(id=cid).first()
    if user:
        email = user.email
        otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
        dsend_vemail(email, otp)
        otp_storage[email] = otp  # Store OTP for verification
        return redirect('checkotp')
    else:
        return HttpResponse("User  not found.")

def rchangep(request, cid):
    user = r_reg.objects.filter(id=cid).first()
    if user:
        email = user.email
        otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
        dsend_vemail(email, otp)
        otp_storage[email] = otp  # Store OTP for verification
        return redirect('checkotp')
    else:
        return HttpResponse("User  not found.")
def forget(request):
    if request.method=="POST":
        handle=request.POST.get("handle")
        request.session['logined2']=handle
        email=request.POST.get("email")
        if handle=="client":
            user=r_reg.objects.filter(email=email).first()
            if user:
                
                request.session['email']=email
                otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
                dsend_vemail(email, otp)
                otp_storage[email] = otp  # Store OTP for verification
                return redirect('checkotp')
            else:
                alert = "User Not Found"
                return HttpResponse("<script>alert('" + alert + "');window.location.href='/';</script>")
        else:
            user=c_reg.objects.filter(email=email).first()
            if user:
                
                request.session['email']=email
                otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
                dsend_vemail(email, otp)
                otp_storage[email] = otp  # Store OTP for verification
                return redirect('checkotp')
            else:
                alert = "User Not Found"
                return HttpResponse("<script>alert('" + alert + "');window.location.href='/';</script>")
    return render(request,'forget.html')
def checkotp(request):
    email=request.session['email']
    if request.method == "POST":
        otp1 = int(request.POST.get('otp'))
        stored_otp = otp_storage.get(email)  # Retrieve the stored OTP
        if stored_otp and otp1 == stored_otp:
            del otp_storage[email]  # Remove OTP after successful verification
            return redirect('changepass')  # Ensure 'changepass' is a valid URL
        else:
            alert = "Wrong OTP"
            return HttpResponse("<script>alert('" + alert + "');window.location.href='/profile';</script>")
    return render(request, 'sendotp.html', {'email': email})
def changepass(request):
    logined=""
    if 'logined' in request.session:
        logined=request.session['logined']
    else:
        logined=request.session['logined2']
    new_trainer=None
    email=request.session['email']
    if logined=="customer":
        user=c_reg.objects.filter(email=email).first()
        trainer_id=user.id
        new_trainer=get_object_or_404(c_reg, id=trainer_id)
    else:
        user=r_reg.objects.filter(email=email).first()
        trainer_id=user.id
        new_trainer=get_object_or_404(r_reg, id=trainer_id)
    if request.method=="POST":
        new_trainer.password=request.POST.get("password")
        new_trainer.save()

        return redirect("changepass1")
    return render(request,'changepass.html',{'email':email})
def changepass1(request):
    return render(request,'changepass1.html')
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def dsend_vemail(email, otp):
    # Format the HTML content with the OTP
    html_content = f"""
    <html>
    <head>
    <style>
    p a b {{
            color:#ff0000;
    }}
    p a b:hover {{
            text-decoration: none;
            color:#00ff00;
    }}
    h1,p {{
    color:#00ffff;
    }}
    </style>
    </head>
      <body style="background-color: #fff; height:100vh;">
        <center><h1>Hello From i CARS!</h1>
        <p>This is the OTP to change password: <a style="text-decoration:none;"><b>{otp}</b></a></p></center>
      </body>
    </html>
    """
    
    # Create the email
    email_message = EmailMultiAlternatives(
        subject='OTP FOR CHANGE PASSWORD',
        body='This is the OTP to change password:'+str(otp),
        from_email=settings.EMAIL_HOST_USER,
        to=[email]
    )
    
    # Attach the HTML content
    email_message.attach_alternative(html_content, "text/html")
    
    # Send the email
    try:
        email_message.send()
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
         
