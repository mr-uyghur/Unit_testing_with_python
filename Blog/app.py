blogs = dict()

MENU_PROMP = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit '


def menu():
    #show the user available blogs
    # let the user make a choice
    # DO something with that choice
    # exit
    print_blogs()
    selection = input(MENU_PROMP)

def print_blogs():
    # print available blogs
    # iterate over the blogs dict
    for key, blog in blogs.items():
        print("- {}".format(blog))