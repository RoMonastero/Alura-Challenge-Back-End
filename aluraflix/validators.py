import re
import validators

def valida_url(url):
    try:
        return validators.url(url)
    except:
        return False

