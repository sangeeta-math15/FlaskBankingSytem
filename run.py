# from banking import create_app
#
# banking = create_app()
#
# if __name__ == '__main__':
#     banking.run(debug=True)

# from banking import create_app
#
# banking = create_app()
#
# @banking.route('/')
# def home():
#     return 'Hello, Flask!'
#
# if __name__ == '__main__':
#     banking.run(debug=True)

from banking import create_app
app = create_app()

if __name__ == '__main__':
    # with banking.app_context():
    #     print(banking.url_map)
    app.run(debug=True)
