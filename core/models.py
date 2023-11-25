from django.db import models
from social_membership.settings import AUTH_USER_MODEL


class UserGroups(models.Model):
    name = models.CharField("Group Name", max_length=255)
    description = models.TextField("First Name", blank=True, null=True)
    createdBy = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_created_by')
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    

    def __str__(self):
        return self.name

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "User Group"


class Message(models.Model):
    text = models.TextField("Message Text", blank=True, null=True)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='message_send_by')
    group = models.ForeignKey(UserGroups, on_delete=models.CASCADE, related_name='user_groups')
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    

    def __str__(self):
        return self.text

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Message"
