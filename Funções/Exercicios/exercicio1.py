# Faça	uma	função	que calcule a	média	de	um	aluno	de	acordo	com	o
# critério	definido. Além	disso,	 faça	uma	segunda	 função	que	informe	o
# status	do	aluno	de acordo	com	a	tabela	a	seguir:
#   Nota	acima	de	6	à “Aprovado”
#   Nota	entre	4	e	6	à Conceito	“Verificação	Suplementar”
#   Nota	abaixo	de	4	à Conceito	“Reprovado”


class CalculateGrades:
    def __init__(self, note1: int | float, note2: int | float) -> None:
        self.get_result(note1, note2)

    def get_result(self, n1, n2) -> str:
        if (n1 + n2) / 2 >= 6:
            print('Approved.')
            return

        if (n1 + n2) / 2 < 6 and (n1 + n2) / 2 >= 4:
            print('Supplemental Verification.')
            return

        print('Disapproved.')
        return


if __name__ == '__main__':
    CalculateGrades(10, 10)
