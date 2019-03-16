logins = {'Vinicius': '123', 'Gabriel': '456', 'Beatriz': '1234','Jon Vlogs': '123'}


disciplinas = {'Vinicius': [['Iniciativa Vingadores' , '18/01/2010' , 'Nick Fury' ]],
               'Gabriel': [['Fisioculturismo', '5/5/2024', 'Sheviii2k']],
               'Beatriz': [['Bia Vlogs', '20/08/2019', 'Pink Mouth']]}



detalhes = {'Iniciativa Vingadores': [['Iniciativa Vingadores','25/04/1995','18/01/2010']],
            'Fisioculturismo': [['Arnold Ohio','05/05/2018','5/5/2024']],
              'Bia Vlogs':[['Bia Vlogs','11/05/2018','20/08/19']]}

detativ={'Iniciativa Vingadores':[['Os Vingadores','A Iniciativa Vingadores'
                                                   'foi um projeto secreto criado pela S.H.I.E.L.D.'
                                                   ' para criar os Vingadores, um time composto de seres'
                                                   ' poderosos que responderiam a quaisquer ameaças globais '
                                                   'que sejam grandes demais para serem lidadas na Terra. ','25/04/1995 - 18/01/2010','Nicholas J. Fury']],
         'Fisioculturismo':[['Fisiocultismo Arnold Ohio','blablablabla blablablablabla blablablablabla bla'
                             'blablablabla blablablablabla blablablablabla bla'
                             'blablablabla blablablablabla blablablablabla bla'
                             'blablablabla blablablablabla blablablablabla bla'
                             'blablablabla blablablablabla blablablablabla bla','05/05/2018 - 05/05/2024','Sheviii2k']],

         'Bia Vlogs':[['Bia Vlogs','blablablablablablablabalblablablablablabla'
                                   'blablablabla blablablablabla blablablablabla bla'
                                   'blablablabla blablablablabla blablablablabla bla'
                                   'blablablabla blablablablabla blablablablabla bla'
                                   'blablablabla blablablablabla blablablablabla bla','11/05/2018 - 20/08/2019','Boca Rosa']]}

def validar_login(login, senha):
    return (login in logins) and (logins[login] == senha)

def get_disciplinas(login):
    return disciplinas[login]

def get_detalhes(disciplina):
    return detalhes[disciplina]

def get_detativ(deta):
    return detativ[deta]
