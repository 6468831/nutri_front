
DEBUG = False

# ALLOWED_HOSTS =  ['89.108.115.97', 'nutritracker.ru', 'www.nutritracker.ru', 'rest.nutritracker.ru']
ALLOWED_HOSTS = ['*']


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_URL = 'https://nutritracker.ru/static/'
MEDIA_URL = 'https://nutritracker.ru/media/'

MEDIA_ROOT = '/home7/media_files'
STATIC_ROOT = '/home7/static_files'




