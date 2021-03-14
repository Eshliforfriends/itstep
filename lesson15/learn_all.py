def learn_all(my_spells: set, teacher_spell: set) -> set:
    new_spells = teacher_spell.difference(my_spells)
    my_spells.update(new_spells)
    return my_spells

Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}

print(learn_all(Ron, Harry))