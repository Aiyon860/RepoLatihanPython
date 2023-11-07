def angka_ke_huruf(grade):
    assert type(grade) == int
    assert grade >= 0 and grade <= 100, f"Grade {grade} is not in range 0-100!"

    if grade > 90 and grade <= 100:
        print('A')
    elif grade > 80 and grade <= 90:
        print('B')
    elif grade > 70 and grade <= 80:
        print('C')
    elif grade > 60 and grade <= 70:
        print('D')
    elif grade > 50 and grade <= 60:
        print('E')
    elif grade <= 50:
        print('F')

# Testing
angka_ke_huruf(100)
angka_ke_huruf(95)
angka_ke_huruf(90)
angka_ke_huruf(85)
angka_ke_huruf(80)
angka_ke_huruf(70)
angka_ke_huruf(75)
angka_ke_huruf(65)
angka_ke_huruf(60)
angka_ke_huruf(55)
angka_ke_huruf(50)
angka_ke_huruf(45)
angka_ke_huruf(110)     # AssertionError from line 3