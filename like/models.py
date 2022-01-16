from django.db import models
from memories.utils import model_utils


# Create your models here.
class Like(model_utils.TimeBasedModel, model_utils.UserBasedModel):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} liked {self.post}'
