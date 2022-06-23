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
    price = models.IntegerField("가격", null=True)
    modified_date = models.DateField("수정 일자", null=True)
    activation = models.BooleanField(default=True)

# product 앱에서 <작성자, 상품, 내용, 평점, 작성일>을 담고 있는 review 테이블 만들기
class Review(models.Model):
    writer = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    contents = models.TextField("내용")
    created_date = models.DateField("작성일자", auto_now_add=True)
    rating = models.IntegerField("평점")


