data = {
    '01175163': {'Name': 'Golf for Health','Unit': 1, 'Grade': 'A'},
    '01200101': {'Name': 'Innovative Thinking', 'Unit': 1, 'Grade': 'A'},
    '01204111': {'Name': 'Computers & Programming', 'Unit': 3, 'Grade': 'B+'},
    '01355112': {'Name': 'Foundation English II', 'Unit': 3, 'Grade': 'A'},
    '01417167': {'Name': 'Engineering Mathematics I', 'Unit': 3, 'Grade': 'B'},
    '01420111': {'Name': 'General Physics I', 'Unit': 3, 'Grade': 'B+'},
    '01420113': {'Name': 'Laboratory in Physics I', 'Unit': 1, 'Grade': 'C+'},
    '01999021': {'Name': 'Thai Language for Communication', 'Unit': 3, 'Grade': 'B+'}
}
print('\n'.join(['{}({}) {}'.format(i,data[i]['Unit'],data[i]['Grade']) for i in data]))
print('----')
print('sum: '+str(sum([data[i]['Unit'] for i in data])))
print('GPA: '+str(sum([4*data[i]['Unit'] if data[i]['Grade']=='A' else(3.5*data[i]['Unit'] if data[i]['Grade'] == 'B+' else(3*data[i]['Unit'] if data[i]['Grade'] == 'B' else 2.5*data[i]['Unit']))for i in data])/sum([data[i]['Unit'] for i in data])))
print('----')
print('\n'.join([data[i]['Name'] for i in data if data[i]['Grade']=='B+' ]))
print('----')
print('\n'.join([data[i]['Name'] for i in data if 'Physics' in data[i]['Name']]))
print('----')
print('\n'.join([i+' '+data[i]['Name'] for i in data  if data[i]['Unit']==1]))
