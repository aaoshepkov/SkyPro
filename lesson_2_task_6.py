lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

def list_parser():
    for i in(lst):
        if i < 30 and i % 3 == 0:
            print(i, end=',')
list_parser()