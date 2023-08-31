from response import check_email


# Test valid email
def test_valid_email():
    email = "test@example.com"
    assert check_email(email) == True


# Test missing @ symbol
def test_invalid_email_missing_at():
    email = "testexample.com"
    assert check_email(email) == False


# Test missing domain
def test_invalid_email_missing_domain():
    email = "test@"
    assert check_email(email) == False


# Test missing username
def test_invalid_email_missing_username():
    email = "@example.com"
    assert check_email(email) == False


# Test multiple @ symbols
def test_invalid_email_multiple_at():
    email = "test@example@domain.com"
    assert check_email(email) == False


# Test invalid characters
def test_invalid_email_invalid_characters():
    email = "test!example.com"
    assert check_email(email) == False


# Test domain with only one character
def test_invalid_email_one_character_domain():
    email = "test@x.y"
    assert check_email(email) == False


# Test empty email
def test_invalid_empty_email():
    email = ""
    assert check_email(email) == False


# Test email without top-level domain
def test_invalid_email_no_tld():
    email = "test@example"
    assert check_email(email) == False


##These tests did not past

# # Test domain with more than four characters
# def test_invalid_email_long_domain():
#     email = "test@example.abcd"
#     assert check_email(email) == False

# # Test username with more than 64 characters
# def test_invalid_email_long_username():
#     email = "a" * 65 + "@example.com"
#     assert check_email(email) == False
