import re

def highlight(text: str, str_to_select: str, decoration: str) -> str:
    new_str = f'{decoration}{str_to_select}{decoration}'
    result = re.sub(str_to_select, new_str, text)
    return result

text = 'Guns. LOTS of Guns'
print(highlight(text, 'LOTS', '***'))