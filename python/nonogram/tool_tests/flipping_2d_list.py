from data_holder import DataHolder

source_list = ((DataHolder('a1'), DataHolder('a2')),
               (DataHolder('b1'), DataHolder('b2')),
               (DataHolder('c1'), DataHolder('c2')))

flipped_list = tuple(zip(*source_list))
# flipped_list = []
# for col_idx in range(len(source_list[0])):
#     tmp_list = []
#     for row_list in source_list:
#         tmp_list.append(row_list[col_idx])
#     flipped_list.append(tmp_list)

source_list[0][0].set_data('a111111')
flipped_list[0][2].set_data('c111111')
print(source_list)
print(flipped_list)
