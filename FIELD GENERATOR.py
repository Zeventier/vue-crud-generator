models = ['judul', 'penulis', 'isi'] # Tambahkan field table disini menggunakan format array
table = 'berita' # Tambahkan nama table disini

th = '''
        <th>__Field__</th>
'''

td = '''
        <td>{{ item.__field__ }}</td>
'''

form = '''
        <div class="form-group mb-3">
                <label for="__field__" class="form-label">__Field__</label>
                <input type="text" class="form-control col-md-6" id="__field__" v-model="form.__field__" />
        </div>
        <div class="text-red-500" v-if="form.errors.__field__">
                {{ form.errors.__field__ }}
        </div>
'''

details = '''
        <p class="card-text">__Field__: {{ __table__.__field__ }}</p>
'''

print ('-----------INDEX------------')
for m in models:
    print (th.replace('__Field__', m.capitalize()))
    
print ('----------------------------')

for m in models:
    print (td.replace('__field__', m))
    
print ('----------------------------')
print ()
print ('---------ADD & EDIT---------')
for m in models:
    print (form.replace('__field__', m).replace('__Field__', m.capitalize()))

print ('----------------------------')
print ()
print ('----------DETAILS-----------')
for m in models:
    print (details.replace('__field__', m).replace('__table__', table).replace('__Field__', m.capitalize()))
