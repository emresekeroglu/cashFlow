import requests


def recaptcha_check(recaptcha_response): #2
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    value = {
        'secret': '6LeqwgIlAAAAAD4Tme5QA18wNA9ubxPJwP4Tw4r8',
        'response': recaptcha_response
    }
    response = requests.post(verify_url, value)
    result = response.json()
    if result['success'] is True:
        return True
    else:
        return {'status': result['success'], 'reason': result['error-codes']} 