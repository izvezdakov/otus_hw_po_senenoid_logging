def determine_current_currency(message):
    if '$' in message:
        return '$'
    elif '€' in message:
        return '€'
    elif '£' in message:
        return '£'
    else:
        raise ValueError('cant determine_current_currency')
