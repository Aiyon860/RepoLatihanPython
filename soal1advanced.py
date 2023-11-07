class Penilaian:
    def __init__(self, grade: int):
        assert type(grade) == int
        assert grade >= 0 and grade <= 100, f"Grade {grade} is not in range 0-100!"
        self.grade = grade

    def angka_ke_huruf(self):
        if self.grade > 90 and self.grade <= 100:
            print('A')
        elif self.grade > 80 and self.grade <= 90:
            print('B')
        elif self.grade > 70 and self.grade <= 80:
            print('C')
        elif self.grade > 60 and self.grade <= 70:
            print('D')
        elif self.grade > 50 and self.grade <= 60:
            print('E')

nilai_1 = Penilaian(100)
nilai_1.angka_ke_huruf()
nilai_2 = Penilaian(90)
nilai_2.angka_ke_huruf()
nilai_3 = Penilaian(80)
nilai_3.angka_ke_huruf()
nilai_4 = Penilaian(70)
nilai_4.angka_ke_huruf()
nilai_5 = Penilaian(60)
nilai_5.angka_ke_huruf()
nilai_6 = Penilaian(50)
nilai_6.angka_ke_huruf()
nilai_7 = Penilaian(-10)    # AssertionError
nilai_8 = Penilaian(110)    # AssertionError