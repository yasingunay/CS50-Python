from seasons import check_birth

def main():
    test_check_birth()

def test_check_birth():
    assert check_birth('1990-01-01') == ("1990", "01", "01")
    assert check_birth('1990-1-1') == None
    assert check_birth("July 1, 1991") == None


if __name__ =="__main__":
    main()
