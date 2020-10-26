class monaie:
    def ajouter(self,devise1,valeure2,devise2):

        try:
            if devise2==devise1:
              val=valeure2 + self
              return val
        except:
         val="ce n'est pas la meme devise"
         return val
    def retrancher(self, devise1, valeure2, devise2):
        try:
            devise2 == devise1
            return valeure2 - self

        except TypeError:
            print("erreure de type")
value=monaie
print(value.ajouter(7,"euro",5,"euro"))
print(value.retrancher(7,"euro",5,"dollars"))


