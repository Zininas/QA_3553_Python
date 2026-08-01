
def clean_name(name):
    """

    ' sveta  ' -> 'Sveta'
    """
    return name.strip().capitalize()

def make_username(first, last):
    """
    ' Sveta ', ' Svetlaya ' ->  'sveta_svetlaya'
    """
    return f"{first.strip()}_{last.strip()}".lower()

def is_valid_email(username):
    """
    'sveta@gmail.com'
    """
    if "@" not in username:
        return False
    domain = username.split("@")[1]
    return "." in domain
#mama
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


