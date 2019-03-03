from django.db import models
from useraccounts.models import UserModel,Pharamcy,Organisation
# Create your models here.

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # archived = models.BooleanField(default=False)
    # def delete(self,*args, **kwargs):
    #     self.archived = True
    #     super().save(self,*args, **kwargs)
    #     super().save(*args, **kwargs)
    class Meta:
        abstract = True

class Medicine(CommonModel):
    name = models.CharField(max_length=30)
    mrp =models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.IntegerField()
    pricePerTablet = models.DecimalField(max_digits=12,decimal_places=10,default=0)
    def save(self,*args,**kwargs):
        if not self.id:
            self.pricePerTablet = (self.mrp/self.quantity)
            #self.username=self.user.user
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'medicine/user_{0}/medicine_{1}/{2}'.format(instance.user.id,instance.medicine.id, filename)

def get_user_image_folder(instance, filename):
    return 'expirydate/user_{0}/medicine_{1}/{2}'.format(instance.user.id,instance.medicine.id, filename)


class MedicineOfUser(CommonModel):
    user = models.ForeignKey(UserModel,
                    related_name="medicineOfUser",
                    on_delete=models.CASCADE,
                    blank=True
                    )
    medicine = models.ForeignKey(Medicine,
                    on_delete=models.CASCADE
                    )
    creditForMedicine= models.DecimalField(max_digits=6, decimal_places=2,default=0,null=True,blank=True)
    expiryDate=models.DateField()
    medicinePicture = models.ImageField(upload_to=user_directory_path,blank=True)
    expiryPicture =models.ImageField(upload_to=get_user_image_folder,blank=True)
    quantityOfMedicine = models.IntegerField()
    pharmacist=models.ForeignKey(
        Pharamcy,
        null=True,
        on_delete=models.DO_NOTHING,
        blank=True

    )
    isSoldByPharmacist = models.BooleanField(default=False)
    isAcceptedByPharmacist = models.BooleanField(default=False)
    isRequested =models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if not self.id:
            self.creditForMedicine = self.quantityOfMedicine * self.medicine.pricePerTablet

        # if self.pharmacist is not None :
        #     self.user.totalCredits = self.user.totalCredits + self.creditForMedicine
        #     self.user.save()
        # if self.isAccepteByPharmacist == True:
        #     self.user.totalCredits = self.user.totalCredits - self.creditForMedicine
        #     self.pharmacist.totalCredits =self.pharmacist.totalCredits + self.creditForMedicine
        #     self.user.save()
        #     self.pharmacist.save()
            #self.username=self.user.user
        super().save(*args,**kwargs)

# class Transaction(CommonModel):
#     transactionID=models.BigAutoField()
#     medicineOfUser=models.ForeignKey(
#                     MedicineOfUser, 
#                     on_delete=models.CASCADE
#                     )


class RequestedMedicines(CommonModel):
    medicineRequested = models.CharField(max_length=20)
    details = models.CharField(max_length=50)
    isAccepted= models.BooleanField(default=False)