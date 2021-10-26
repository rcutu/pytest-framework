class Config:
    def __init__(self, env):

        supported_envs = ['dev', 'qa']

        if env.lower() not in supported_envs:
            raise Exception(f'{env} not in supported environments')

        self.base_url = {
            'dev': 'https://mydevenv.com',
            'qa': 'https://myqa.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]


my_config = Config('qa')
my_config_url = my_config.base_url

print(my_config_url)