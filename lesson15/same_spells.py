def same_spells(ron_spells: set, harry_spells: set) -> set:
    same_spell = ron_spells.intersection(harry_spells)
    return same_spell


Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}

print(same_spells(Ron, Harry))