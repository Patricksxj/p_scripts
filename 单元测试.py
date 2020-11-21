
class newtest:
    def setUp():
        a=1+2+3
        print("Before every test case!")

    def test_case_01():
        print("this is test case 1")

    def test_case_02():
        a = 1 + 2 + 3
        print("a=%s" % a)
        print("this is test case 2")

def main():
    newtest.test_case_02()

if __name__ == "__main__":
    main()