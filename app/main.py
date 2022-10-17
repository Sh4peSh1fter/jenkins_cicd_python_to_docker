EMAIL_DOMAIN = "com"


def solution(S, C):
    employees_email_list = []
    unique_name_dict = {}

    for full_name in S.split(", "):
        first_name = full_name.split(' ')[0]
        last_name = full_name.split(' ')[-1].replace("-", "")

        if f"{first_name} {last_name}" in unique_name_dict.keys() and unique_name_dict[f"{first_name} {last_name}"] == '':
            unique_name_dict[f"{first_name} {last_name}"] = 2
        elif f"{first_name} {last_name}" in unique_name_dict.keys():
            unique_name_dict[f"{first_name} {last_name}"] += 1
        else:
            unique_name_dict[f"{first_name} {last_name}"] = ''

        email = f"<{first_name}.{last_name}{unique_name_dict[f'{first_name} {last_name}']}@{C}.{EMAIL_DOMAIN}>".lower()
        employees_email_list.append(full_name + " " + email)

    return ", ".join(employees_email_list)


def main():
    print(solution("John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker", "Example"))
    print(solution(input("employees names: \n> "), "Example"))


if __name__ == '__main__':
    main()