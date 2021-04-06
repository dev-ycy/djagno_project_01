from models import findall, insert, deleteby_no_and_password


def test_findall():
    results = findall()
    print(results)


def test_insert():
    name = '둘리'
    password = "1234"
    message = "호잇"

    result = insert(name, password, message)
    print(result)


def test_deleteby_no_and_password():
    no = 2
    password = '1234'

    result = deleteby_no_and_password(no, password)
    print(result)


def main():
    # test_insert()
    # test_deleteby_no_and_password()
    test_findall()


if __name__ == '__main__':
    main()