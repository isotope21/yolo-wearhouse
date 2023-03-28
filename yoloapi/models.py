from django.db import models


# class Book(models.Model):
#     title = models.CharField(max_length=100)

#     @classmethod
#     def create(cls, title):
#         book = cls(title=title)
#         # do something with the book
#         return book
    

# class imageModel(models.Model):
#     geeks_field = models.ImageField()
         
#     def __str__(self):
#          return self.geeks_field


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title


class GeeksModel(models.Model):

    title = models.CharField(max_length = 200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
