from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    cat_id                          = models.AutoField(primary_key=True, unique=True, editable=False, null=False)
    cat_name                        = models.CharField(max_length=255, null=True)
    parent                          = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at                      = models.DateTimeField(auto_now_add=True, editable=False,null=True)

    def __str__(self):
        return self.cat_name

    class MPTTMeta:
        order_insertion_by = ['cat_name']


class Post(models.Model):

    post_id                         = models.AutoField(primary_key=True, unique=True, editable=False, null=False)
    post_title                      = models.CharField(max_length=255, null=True)
    post_slug                       = models.SlugField(max_length=255,null=True)
    post_content                    = models.TextField(null=True)
    post_category                   = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at                      = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    

    def __str__(self):
        return str(self.post_title)

