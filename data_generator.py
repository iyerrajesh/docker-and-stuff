import random
import string

user_ids = list(range(1, 101))
recipient_ids = list(range(1, 21))

def generate_message() -> dict:
    random_user_id = random.choice(user_ids)
    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()
    # User can't send message to himself
    #recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)
    # Generate a random message
    #vendor_chars = 'aplemsfts'
    #message = ''.join(random.choice(vendor_chars) for i in range(4))
    vendors = ['apple', 'msft', 'csco', 'adbe', 'intc', 'xlnx', 'brcm', 'vmw', 'ibm', 'goog']
    weights = [5, 5, 1, 1, 1, 1, 1, 1, 1, 1]

    return {
        'data': {
            'dev_id': random_user_id,
            'nuid': random_recipient_id,
            'vendor': random.choice(vendors),
            'foo': {'bar': ['a,b,c,d']}
        }

    }
