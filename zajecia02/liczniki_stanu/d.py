def licznik_d():
    if not hasattr(licznik_d, 'count'):
        licznik_d.count = 0
    licznik_d.count += 1
    return licznik_d.count