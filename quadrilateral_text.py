
def string_reverser(normal_list):
    reversed_list = []
    for i in normal_list:
        reversed_list.append(i[::-1])

    return reversed_list


def quad_text(combined_lists):
    for norm_list, rever_list in combined_lists:
        text_len = len(norm_list)
        spaces = (text_len - 2) *(" ")
        lines = (text_len + 4) *("=")
        
        print(f"\n {lines} ")
        print(f"|| {norm_list} ||")
        
        for i, j in zip(norm_list[1:-1], rever_list[1:-1]):
            print(f"|| {i}{spaces}{j} ||")
        
        print(f"|| {rever_list} ||")
        print(f" {lines} ")


if __name__ == "__main__":

    normal_list = ["Joe", "John", "David", "William"] 

    reversed_list = string_reverser(normal_list)
    combined_lists = zip(normal_list, reversed_list)

    quad_text(combined_lists)
