
def meinDecoratorErschaffer(text:str) -> callable:
    def derDecorator(dieFkt:callable) -> callable:

        def neueFkt(*args,**kwargs):
            dieFkt(text,*args,**kwargs)

        return neueFkt
    return derDecorator

@meinDecoratorErschaffer("Hallo Welt")
def meineFkt(nervig):
    print(nervig)

#meineFkt = derDecorator(meineFkt)

meineFkt()





