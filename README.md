<h1 align='center'> BLAST парсинг с помощью Biopython </h1>

### ❗Важно
Скрипт использует библиотеки Biopython, datetime и time, shutil, os. Для корректной работы скрипта требуется установить Python 3.11 и Biopython через pip. 
```
>>> pip install biopython
```

### ⚙️ Принцип работы

Скрипт на вход получает **.fasta** файл (*sequence.fasta*), содержащий последовательность нуклеотидов внутри. Используя модуль **SeqIO**, **NCBIWWW** и **NCBIXML** программа отправляет запрос в базу данных нуклеотидных последовательностей (*nt*) по модели **blastn**. После она выводит результат парсинга и сохраняет XML файл.

### ❓ Что планируется в будущем
