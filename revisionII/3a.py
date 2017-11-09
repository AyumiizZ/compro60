data = [
    ['01175163','Golf for Health',1,'A'],
    ['01200101','Innovative Thinking',1,'A'],
    ['01204111','Computers & Programming',3,'B+'],
    ['01355112','Foundation English II',3,'A'],
    ['01417167','Engineering Mathematics I',3,'B'],
    ['01420111','General Physics I',3,'B+'],
    ['01420113','Laboratory in Physics I',1,'C+'],
    ['01999021','Thai Language for Communication',3,'B+']
]
print('\n'.join(['{}({}) {}'.format(i[0],i[2],i[3]) for i in data]))
print('----')
print('sum: '+str(sum([i[2] for i in data])))
print('GPA: '+str(sum([4*i[2] if i[3]=='A' else(3.5*i[2] if i[3] == 'B+' else(3*i[2] if i[3] == 'B' else 2.5*i[2]))for i in data])/sum([i[2] for i in data])))
print('----')
print('\n'.join([i[1] for i in data if i[3]=='B+' ]))
print('----')
print('\n'.join([i[1] for i in data if 'Physics' in i[1]]))
print('----')
print('\n'.join([i[0]+' '+i[1] for i in data  if i[2]==1]))