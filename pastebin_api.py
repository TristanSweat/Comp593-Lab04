import requests
# Request a new PasteBin paste

def post_new_paste(title, body_text, expiration='10M', listed=True):
    """
    Posts a new paste to PasteBin

    :param title: Paste title
    :param body_text: Paste Body Text
    :param expiration: Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1YR)
    :param listed: Whether paste is publicly listed (True) or not (False)
    :returns: URL of new paste, if successful. Otherwise None.
    """
    print(f'Posting a new Paste to PasteBin...', end='')

    p = {
        'api_dev_key': 'fJq6mShvYCt0Os5Eq7t8IKSVIErjdgeo',
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_past_name': title,
        'api_paste_private': 0 if listed else 1,
        'api_paste_expire_date': expiration 
    }
    paste_url = "https://pastebin.com/api/api_post.php" 
    resp_msg = requests.post(paste_url, data=p)

    if resp_msg.status_code == requests.codes.ok:
        print('success')
        return resp_msg.text
    else: 
        print('failure')
        print(f'Status code: {resp_msg.status_code}, Error reason: {resp_msg.reason}')
        return None 