import re

# Find a list of all of the names in the following string using regex.
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    return re.findall("[A-Z][a-z]+", simple_string)

# The dataset file in [assets/grades.txt](assets/grades.txt) contains a line separated list of people with
# their grade in  a class. Create a regex to generate a list of just those students who received a B in the course.
def grades():
    with open ("C:\\Users\\dmakeev\\Desktop\\grades.txt", "r") as file:
        grades = file.read()

    return [match.group(1) for match in re.finditer("([\w]+ [\w]+)(: B)", grades)]


# Consider the standard web log file in assets/logdata.txt. This file records the access a user makes when
# visiting a web page (like this one!). Each line of the log has the following items:
#
# a host (e.g., '146.204.224.152')
# a user_name (e.g., 'feest6811' note: sometimes the user name is missing!
# In this case, use '-' as the value for the username.)
# the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
# the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
#
# example_dict = {"host":"146.204.224.152",
#                 "user_name":"feest6811",
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}
def logs():
    with open("C:\\Users\\dmakeev\\Desktop\\logdata.txt", "r") as file:
        logdata = file.read()

    regex = "(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - (?P<user_name>[[\w-]+) \[(?P<time>[\d/\w:\s-]*)\] \"(?P<request>[^\"]*)\""
    return [item.groupdict() for item in re.finditer(regex, logdata)]
