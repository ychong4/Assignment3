from django.conf import settings
# Ability to point to Production or Sandbox URLs
JUST_GIVING_WEB_URL = getattr(settings, 'JUST_GIVING_WEB_URL', 'http://www.staging.justgiving.com')
JUST_GIVING_API_URL = getattr(settings, 'JUST_GIVING_API_URL', 'http://api.staging.justgiving.com')
# Replace below with your personal details
JUST_GIVING_CHARITY_ID = getattr(settings, 'JUST_GIVING_CHARITY_ID', '261405315')
JUST_GIVING_APP_ID = getattr(settings, 'JUST_GIVING_APP_ID', 'b3d13434')
# Add a list of all the currencies you need to support
CURRENCIES = getattr(settings, 'CURRENCIES', ['USD'])

