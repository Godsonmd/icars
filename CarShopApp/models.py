from django.db import models

# Create your models here.
STATES = {
('Andhra Pradesh', 'Andhra Pradesh'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Assam', 'Assam'),
('Bihar', 'Bihar'),
('Chhattisgarh', 'Chhattisgarh'),
('Goa', 'Goa'),
('Gujarat', 'Gujarat'),
('Haryana', 'Haryana'),
('Himachal Pradesh', 'Himachal Pradesh'),
('Jharkhand', 'Jharkhand'),
('Karnataka', 'Karnataka'),
('Kerala', 'Kerala'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Maharashtra', 'Maharashtra'),
('Manipur', 'Manipur'),
('Meghalaya', 'Meghalaya'),
('Mizoram', 'Mizoram'),
('Nagaland', 'Nagaland'),
('Odisha', 'Odisha'),
('Punjab', 'Punjab'),
('Rajasthan', 'Rajasthan'),
('Sikkim', 'Sikkim'),
('Tamil Nadu', 'Tamil Nadu'),
('Telangana', 'Telangana'),
('Tripura', 'Tripura'),
('Uttar Pradesh', 'Uttar Pradesh'),
('Uttarakhand', 'Uttarakhand'),
('West Bengal', 'West Bengal')
}

class c_reg(models.Model):
    dp=models.ImageField(upload_to='cdp/', blank=True,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    dob=models.DateField(null=True)
    phone=models.IntegerField(null=True)
    drive_l_f=models.ImageField(upload_to='cdrlf/', blank=True,null=True)
    drive_l_b=models.ImageField(upload_to='cdrlb/', blank=True,null=True)
    def __str__(self):
        return self.name
class a_reg(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.email
class r_reg(models.Model):
    dp=models.ImageField(upload_to='rdp/', blank=True,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    dob=models.DateField(null=True)
    phone=models.IntegerField(null=True)
    drive_l_f=models.ImageField(upload_to='rdrlf/', blank=True,null=True)
    drive_l_b=models.ImageField(upload_to='rdrlb/', blank=True,null=True)
    def __str__(self):
        return self.name
    



    
class car(models.Model):
    campany=models.CharField(max_length=100)
    carname=models.CharField(max_length=100)
    seater=models.IntegerField()
    noplate=models.CharField(max_length=100)
    gear=models.CharField(max_length=100)
    fuel=models.CharField(max_length=100)
    rate=models.FloatField()
    kms=models.CharField(max_length=100)
    state=models.CharField(max_length=20,choices=STATES,default='Kerala')
    owner=models.CharField(max_length=100)
    owner_d=models.ForeignKey(r_reg,on_delete=models.CASCADE, blank=True,null=True)
    car_f_photo=models.ImageField(upload_to='carphoto/')
    def __str__(self):
        return self.carname+" { "+self.noplate+" } "+self.owner+" | "+self.state
class booked(models.Model):
    car=models.ForeignKey(car,on_delete=models.CASCADE)
    person=models.ForeignKey(c_reg,on_delete=models.CASCADE)
    booked_time=models.DateTimeField(auto_now_add=True)
    pickup=models.DateTimeField()
    dropdown=models.DateTimeField()
    pickupl=models.TextField()
    dropdownl=models.TextField(null=True,blank=True,default=pickupl)
class taxibooking(models.Model):
    person=models.ForeignKey(c_reg,on_delete=models.CASCADE)
    booked_time=models.DateTimeField(auto_now_add=True)
    pickup=models.DateTimeField()
    pickupl=models.TextField()
    noP=models.IntegerField()





VERIFY = {
('Verified', 'Verified'),
('Not verified', 'Not verified'),
}
class subcription(models.Model):
    person=models.ForeignKey(c_reg,on_delete=models.CASCADE)
    booked_time=models.DateField(auto_now_add=True)
    closedown=models.DateField()
    prize=models.FloatField()
    month=models.IntegerField()
    transitionID=models.CharField(max_length=100)
    verified=models.CharField(choices=VERIFY,max_length=20,default='Not verified')
    def __str__(self):
        return self.person.name+" { "+str(self.month)+" } "+str(self.prize)+" | "+self.verified
    
class banc(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email
class banr(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email
