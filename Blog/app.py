blogs = dict()




def menu():
    #show the user available blogs
    # let the user make a choice
    # DO something with that choice
    # exit
    print_blogs()

def print_blogs():
    # print available blogs
    # iterate over the blogs dict
    for key, blog in blogs.items():
        print("- {}".format(blog))