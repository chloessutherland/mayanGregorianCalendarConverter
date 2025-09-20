from date import *


# Create a string that formats a GregorianDate object into a human-readable date: ##/##/####
def format_gregorian(gregorian):
    format_string = str(gregorian.month) + "/" + str(gregorian.day) + "/"
    # Format for BC
    if gregorian.year < 0:
        format_string += str(abs(gregorian.year)) + " BC"
    # Format for AD
    else:
        format_string += str(gregorian.year)
    return format_string


# Create a string that formats a MayaDate object into a human-readable date: [baktuns].[katuns].[tuns].[winals].[kins]
def format_mayan(mayan):
    return (
        str(mayan.baktuns)
        + "."
        + str(mayan.katuns)
        + "."
        + str(mayan.tuns)
        + "."
        + str(mayan.winals)
        + "."
        + str(mayan.kins)
    )
