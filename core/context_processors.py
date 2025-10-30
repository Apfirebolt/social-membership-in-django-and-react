import datetime

def global_settings(request):
    return {
        'CURRENT_YEAR': datetime.date.today().year,
        'SITE_TITLE': "Social Membership, Inc. All rights reserved",
    }