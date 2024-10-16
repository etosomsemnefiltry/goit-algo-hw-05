import search_algs as s
import timeit


def get_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError as e:
        try:
            with open(filename, 'r', encoding='cp1251') as file:
                return file.read()
        except Exception as e:
            print(f"Ошибка чтения cp1251: {e}")
            return None

text1 = get_text('file_1.txt')
text2 = get_text('file_2.txt')

key1 = 'що всередині'
key2 = 'завдання програміста'

fake = 'sfdfhategd'

kmp_time = timeit.timeit(lambda: s.kmp_search(text1, key1), number=100)
boyer_moore_time = timeit.timeit(lambda: s.boyer_moore_search(text1, key1), number=100)
rabin_karp_time = timeit.timeit(lambda: s.rabin_karp_search(text1, key1), number=100)

# Поиск реальных значений Текст 1
print('\nПоиск реальных значений Текст 1')
print(f"{kmp_time:.6f} - KMP")
print(f"{boyer_moore_time:.6f} - Boyer-Moore")
print(f"{rabin_karp_time:.6f} - Rabin-Karp\n")

kmp_time = timeit.timeit(lambda: s.kmp_search(text1, fake), number=100)
boyer_moore_time = timeit.timeit(lambda: s.boyer_moore_search(text1, fake), number=100)
rabin_karp_time = timeit.timeit(lambda: s.rabin_karp_search(text1, fake), number=100)

# Поиск фейковых значений Текст 1
print('Поиск фейковых значений Текст 1')
print(f"{kmp_time:.6f} - KMP")
print(f"{boyer_moore_time:.6f} - Boyer-Moore")
print(f"{rabin_karp_time:.6f} - Rabin-Karp\n")


kmp_time = timeit.timeit(lambda: s.kmp_search(text2, key2), number=100)
boyer_moore_time = timeit.timeit(lambda: s.boyer_moore_search(text2, key2), number=100)
rabin_karp_time = timeit.timeit(lambda: s.rabin_karp_search(text2, key2), number=100)

# Поиск реальных значений Текст 2
print('\nПоиск реальных значений Текст 2')
print(f"{kmp_time:.6f} - KMP")
print(f"{boyer_moore_time:.6f} - Boyer-Moore")
print(f"{rabin_karp_time:.6f} - Rabin-Karp\n")

kmp_time = timeit.timeit(lambda: s.kmp_search(text2, fake), number=100)
boyer_moore_time = timeit.timeit(lambda: s.boyer_moore_search(text2, fake), number=100)
rabin_karp_time = timeit.timeit(lambda: s.rabin_karp_search(text2, fake), number=100)

# Поиск фейковых значений Текст 2
print('Поиск фейковых значений Текст 2')
print(f"{kmp_time:.6f} - KMP")
print(f"{boyer_moore_time:.6f} - Boyer-Moore")
print(f"{rabin_karp_time:.6f} - Rabin-Karp\n")