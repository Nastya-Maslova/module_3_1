calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for i in list_to_search:
        if string.lower() in i.lower():
            flag = True
    return flag


print(string_info("Capybara"))
print(string_info("word"))
print(is_contains("urban", ["cal", "ban", "UrBAn"]))
print(calls)
