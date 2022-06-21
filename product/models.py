from django.db import models

# Create your models here.
class Product(models.Model):
    writer = models.ForeignKey("user.User", on_delete=models.CASCADE)
    title = models.CharField(max_length = 30)
    description = models.TextField("설명")
    exposure_start_date = models.DateField("노출 시작일자", null=True)
    exposure_end_date = models.DateField("노출 종료일자", null=True)
    thumbnail = models.FileField("썸네일", upload_to="product/")
    created_date = models.DateField("등록일자", auto_now_add=True)

