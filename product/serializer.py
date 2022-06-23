from rest_framework import serializers

from .models import Product as ProductModel
from .models import Review as ReviewModel
from datetime import datetime

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ["contents", "rating"]


class ProductSerializer(serializers.ModelSerializer):
    review_serializer = ReviewSerializer(many=True)
    
    # validate 함수 선언 시 serializer에서 자동으로 해당 함수의 validation을 해줌
    def validate(self, data):
        today = datetime.now()
        # custom validation pattern
        if data.get("exposure_end_date", "") < today:
            # validation에 통과하지 못할 경우 ValidationError class 호출
            raise serializers.ValidationError(
                    # custom validation error message
                    detail={"error": "노출 종료 일자가 현재보다 더 이전 시점이라면 상품을 등록할 수 없습니다."},
                )
        # validation에 문제가 없을 경우 data return
        return data


    def create(self, validated_data):
        today = datetime.now()
        # object를 생성할때 다른 데이터가 입력되는 것을 방지하기 위해 미리 pop 해준다.
        description = validated_data.pop('description')
        validated_data['description'] = description + f"{today}에 등록된 상품입니다."

        # User object 생성
        user = ProductModel(**validated_data)
        user.save()


    def update(self, instance, validated_data):
        today = datetime.now()
        # instance에는 입력된 object가 담긴다.
        for key, value in validated_data.items():
            if key == "description":
                value = f"{today}에 등록된 상품입니다."+ value
                continue
            
            setattr(instance, key, value)
        instance.save()
        return instance


    class Meta:
        model = ProductModel
        fields = ["id","title", "description", "writer", "exposure_start_date","exposure_end_date", "thumbnail" ]

    