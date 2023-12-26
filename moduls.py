def tampilTrayek(awal,akhir,listTrayek):
    with open(listTrayek, 'r') as f:
        lines = f.readlines()
        for line in range(awal,akhir):
            print(lines[line])