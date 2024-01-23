import os 

file_path = os.path.dirname(os.path.realpath(__file__))
template_dir = 'Template'
dir_path = os.path.join(file_path, template_dir)
working_dir = 'Buku'
out_path = os.path.join(file_path, working_dir)

if not os.path.isdir(out_path):
    os.mkdir(out_path)

fdict = {
    '__Title__': 'Buku',
    '__table__' : 'buku',
}
lfdict = list(fdict.keys())
filez = ['Add.vue', 'Details.vue', 'Edit.vue', 'Index.vue']


for f1 in filez :
    
    text_file_name = os.path.join(dir_path, f1)    
    print('read: ', text_file_name)
    text_file = open(text_file_name, 'r')
    data_file = text_file.read()
    
    # ubah setiap variabel
    for lf in lfdict :
        # print(fdict[lf])
        data_file = data_file.replace(lf, fdict[lf])
    
    # tutup file
    text_file.close()
    
    out_file_name = os.path.join(out_path, f1)
    out_file = open(out_file_name, 'w')
    out_file.writelines(data_file)
    
    out_file.close()

print('~~~~~~~~~~~~~~~~~~~~~~~')