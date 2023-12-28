from django.db import models
from social_membership.settings import AUTH_USER_MODEL


class UserGroups(models.Model):
    name = models.CharField("Group Name", max_length=255)
    description = models.TextField("Group Description", blank=True, null=True)
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


class GroupMembers(models.Model):
    group = models.ForeignKey(UserGroups, on_delete=models.CASCADE, related_name='group_members')
    member = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member')
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    level = models.CharField("Level", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.group.name + " - " + self.member.username

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Group Members"


class Plot(models.Model):
    location = models.CharField("Location", max_length=255)
    price = models.IntegerField("Price", default=0)
    description = models.TextField("Description", blank=True, null=True)
    createdBy = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='plot_created_by')
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.location + " - " + str(self.price)

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Plot"


class PlotImages(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='plot_images')
    image = models.ImageField(upload_to='plot_images')
    title = models.CharField("Title", max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.plot.location + " - " + str(self.image)

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "Plot Images"
