def create_key_word(customer):
    word = customer.key_word[0:3]
    number = int(customer.key_word[3:])
    num = number + 1
    return word + str(num)
