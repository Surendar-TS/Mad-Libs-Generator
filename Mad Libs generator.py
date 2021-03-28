play =  input ( 'Play (Y/N)? :' )

if play == 'y' or play == 'Y':
    name = input ('Enter a name: ')
    place = input ('Enter a place: ')
    day = input ('Enter a day: ')
    time = input ('Enter a time: ')

    print ('--------------------------------')
    print (name, ' will be waiting for you at ', place, '.')
    print ('Please be there on ', day, ', at ', time, ' without fail')
    
