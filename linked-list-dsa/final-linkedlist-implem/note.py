head = {
    'value': 1, 
    'next': {
        'value': 2, 
        'next': {
            'value': 3, 
            'next': {
                'value': 4, 
                'next': {
                    'value': 5, 
                    'next': None
                }
            }
        }
    }
}

print(head['next']['next']['next']['next']['value'])