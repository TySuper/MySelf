dsm_accessdb_v1={
    "config": {
        "default_password": "f2aae6e668b0fed6bb02266d09694448",
        "email_config": {
            "crypto": "normal",
            "email": 0,
            "encrypt_password": "d1489f105c9fa64c0b6db3ee51b8d6db",
            "name": 0,
            "port": 0,
            "server": 0,
            "username": 0
        },
        "password_fail_limit": 5,
        "password_limit_expire": 24,
        "password_method": "random"
    },
    "debug": {
        "is_image_auth": 0
    },
    "rights": {},
    "users": {
        "admin": {
            "email": "hanbo@xitcorp.com",
            "first_login": "false",
            "last_update": 12,
            "last_update_time_for_password": 1591325102,
            "level": "7",
            "limit_expire": 1591771115,
            "name": "hanbo",
            "password": "7753becd791f8df265cb9ef297ddf38c",
            "permissions": {},
            "phone": "17721965910",
            "pw_fail_cnt": 0,
            "rights": [],
            "role": "administrator",
            "status": "limited",
            "username": "admin"
        }
    },
    "version": 1
}


print(type(dsm_accessdb_v1))
print(dsm_accessdb_v1['users']['admin']["status"])
dsm_accessdb_v1['users']['admin']["status"] = "1"
print(dsm_accessdb_v1['users']['admin']["status"])



