m = int(input('Digite a medida (em medtros) a ser convertida aqui: '))

dcm = m * 10 # decímetro
cm = m * 100
mm = m *1000

km = m /1000
hm = m /100
dc = m /10 # decâmetro

print('{} metros são equivalentes a {} decimetros, {} centimetros e {} milimetros!'.format(m, dcm, cm, mm))
print('{} metros também são equivalentes a {} decâmetros, {} hectômetros e {} quilômetros'.format(m, dc, hm, km))
