from django.db import models
from memories.utils import model_utils, image_utils
# Create your models here.


class Post(model_utils.TimeBasedModel, model_utils.UserBasedModel):
    caption = models.TextField()
    slug = models.SlugField(default=model_utils.gen_slug)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - memories {self.slug}'

class PostFile(model_utils.TimeBasedModel):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=image_utils.get_upload_path)

    def __str__(self):
        return f'{self.post.slug} file'