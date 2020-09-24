n1, n2, n3, n4 = input().split(' ')

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 *4) + (n4 * 1))/ 10.0

if media >= 7.0:
    print(f"""Media: {media:.1f}
Aluno aprovado.""")
elif media >= 5.0 and media <= 6.9:
    print(f"""Media: {media:.1f}
Aluno em exame.""")
    ne = float(input())
    print("Nota do exame: {}".format(ne))
    media = (media + ne)/2.0
    if media >= 5.0:
        print(f"""Aluno aprovado.
Media final: {media:.1f}""")
    else:
        print(f"""Aluno reprovado.
Media final: {media:.1f}""")
else:
    print(f"""Media: {media:.1f}
Aluno reprovado.""")