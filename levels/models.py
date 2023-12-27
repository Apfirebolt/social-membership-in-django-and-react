from django.db import models
from social_membership.settings import AUTH_USER_MODEL


class Level(models.Model):
    lead = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subject')
    level = models.IntegerField("Level", default=0)
    share_percentage = models.IntegerField("Share Percentage", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.lead.email + ' -> ' + self.subject.email
    
    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Level"


class PlotSell(models.Model):
    amount = models.IntegerField("Amount", default=0)
    seller = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='seller')
    buyer = models.CharField("Buyer", max_length=100, blank=True, null=True)
    location = models.CharField("Location", max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.seller.email + ' -> ' + self.amount
    
    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Plot Sell"

