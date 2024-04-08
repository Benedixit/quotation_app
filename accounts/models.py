from django.db import models

# Create your models here.
class Cost(models.Model):
    overhead_cost = models.DecimalField(max_digits=15, decimal_places=2)

class Salaries(models.Model):
    salary = models.DecimalField(max_digits=15, decimal_places=2, default=None)
    task = models.CharField(max_length=50, default=None)

    class Meta:
        verbose_name = 'Salary'
        verbose_name_plural = 'Salaries'

    def __str__(self):
        return self.task
    



class PriceDetail(models.Model):

    company_name = models.CharField(max_length=500)

    invoice_id = models.CharField(max_length=50)

    invoice_title = models.CharField(max_length=255)

    company_location = models.CharField(max_length=255)

    moodboard_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    illustration_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    storyboard_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    compositing_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    editing_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    motion_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    modelling_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    texturing_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    rigging_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    lookdev_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    layout_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    animation_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    fx_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    lighting_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    rendering_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    voiceover_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    audio_studio_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    music_sync_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)
    
    prod_mgt = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    total_sum = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    vat_price = models.CharField(max_length=100, default="FREE", blank=True, null=True)

    final_cost = models.CharField(max_length=100, default="FREE", blank=True, null=True)



    def __str__(self):
        return f"{self.company_name} - Invoice: {self.invoice_id}"
    

class PriceInclude(models.Model):

    moodboard = models.BooleanField(default=True)
    illustration = models.BooleanField(default=True)
    storyboard = models.BooleanField(default=True)
    compositing = models.BooleanField(default=True)
    editing = models.BooleanField(default=True)
    motion = models.BooleanField(default=True)
    modelling = models.BooleanField(default=True)
    texturing = models.BooleanField(default=True)
    rigging = models.BooleanField(default=True)
    animation = models.BooleanField(default=True)
    fx = models.BooleanField(default=True)
    lighting = models.BooleanField(default=True)
    rendering = models.BooleanField(default=True)
    voiceover = models.BooleanField(default=True)
    music_sync = models.BooleanField(default=True)
    audio_studio = models.BooleanField(default=True)
    layout = models.BooleanField(default=True)
    lookdev = models.BooleanField(default=True)
    price_detail = models.OneToOneField("PriceDetail", on_delete=models.CASCADE, default=None)
    
    
    def __str__(self):
        return f'{self.price_detail}'