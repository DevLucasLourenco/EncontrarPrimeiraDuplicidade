class Duplicidade():

    def __init__(self, lista: list[list],break_primeira_duplicidade=True) -> None:
        self.flag = break_primeira_duplicidade
        self.lista_tratada = list()
        self.__lista = lista
        self.encontrar_duplicadas()


    def encontrar_duplicadas(self) -> None:
        for i, item in enumerate(self.__lista):

            apoio = list()
            duplicata = list()

            for each in item:
                if not each in apoio:
                    apoio.append(each)
                else:
                    duplicata.append(each)
                    if self.flag:
                        break
                    

            self.lista_tratada.append(Duplicidade.__if_lista_duplicata_vazia(duplicata))
        

    @staticmethod
    def __if_lista_duplicata_vazia(item):
        if item == []:
            return [None]
        else:
            return item



if __name__ == "__main__":
    lista = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
            [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
            [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
            [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
            [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
            [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
            [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
            [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
            [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
            [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            ]
    
    t = Duplicidade(lista)
    print(t.lista_tratada)
    
    # output:
    # >>> [[None], [9], [2], [8], [8], [2], [2], [1], [1], [2], [5], [None]]

    ##############################
    
    t2 = Duplicidade(lista, break_primeira_duplicidade=False)
    print(t2.lista_tratada)

    # output:
    # [[None], [9, 9, 1, 8], [2, 6], [8, 7, 3], [8, 8, 1], [2, 1, 1, 9], [2, 10, 5, 10, 1], [1, 1, 1, 1], [1, 5, 7], [2, 2, 1], [5, 1, 8, 8, 7], [None]]
