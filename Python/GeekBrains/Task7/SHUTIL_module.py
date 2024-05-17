'''
Модуль shutil содержит набор функций высокого уровня для обработки файлов, групп файлов, и папок. В частности, 
доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки. Часто используется вместе 
с модулем os.

Для того, чтобы начать работать с данным модулем необходимо его импортировать в свою программу:

import shutil

Познакомимся с базовыми функциями данного модуля:

● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst.

● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.

● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path должен указывать на 
директорию, а не на символическую ссылку.

'''