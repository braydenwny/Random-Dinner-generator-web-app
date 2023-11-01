from website import create_app

app = create_app()

#if __name__ == '__main__':         Do not push to git for deployment
 #   app.run(debug=False)