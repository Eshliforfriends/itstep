def unique_spells(ron_spells: set, harry_spells: set) -> set:
    unique_spell = ron_spells.difference(harry_spells)
    unique_spell.update(harry_spells.difference(ron_spells))
    return unique_spell


Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}

print(unique_spells(Ron, Harry))