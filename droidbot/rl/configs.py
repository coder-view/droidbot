SCREEN_H = 180
SCREEN_W = 120

INTERESTED_PERMISSIONS = [
    'ACCEPT_HANDOVER',
    'ACCESS_BACKGROUND_LOCATION',
    'ACCESS_CALL_AUDIO',
    'ACCESS_CHECKIN_PROPERTIES',
    'ACCESS_COARSE_LOCATION',
    'ACCESS_FINE_LOCATION',
    'ACCESS_LOCATION_EXTRA_COMMANDS',
    'ACCESS_MEDIA_LOCATION',
    'ACCESS_NETWORK_STATE',
    'ACCESS_NOTIFICATION_POLICY',
    'ACCESS_WIFI_STATE',
    'ACCOUNT_MANAGER',
    'ACTIVITY_RECOGNITION',
    'ADD_VOICEMAIL',
    'ANSWER_PHONE_CALLS',
    'BATTERY_STATS',
    'BIND_ACCESSIBILITY_SERVICE',
    'BIND_APPWIDGET',
    'BIND_AUTOFILL_SERVICE',
    'BIND_CALL_REDIRECTION_SERVICE',
    'BIND_CARRIER_MESSAGING_CLIENT_SERVICE',
    'BIND_CARRIER_MESSAGING_SERVICE',
    'BIND_CARRIER_SERVICES',
    'BIND_CHOOSER_TARGET_SERVICE',
    'BIND_CONDITION_PROVIDER_SERVICE',
    'BIND_CONTROLS',
    'BIND_DEVICE_ADMIN',
    'BIND_DREAM_SERVICE',
    'BIND_INCALL_SERVICE',
    'BIND_INPUT_METHOD',
    'BIND_MIDI_DEVICE_SERVICE',
    'BIND_NFC_SERVICE',
    'BIND_NOTIFICATION_LISTENER_SERVICE',
    'BIND_PRINT_SERVICE',
    'BIND_QUICK_ACCESS_WALLET_SERVICE',
    'BIND_QUICK_SETTINGS_TILE',
    'BIND_REMOTEVIEWS',
    'BIND_SCREENING_SERVICE',
    'BIND_TELECOM_CONNECTION_SERVICE',
    'BIND_TEXT_SERVICE',
    'BIND_TV_INPUT',
    'BIND_VISUAL_VOICEMAIL_SERVICE',
    'BIND_VOICE_INTERACTION',
    'BIND_VPN_SERVICE',
    'BIND_VR_LISTENER_SERVICE',
    'BIND_WALLPAPER',
    'BLUETOOTH',
    'BLUETOOTH_ADMIN',
    'BLUETOOTH_PRIVILEGED',
    'BODY_SENSORS',
    'BROADCAST_PACKAGE_REMOVED',
    'BROADCAST_SMS',
    'BROADCAST_STICKY',
    'BROADCAST_WAP_PUSH',
    'CALL_COMPANION_APP',
    'CALL_PHONE',
    'CALL_PRIVILEGED',
    'CAMERA',
    'CAPTURE_AUDIO_OUTPUT',
    'CHANGE_COMPONENT_ENABLED_STATE',
    'CHANGE_CONFIGURATION',
    'CHANGE_NETWORK_STATE',
    'CHANGE_WIFI_MULTICAST_STATE'
]


INTERESTED_BROADCASTS = [
    'AIRPLANE_MODE_CHANGED',
    'BATTERY_CHANGED',
    'BATTERY_LOW',
    'BATTERY_OKAY',
    'BOOT_COMPLETED',
    'DATE_CHANGED',
    'DEVICE_STORAGE_LOW',
    'DEVICE_STORAGE_OK',
    'INPUT_METHOD_CHANGED',
    'INSTALL_PACKAGE',
    'LOCALE_CHANGED',
    'MEDIA_EJECT',
    'MEDIA_MOUNTED',
    'MEDIA_REMOVED',
    'MEDIA_SHARED',
    'MEDIA_UNMOUNTED',
    'NEW_OUTGOING_CALL',
    'OPEN_DOCUMENT',
    'OPEN_DOCUMENT_TREE',
    'PACKAGE_ADDED',
    'PACKAGE_CHANGED',
    'PACKAGE_DATA_CLEARED',
    'PACKAGE_FIRST_LAUNCH',
    'PACKAGE_FULLY_REMOVED',
    'PACKAGE_INSTALL',
    'PACKAGE_REMOVED',
    'PACKAGE_REPLACED',
    'PACKAGE_RESTARTED',
    'PACKAGE_VERIFIED',
    'PASTE',
    'POWER_CONNECTED',
    'POWER_DISCONNECTED',
    'POWER_USAGE_SUMMARY',
    'PROVIDER_CHANGED',
    'QUICK_CLOCK',
    'REBOOT',
    'SCREEN_OFF',
    'SCREEN_ON',
    'SET_WALLPAPER',
    'SHUTDOWN',
    'TIMEZONE_CHANGED',
    'TIME_CHANGED',
    'TIME_TICK',
    'UID_REMOVED',
    'UNINSTALL_PACKAGE',
    'USER_BACKGROUND',
    'USER_FOREGROUND',
    'USER_INITIALIZE',
    'USER_PRESENT',
    'VOICE_COMMAND',
    'WALLPAPER_CHANGED',
    'WEB_SEARCH'
]

# TODO @Songhe please define this list
# A list of APIs to monitor at runtime
# Note that this list is used to represent the app's behavior
INTERESTED_APIS = [
    'android.content.Context.bindService'
]

# TODO @Songhe please define this list
# A list of sensitive APIs
# Note that this list is used to identify sensitive behaviors in the app
SENSITIVE_APIS = [
    'android.location.LocationManager.requestLocationUpdates'
]

ACTION_TYPES = [
    'gesture',
    'intent',
    'key'
]

GESTURE_TYPES = [
    'touch',
    'long_touch',
    'scroll_up',
    'scroll_down'
]

