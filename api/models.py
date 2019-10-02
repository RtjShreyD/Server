from django.db import models    

class SerialNo(models.Model):
    
    ser_no = models.CharField(max_length=20)
    
    def __str__(self):
        return "Serial No:" + self.ser_no 


class Users(models.Model):
    
    user = models.CharField(max_length = 20)
    ser_no = models.ForeignKey(SerialNo, on_delete=models.CASCADE)

    def __str__(self):
        return "User:" + self.user + "Operating at Box:" + self.ser_no


class Order(models.Model):
    
    order_ids = models.CharField(max_length=20)
    ser_no = models.ForeignKey(SerialNo, on_delete=models.CASCADE)

    def __str__(self):
        return "Serial No:" + self.ser_no + "Order:" + self.order


class Status(models.Model):
    
    status = models.BooleanField()
    ser_no = models.ForeignKey(SerialNo, on_delete=models.CASCADE)

    def __str__(self):
        
        if (self.status):
            return "Serial No:" + self.ser_no + "Status: OPEN"
        else :
            return "Serial No:" + self.ser_no + "Status: CLOSE"



            