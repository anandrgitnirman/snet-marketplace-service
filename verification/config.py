NETWORKS = {
    3: {
        "name": "test",
        "http_provider": "https://ropsten.infura.io",
        "ws_provider": "wss://ropsten.infura.io/ws",
        "db": {
            "DB_DRIVER": "mysql+pymysql",
            "DB_HOST": "localhost",
            "DB_USER": "unittest_root",
            "DB_PASSWORD": "unittest_pwd",
            "DB_NAME": "verification_unittest_db",
            "DB_PORT": 3306,
        },
    }
}
NETWORK_ID = 3
SLACK_HOOK = {}
REGION_NAME = "us-east-2"

JUMIO_BASE_URL = "https://netverify.com/api/v4"
JUMIO_INITIATE_URL = f"{JUMIO_BASE_URL}/initiate"
JUMIO_SUBMIT_URL = ""
DAPP_POST_JUMIO_URL = ""
JUMIO_CALLBACK_URL = ""
JUMIO_WORKFLOW_ID = 200
JUMIO_API_TOKEN_SSM_KEY = ""
JUMIO_API_SECRET_SSM_KEY = ""
ALLOWED_VERIFICATION_REQUESTS = 2

VERIFIED_MAIL_DOMAIN = ["allowed.io"]

REGISTRY_ARN = {
    "ORG_VERIFICATION": ""
}
SLACK_CHANNEL_FOR_APPROVAL_TEAM = ""
SIGNING_SECRET = ""
STAGING_URL = ""
ALLOWED_SLACK_CHANNEL_ID = ["dummy_channel_id"]
ALLOWED_SLACK_USER = ['dummy_name']
INDIVIDUAL_API_ENDPOINT = ""
SLACK_APPROVAL_CHANNEL_URL = ""
MAX_INDIVIDUAL_SLACK_LISTING = 5
SLACK_APPROVAL_OAUTH_ACCESS_TOKEN = ""
