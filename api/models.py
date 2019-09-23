from django.db import models    


class SerialNo(models.Model): #Will be our logger
    
    ser_no = models.CharField(max_length=20)
    
    def __str__(self):
        return "Serial No:" + self.ser_no 

class Order(models.Model):
    
    order_ids = models.CharField(max_length=20)
    ser_no = models.ForeignKey(SerialNo, on_delete=models.PROTECT)

    def __str__(self):
        return "Serial No:" + self.ser_no + "Order:" + self.order


class Status(models.Model):
    
    status = models.BooleanField()
    ser_no = models.ForeignKey(SerialNo, on_delete=models.PROTECT)

    def __str__(self):
        
        if (self.status):
            return "Serial No:" + self.ser_no + "Status: OPEN"
        else :
            return "Serial No:" + self.ser_no + "Status: CLOSE"

class Transaction(models.Model):

    trans_status = models.IntegerField()
    ser_no = models.ForeignKey(SerialNo, on_delete=models.PROTECT)
    order_ids = models.ForeignKey(Order, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self):
        if(self.trans_status==0):
            return "Complete"
        if(self.trans_status==1):
            return "Abandoned"
        if(self.trans_status==2):
            return "Incomplete"
        else:
            return None