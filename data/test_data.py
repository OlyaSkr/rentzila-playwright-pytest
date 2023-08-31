class Data:
    # valid credentials
    email = 'olhaskoryk039@gmail.com'
    password = 'cv5623Er23'

    # uppercase email
    uppercase_email = 'OLHASKORYK039@GMAIL.COM'

    # valid phone
    phone = '+380663258822'

    # phone in my profile
    phone_profile = '+380 66 325 8822'

    # phone without "+"
    phone_without_plus = '380663258822'

    # phone without "+" and "38"
    phone_without_plus_code = '0663258822'

    # valid email
    email_valid = 'testuserrentzila@gmail.com'

    # invalid emails
    email_with_space = 'testuser  rentzila@gmail.com'
    email_cyrillic = 'еуіегіуккутеяшдф'
    email_without_symbol = 'testuserrentzilagmail.com'
    email_without_dot = 'testuserrentzila@gmailcom'
    email_without_com = 'testuserrentzila@gmail'
    email_without_gmail = 'testuserrentzila@.com'
    email_without_gmail_com = 'testuserrentzila'
    email_with_two_symbols = 'testuserrentzila@@gmail.com'

    # invalid passwords
    password_with_space = 'Testuser10  '
    password_with_begin_space = '  Testuser10'
    password_non_exist = 'Testuser13'
    password_without_uppercase = 'testuser10'
    password_without_lowercase = 'TESTUSER10'
    password_cyrillic = 'Еуіегіук10'

    # invalid phone numbers
    phone_without_zero_code = '506743060'
    phone_without_last_number = '050674306'
    phone_with_dash = '+380-50-674-3060'
    phone_with_space = '+380 50 674 3060'
    phone_with_brackets = '+380(50)6743060'
    phone_without_code_with_brackets = '(50)6743060'
    phone_with_eleven_numbers = '05067430600'
    phone_with_other_country_code = '+10506743060'
    phone_without_code = '+0506743060'
