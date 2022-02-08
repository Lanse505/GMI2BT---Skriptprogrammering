import util

if __name__ == '__main__':
    api_key = util.handleAPIKey()
    while True:
        util.runMainLoop(api_key)
