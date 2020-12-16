normal_list = ["Joe", "John", "David", "William"] 


def initialization():
    rev_list = string_reverser()
    combined_lists = zip(normal_list, rev_list)
    quad_text(list(combined_lists))

def string_reverser():
    reversed_list = []
    for i in normal_list:
        reversed_list.append(i[::-1])
    return(reversed_list)

def quad_text(combined_lists):
    for (norm_list, reve_list) in combined_lists:
        text_len = len(norm_list)
        spaces = (text_len - 2) *(" ")
        lines = (text_len + 4) *("=")
        print("\n")
        print(f" {lines} ")
        print(f"|| {norm_list} ||")
        for i, j in zip(norm_list[1:-1], reve_list[1:-1]):
            print(f"|| {i}{spaces}{j} ||")
        print(f"|| {reve_list} ||")
        print(f" {lines} ")

initialization()