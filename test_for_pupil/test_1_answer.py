# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import turtle as t

count = 0 #шаг цикла рисования

t.shape("turtle") 

t.pencolor('red')#цвет линий - красный
t.fillcolor('yellow')#цвет заливки квадрата - желтый
t.bgcolor("blue")#цвет фона окна - синий

t.begin_fill() #объявляем, что замкнутый контур (наш квадрат) будет залит

while count #завершим условие цикла (не забудем поставить двоеточие)
#---добавьте недостающий код (помним про вложенность после двоеточия)
#---недостающий код, строка 1 (двигаем "черепашку" на 150 шагов вперед)
#---недостающий код, строка 2 (поворачиваем "черепашку" на 90 градусов вправо)
    count+=1

t.end_fill() #завершение заливки (замкнутые контуры более заливаться не будут)
    
t.mainloop()

