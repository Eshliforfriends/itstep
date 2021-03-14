def add_new_spell(spell_list: set, new_spell: str) -> bool:
    if new_spell in spell_list:
        return False
    else:
        spell_list.add(new_spell)
        return True


Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}
new_spell = 'Expelliarmus'

print(add_new_spell(Harry, new_spell))
print(Harry)

print(add_new_spell(Ron, new_spell))
print(Ron)