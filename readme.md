## Проект на тему: «Интерполирование трансцендентных функций»
Исследовать поведение функций интерполяции (найти неизвестные промежуточные значений с помощью нескольких известных).

Подзадачи:
1) Табулирование erf(x) на определенном отрезке [a,b] с некоторым шагом h с точностью eps. В итоге получить таблицу с значениями.
2) На следующем шаге по полученной таблице значений необходимо вычислить полином Лагранжа по равномерно распределенным узлам, а также необходимо посчитать погрешность в зависимости от количества узлов.
3) На последнем шаге необходимо вычислить полином Лагранжа, однако уже по Чебышевским узлам. Еще необходимо посчитать погрешность и построить график зависимости от количества узлов.

---
#### Заключение:

При вычислении интерполяционного полинома Лагранжа функция на равномерно распределенных узлах сначала дает минимальную погрешность, однако при увеличении количества узлов эта погрешность возрастает. 
И растет очень быстро. Вычисление полинома Лагранжа по корням Чебышева, наоборот, дают минимальную погрешность при увеличении количества узлов. 

