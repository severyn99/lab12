import re


if __name__ == "__main__":

    pattern = r"\S+\s-\s-\s\[(?:08|09|10)\/Mar\/2004:(?:07:10:27|0[8-9]:\d{2}:\d{2}|10:\d{2}:|d{2}|11:[0-4]\d:\d{2}|16:2[01]:\d{2})\s\S+\]\s\S+\s\S+\s\S+\s[2]\d{2}\s\S+"
    number_of_matched_requests = 0
    read_lines = 0

    with open("access_log") as file:
        for line in file:
            read_lines += 1
            if re.match(pattern, line):
                number_of_matched_requests += 1
                print(re.findall(pattern, line))

    print("\nNumber of all read lines: %d" % read_lines)
    print("\nNumber of all successful requests between 08/Mar/2004:07:11:37 and 10/Mar/2004:11:41:52: %d" % number_of_matched_requests)
