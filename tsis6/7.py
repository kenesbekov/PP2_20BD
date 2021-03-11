# def count_str(s):
#     d = {'Upper Case': 0, 'Lower Case': 0}
#     for ch in s:
#         if ch.isupper():
#             d['Upper Case'] += 1
#         elif ch.islower():
#             d['Lower Case'] += 1
#     print('# Of Uppers: %d'%d['Upper Case'],
#           '# Of Lowers: %d'%d['Lower Case'], sep = '\n')

# count_str(input())

s = input()
print('# Of Uppers: %d' %sum(1 for ch in s if ch.isupper()),
      '# Of Lowers: %d' %sum(1 for ch in s if ch.islower()), sep ='\n')