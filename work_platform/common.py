"""
    Common Utility Functions
"""

def parse_skill(skill):
    return skill.split(" ")[0]

def strip_bad_character(dirty_string):
    """ 
        Removes Bad character
    """
    bad_char = ["*", "#", "$", "%"]
    return ''.join(ch for ch in dirty_string if not ch in bad_char)

def strip_lines(dirty_string):
    """
        strip Lines from string
    """
    return ''.join(str for str in dirty_string.splitlines())

