TC_ACCOUNT_ID = '31563997'
TC_API_KEY = 'ec92d54b004a404f83bcb17fb8bdebe22d80a0c1a8ff41f4b82f64af2d92258f'
TC_API_SECRET = '52548797670b898d578163d7fd32899776424a7dae42f76835a402c28de06ffe7afd65ba9b432296f84e50865a7164a57ecc0ce56e577a2166dfd146a966392dc207892dfe83776f1c71eb2a00d50c71c45b3d675d68f44024fd6682cc46c4fa0793e440'
BASE_URL = 'https://api.3commas.io'

API_KEY = 'FLgpsOsl9xuz_DD1HK194X0xALO236Y0OFY4Twj4'
SECRET_KEY = 'vVwkLvohN5KHI5UcyKn1knqnwR-zcqkJUeT48h24'
SUB_ACCOUNT = '3commas'
PAIRS_BLACKLIST = ['DMG-PERP', 'BRZ-PERP', 'PERP/USD', 'SRN-PERP', 'PRIV-PERP', 'SHIB-PERP']
MAX_OPEN_POSITIONS = 10
FUNDS_USAGE = 0.9
TF = 15  # Timeframe - always in minutes - Greater than 1 minute, less than 1 day.
ADX_LENGTH = 14
EMA_LENGTH = 20
EMA_SMOOTHING = 3
DEAL_BOT_RATIO_WARNING = 0.75
CLOSE_DEALS_WITH_BOT = False  # WARNING: Will close all open positions with no equivalent enabled bots.
EARLY_CLOSE = True
CLOSE_DEALS = True  # Allow bot to close deals on opposite signals. Use False to manually rescue red bags.

# 3Commas Bot Settings
BASE_ORDER_VOLUME = 10 #IN USD
TAKE_PROFIT = 0.75
SAFETY_ORDER_VOLUME = 12.5
MARTINGALE_VOLUME_COEFFICIENT = 1.2
MARTINGALE_STEP_COEFFICIENT = 1.55
MAX_SAFETY_ORDERS = 10
ACTIVE_SAFETY_ORDERS_COUNT = 5
SAFETY_ORDER_STEP_PERCENTAGE = 0.21
LEVERAGE_CUSTOM_VALUE = 3

# Used When Updating Bot Settings
STOP_LOSS_TYPE = 'stop_loss_and_disable_bot'  # or stop_loss
STOP_LOSS_PERCENTAGE = 0
STOP_LOSS_TIMEOUT_ENABLED = False
STOP_LOSS_TIMEOUT_IN_SECONDS = 300
START_ORDER_TYPE = 'market'