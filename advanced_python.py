
from string import Template

def main():
    # Usual string formtting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)

    # template with placeholder
    templ = Template("You're watching ${title} by ${author}")
    
    # substitute method with keyword arguments
    str2 = templ.substitute(title = "Advanced Python", author = "Joe Marini")
    print(str2)

    # substitute method with dictionary
    data = {
        "author" : "Joe Marini",
        "title" : "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3)


if __name__ == "__main__":
    main()