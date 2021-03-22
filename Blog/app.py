from blog import Blog

blogs = dict() #blog_name : Blog object

MENU_PROMP = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit '

POST_TEMPLATE = '''
--- {} ---
{}
'''

def menu():
    #show the user available blogs
    # let the user make a choice
    # DO something with that choice
    # exit
    print_blogs()
    selection = input(MENU_PROMP)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMP)



def print_blogs():
    # print available blogs
    # iterate over the blogs dict
    for key, blog in blogs.items():
        print("- {}".format(blog))

def ask_create_blog():
    # ask user for blog title and their name and will create a blog
    title = input('Enter your Blog title: ') #enter title here
    author = input('Enter your name: ')
    # here add the result to blog dict
    blogs[title] = Blog(title, author)


def ask_read_blog():
    # asks for blog title and print the post
    title = input('Enter the blog title you want to read: ')
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    pass