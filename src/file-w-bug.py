print('this should have issues')

def noncompliant():
    ls = [1, 2, 3]
    foo(ls[3])  # Noncompliant
