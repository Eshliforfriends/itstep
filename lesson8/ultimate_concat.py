first_list = ['Neo', 'Trinity', 'Mouse']
second_list = ['Matrix', 'Forever', 'Alone']
output_list = ['{} {}'.format(a, b) for a in first_list for b in second_list]
print(output_list)