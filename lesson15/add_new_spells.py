def add_new_spell(spell_list: set,*args: set) -> bool:
    for elem in args:
        if elem in spell_list:
            return False
            break
        else:
            spell_list.add(elem)
            return True

Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}

print(add_new_spell(Harry, 'Expelliarmus', 'Lumos', 'Obliviate'))
print(Harry)