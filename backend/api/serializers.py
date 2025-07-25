from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)
   

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_product = serializers.SerializerMethodField(read_only=True)

    def get_other_product(self, obj):
        request = self.context.get('request')
        user = obj
        my_product_qs = user.product_set.all()[:5]
        return UserProductInlineSerializer(my_product_qs, many=True,context=self.context).data 