def dfa(string, n):
    """
    Initial state of the DFA.

    This function checks if the first character of the string is 'a'
    and if there are more characters to process. If so, it transitions
    to state s0.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if (string[n] == 'a') and (n < len(string) - 1):
        s0(string, n + 1)
    else:
        print('Rejected')


def s0(string, n):
    """
    State s0 of the DFA.

    This function handles the transition from state s0. If the current 
    character is 'n', it transitions to state s1. If the current character 
    is 'm', it transitions to state s7.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if string[n] == 'n':
        s1(string, n + 1)
    elif string[n] == 'm':
        s7(string, n + 1)
    else:
        print('Rejected')


def s1(string, n):
    """
    State s1 of the DFA.

    This function handles the transition from state s1. Depending on the 
    current character, it may transition to states s2, s3, s4, or accept 
    the string if it reaches the end.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if n == len(string):
        print('Accepted')
    elif string[n] == 'd':
        s2(string, n + 1)
    elif string[n] == 'c':
        s3(string, n + 1)
    elif string[n] == 'a':
        s4(string, n + 1)
    else:
        print('Rejected')


def s2(string, n):
    """
    State s2 of the DFA.

    This function handles the transition from state s2. It accepts the string 
    if it reaches the end, otherwise it rejects the string.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if n == len(string):
        print('Accepted')
    else:
        print('Rejected')


def s3(string, n):
    """
    State s3 of the DFA.

    This function handles the transition from state s3. If the current 
    character is 'a', it transitions back to state s1. If it reaches the end 
    or the character is not 'a', it rejects the string.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if n == len(string) or string[n] != 'a':
        print('Rejected')
    else:
        s1(string, n + 1)


def s4(string, n):
    """
    State s4 of the DFA.

    This function handles the transition from state s4. If the current 
    character is 'r', it transitions to state s5. If it reaches the end or 
    the character is not 'r', it rejects the string.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if n == len(string) or string[n] != 'r':
        print('Rejected')
    else:
        s5(string, n + 1)


def s5(string, n):
    """
    State s5 of the DFA.

    This function handles the transition from state s5. If the current 
    character is 'y', it transitions to state s6. If it reaches the end or 
    the character is not 'y', it rejects the string.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if n == len(string) or string[n] != 'y':
        print('Rejected')
    else:
        s6(string, n + 1)


def s6(string, n):
    """
    State s6 of the DFA.

    This function handles the transition from state s6. If the current 
    character is 'a', it transitions back to state s1. If it reaches the end 
    or the character is not 'a', it rejects the string.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if n == len(string) or string[n] != 'a':
        print('Rejected')
    else:
        s1(string, n + 1)


def s7(string, n):
    """
    State s7 of the DFA.

    This function handles the transition from state s7. If the current 
    character is 'i', it transitions to state s8. If it reaches the end or 
    the character is not 'i', it rejects the string.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if n == len(string) or string[n] != 'i':
        print('Rejected')
    else:
        s8(string, n + 1)


def s8(string, n):
    """
    State s8 of the DFA.

    This function handles the transition from state s8. If the current 
    character is 'l', it transitions back to state s1. If it reaches the end 
    or the character is not 'l', it rejects the string.

    Args:
        string (str): The input string to be parsed by the DFA.
        n (int): The current position in the string.

    Returns:
        None
    """
    if n == len(string) or string[n] != 'l':
        print('Rejected')
    else:
        s1(string, n + 1)


# List of test strings
test_strings = [
    'aa', ' ', 'and', 'a', 'aaa', 'a', 'a ', 'as', 'ann', 'aan', 'an',
    'aana', 'anaa', 'anna', 'ana', 'aanca', 'ancca', 'ancaa', 'anca',
    'annca', 'ancca', 'anarya', 'aanarya', 'anaryaa', 'annarya', 'anarrya',
    'anaryya', 'anaryaa', 'amil', 'aamil', 'amilaa', 'amila', 'ammil',
    'amiil', 'amill', 'amila', 'anaa', 'anaryaa',
]

# Process each string with the DFA
for word in test_strings:
    dfa(word, 0)
