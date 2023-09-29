import numpy as np
import matplotlib.pyplot as plt
x = [0.021658, 0.035035, 0.047775]
y = [0.32,0.446,0.67]

x1 = [0.0159936, 0.025872, 0.035228]
y1 = [0.285,0.4,0.528]
plt.title('График зависимости ω = f(Mэ) при Н = const',style="italic")
plt.plot(x, y, label = 'Внутренняя', color = 'r')
plt.plot(x1, y1, label = 'Внешняя', color = 'b')
plt.scatter(x,y, color = 'r')
plt.scatter(x1,y1, color = 'b')
plt.xlabel('Mэ, Н*м', position = (1, -1), style="italic")
plt.ylabel('W, град/с', position = (2.1, 1), rotation = -180+90+45+45, style="italic")
plt.legend(fontsize = 10,
          ncol = 2,    #  количество столбцов
          facecolor = 'oldlace',    #  цвет области
          edgecolor = 'r',    #  цвет крайней линии
          title = 'Прямые',    #  заголовок
          title_fontsize = '10'    #  размер шрифта заголовка
         )

plt.grid()
plt.show()