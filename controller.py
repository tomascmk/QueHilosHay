def checkNation(nation, type):
    isFrom = False
    for country in countriesL:
        if nation in country:
            isFrom = True
    if not nation:
        for country in countriesM:
            if nation in country:
                isFrom = True
    if not nation:
        for country in countriesS:
            if nation in country:
                isFrom = True
    if nation:
        print('')
        print('\t !', type, ' check FAILED')
    if not nation:
        print('')
        print('\t √', type, ' check SUCCESS')
    return isFrom


countriesL = ['PARAGUAY', 'MEXICO', 'MEJICO', 'BOLIVIA', 'VENEZUELA', 'ESPAÑA', 'ESPANA', 'ESPANIA', 'ECUADOR', 'CHILE',
              'COLOMBIA']
countriesM = ['Paraguay', 'México', 'Mexico', 'Méjico', 'Mejico', 'Bolivia', 'Venezuela', 'España', 'Espana', 'Espania',
              'Ecuador', 'Chile', 'Colombia']
countriesS = ['paraguay', 'méxico', 'mexico', 'méjico', 'mejico', 'bolivia', 'venezuela', 'españa', 'espana', 'espania',
              'ecuador', 'chile', 'colombia']