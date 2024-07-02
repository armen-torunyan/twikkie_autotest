class Config:
    def __init__(self, env, api, browser):
        self.base_url = {
            'qa': 'http://172.105.53.207'
        }[env]

        self.admin_port = {
            'qa': ''
        }[env]

        self.api_url = {
            'api_env': 'SOME URI FOR API',
        }[api]

        self.browser = {
            'api': 'api',
            'chrome': 'chrome',
            'firefox': 'firefox',
        }[browser]