TEST LOGIC
======

CODE
----

#. The next code is solve for test_logic:

    dict_alpha = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    def integer_to_sequence_alpha(integer):
        if integer < 1:
            raise ValueError("Number should be positive")
        sequence_alpha = ""
        while True:
            if integer > (len(dict_alpha)):
                integer, rest = divmod(integer - 1, len(dict_alpha))
                sequence_alpha = dict_alpha[rest] + sequence_alpha
            else:
                return print((dict_alpha[integer - 1]) + sequence_alpha)
