
times = ('Palmeiras','Cruzeiro','Grêmio','Santos',
'Corinthians','Flamengo','Atlético Mineiro','Athletico Paranaense',
'Internacional','Chapecoense','Botafogo','São Paulo','Fluminense','Vasco da Gama',
'Bahia','Sport','Vitória','Ponte Preta','América','Coritiba')

print  ('\n',' '*8,'5 PRIMEIROS TIME NO BRASILEIRÃO 2019:\n','- '*31,'\n', times[0:5],'\n','- '*31,)
print  ('\n',' '*8,'OS ULTIMOS 4 TIMES COLOCADOS NA TABELA:\n','- '*24,'\n',times[15:19],'\n','- '*24,)
print('\n',' '*8,'TIMES EM ORDEM ALFABÉTICA:\n' ,'- '*52,'\n',sorted(times),'\n\n','- '*52,)
print('\n',' '*9,'POSIÇÃO CHAPECOENSE \n',' '*8,'- '*7,'\n',' '*10,times.index('Chapecoense'),'Posicão','\n',' '*8,'- '*7)

