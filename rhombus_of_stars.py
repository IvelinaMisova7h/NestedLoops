n = int(input())

for row in range(1, n+1):
    print(' '*(n-row) + '* '*row)

for row in range(1, n):
    print(' '*row + '* '*(n-row))

# Second solve

#space = ' '
#star = '*'
#secon_part_star = 0
# for row in range(1, 2*n):
    # if row <= n:
        #space = n - row
        #star = row
        #print(' '*space + '* '*star)
    # else:
        #space = row - n

        #print(' '*space + '* '*second_part_star)
        #second_part_star -= 1
