
def derDecorator(dieFkt:callable) -> callable:

    def neueFkt(*args,**kwargs):
        dieFkt("Hallo:",*args,**kwargs)

    return neueFkt

@derDecorator
def meineFkt(nervig):
    print(nervig)

#meineFkt = derDecorator(meineFkt)

meineFkt()
