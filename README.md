<h1 align='center'> BLAST парсинг с помощью Biopython </h1>

### ❗Важно
Скрипт использует библиотеки Biopython, datetime и time, os. Для корректной работы скрипта требуется установить Python 3.11 и Biopython через pip. 
```
>>> pip install biopython
```

### ⚙️ Принцип работы

Скрипт на вход получает **.fasta** файл (*sequence.fasta*), содержащий последовательность нуклеотидов внутри. Используя модуль **SeqIO**, **NCBIWWW** и **NCBIXML** программа отправляет запрос в базу данных нуклеотидных последовательностей (*nt*) по модели **blastn**. После она выводит результат парсинга и сохраняет XML файл.

### Пример вывода в консоли

![image](https://github.com/mrjabka/BLAST_Parcing/assets/157302347/08c47efd-e400-4cbe-816a-ba93215c9741)

### Вывод в BLAST WEB

![image](https://github.com/mrjabka/BLAST_Parcing/assets/157302347/3627c7bf-92da-4965-86ff-c5749cbcafd9)


### ❓ Что планируется в будущем

- Сделать веб-интерфейс для программы.
- Создать свою базу данных на основе BLAST'а.
