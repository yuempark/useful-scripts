original_title = input('Enter the title:\n')
print('')

upper_inds = []
for ind,char in enumerate(original_title):
    if char.isupper():
        upper_inds.append(ind)

new_title = (original_title+'.')[:-1]

n_braces_added = 0
for i in range(len(upper_inds)):
    braced_i = upper_inds[i] + n_braces_added
    new_title = new_title[:braced_i] +\
                '{' + new_title[braced_i] + '}' +\
                new_title[braced_i+1:]
    n_braces_added = n_braces_added + 2

print('Capitalized title:')
print(new_title)
