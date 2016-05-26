from pusher import Pusher


def includeme(config):
    settings = config.get_settings()

    app_id = str(settings['pusher.app_id'])
    key = settings['pusher.key']
    secret = settings['pusher.secret']
    host = settings['pusher.host']
    #port = settings.get('pusher.port',80)
    config.registry.pusher = Pusher(app_id, key, secret,host=host)
