from RedditReader import Subreddit


def reddit(content):
    out = []
    args = content.split(' ')
    if len(args) == 1:
        key = 'memes'
        meme = Subreddit(key)
        meme.get_random()
        url = meme.url
        title = meme.title
        out.append(url)
        out.append(title)
        return out

    key = args[1]
    meme = Subreddit(key)
    meme.get_random()
    url = meme.url
    title = meme.title
    out.append(url)
    out.append(title)
    return out
