# Throwaway file to verify the --error flag actually fails CI on findings.
# Delete this file once the test confirms red/green as expected.

def dangerous(user_input):
    return eval(user_input)
