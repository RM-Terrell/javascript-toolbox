import re


# https://www.hackerrank.com/challenges/time-conversion/problem
def timeConversion(twelve_hour_input):
    # remove am / pm for later
    am_pm = twelve_hour_input[-2:].lower()
    twelve_hour_input = twelve_hour_input[:-2]
    input_time_array = re.split(':', twelve_hour_input)
    input_time_array.append(am_pm)

    if am_pm == 'am':
        if input_time_array[0] == '12':
            input_time_array[0] = '00'
    elif am_pm == 'pm':
        if input_time_array[0] != '12':
            input_time_array[0] = str(int(input_time_array[0]) + 12)
    return ':'.join(input_time_array[:-1])


if __name__ == '__main__':
    twelve_hour_input = '01:05:45PM'
    result = timeConversion(twelve_hour_input)
    print(result)
