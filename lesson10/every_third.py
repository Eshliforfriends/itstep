import even_list_generate
def every_third(range_start, range_end):
    return even_list_generate.even_list_generate(range_start, range_end)[2::3]

print(every_third(-10,46))

