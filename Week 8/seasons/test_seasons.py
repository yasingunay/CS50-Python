from seasons import check_birth

def main():
    test_check_birth()

def test_check_birth():
    assert check_birth('1994-07-04') == ("1994", "07", "04")
    assert check_birth('1994-7-4') == None
    assert check_birth("July 4, 1994") == None


if __name__ =="__main__":
    main()