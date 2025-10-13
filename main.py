from flask import Flask, render_template

app = Flask(__name__)

# APK data - You can easily add/remove apps here
apk_list = [
    {
        "name": "FB Lite 2",
        "description": "Lightweight Facebook client",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/1st-Fb-Lite/Lite.2.apk"
    },
    {
        "name": "FB Lite 3",
        "description": "Enhanced Facebook experience",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/2nd-Fb-Lite/Lite.3.apk"
    },
    {
        "name": "FB Lite 4",
        "description": "Updated Facebook version",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/3rd-Fb-Lite/Lite.4.apk"
    },
    {
        "name": "FB Lite 5",
        "description": "Latest Facebook lite",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/4th-Fb-Lite/Lite.5.apk"
    },
    {
        "name": "FB Lite 6",
        "description": "Premium Facebook mod",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/5th-Fb-Lite/Lite.6.apk"
    },
    {
        "name": "FB Lite 7",
        "description": "Advanced features included",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/6th-Fb-Lite/Lite.7.apk"
    },
    {
        "name": "FB Lite 8",
        "description": "Optimized performance",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/7th-Fb-Lite/Lite.8.apk"
    },
    {
        "name": "FB Lite 9",
        "description": "New UI improvements",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/8th-Fb-Lite/Lite.9.apk"
    },
    {
        "name": "FB Lite 10",
        "description": "Enhanced stability",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/9th-Fb-Lite/Lite.10.apk"
    },
    {
        "name": "FB Lite 11",
        "description": "Latest release version",
        "category": "Social",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/10th-Fb-Lite/Lite.11.apk"
    },
    {
        "name": "XPAK Installer",
        "description": "Unlocked AdsFree",
        "category": "App Installer",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/XAPK/XAPK_Installer.apk"
    },
    {
        "name": "Multispace",
        "description": "AdsFree Unlocked",
        "category": "App Cloner",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/Multispace/dualspace.apk"
    },
    {
        "name": "Termux",
        "description": "Latest Termux version",
        "category": "Programing",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/termux/com.termux_1020.apk"
    },
    {
        "name": "SafeUm Gold",
        "description": "Safeum Premium App",
        "category": "Messaging",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/Safeum/SafeUm_Gold.apk"
    },
    {
        "name": "SafeUm VIP",
        "description": "Safeum Blue Unlocked",
        "category": "Messaging",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/Safeum-v2/SafeUm_Vip.apk"
    },
    {
        "name": "2nr Premium",
        "description": "Unlocked Version",
        "category": "Messaging",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/2nr-Premium/2nr_premium.xapk"
    },
    {
        "name": "2nd Line",
        "description": "Moded XAPK",
        "category": "Messaging",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/2ndLine/2ndLine.xapk"
    },
    {
        "name": "Sony LIV",
        "description": "Premium MOD Ads Free",
        "category": "Entertainment",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/Sony-LIV/Sony_LIV_Addsfree.apk"
    },
    {
        "name": "Youtube Premium",
        "description": "Ads Free Version",
        "category": "Media & Video",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/Youtube_Premium/YouTube-Premium.apk"
    },
    {
        "name": "Netflix",
        "description": "Premium Unlocked",
        "category": "Entertainment",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/Netflix/Netflix.apk"
    },
    {
        "name": "Lat VPN",
        "description": "Updated MOD",
        "category": "VPN & Proxy",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/LAT/VPN_Lat.apk"
    },
    {
        "name": "Touch VPN",
        "description": "Premium Version Unlocked",
        "category": "VPN & Proxy",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/Touch-VPN/touchvpn-MOD.apk"
    },
    {
        "name": "Secure VPN",
        "description": "Ads Free Experience",
        "category": "VPN & Proxy",
        "url": "https://github.com/Tabbu-Arain/10-Colour-FB-Lite/releases/download/Secure-VPN/Secure-VPN.apk"
    },
]

@app.route('/')
def home():
    return render_template('index.html', apk_list=apk_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
