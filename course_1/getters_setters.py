class CasillaVotacion:

    def __init__(self, identificador, pais):
        self.__indentificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'la region {region} no es valida en {self.__pais}')

def run():
    casillaVotacion = CasillaVotacion(123, ['Ciudad Mexico', 'Morelos'])
    print(casillaVotacion.region)
    casillaVotacion.region = 'Morelos'
    print(casillaVotacion.region)

if __name__ == '__main__':
    run()
