import logging
import json
import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ========== إعدادات البوت ==========
BOT_TOKEN = "7974588760:AAGsLqpJW-gHz0bEBUDrfQo5EVdsVBCJc_g"
CHANNEL_LINK = "https://t.me/dytfonvvhjmbv"
CHANNEL_USERNAME = "@dytfonvvhjmbv"
ADMIN_ID = 8096873389

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return []

def save_user(user_id):
    users = load_users()
    if user_id not in users:
        users.append(user_id)
        with open(USERS_FILE, "w") as f:
            json.dump(users, f)

# ========== الأرقام ==========
NUMBERS = {
    "whatsapp": {
        "germany": [
            "+4915201234501","+4915209876502","+4917612345603","+4915754321704",
            "+4916098765805","+4917523456706","+4915687654307","+4916034567808",
            "+4917845678909","+4915290123410","+4916745678211","+4917312345612",
            "+4915867890113","+4916423456714","+4917956789015","+4915334567816",
            "+4916789012317","+4917456789118","+4915612345619","+4916123789020",
            "+4917890123421","+4915478901222","+4916234567823","+4917012345624",
            "+4915890234525","+4916567890126","+4917234560827","+4915345678928",
            "+4916901234529","+4917678901230","+4915456789031","+4916012345732",
            "+4917789012533","+4915523456834","+4916290123435","+4917067890136",
            "+4915734560937","+4916845678238","+4917401234539","+4915268901340",
            "+4916756789041","+4917323456742","+4915890678143","+4916467890344",
            "+4917034567845","+4915712346046","+4916279012347","+4917846789148",
            "+4915423456749","+4916990123450",
        ],
        "russia": [
            "+79161234501","+79269876502","+79031234603","+79154321704",
            "+79261234805","+79372345706","+79483456807","+79594567908",
            "+79105678909","+79216789010","+79327890111","+79438901212",
            "+79549012313","+79650123414","+79761234515","+79872345616",
            "+79983456717","+79094567818","+79105678919","+79216789020",
            "+79327891121","+79438902222","+79549013323","+79650124424",
            "+79761235525","+79872346626","+79983457727","+79094568828",
            "+79101239929","+79212340030","+79323451131","+79434562232",
            "+79545673333","+79656784434","+79767895535","+79878906636",
            "+79989017737","+79090128838","+79101239939","+79212341040",
            "+79323452141","+79434563242","+79545674343","+79656785444",
            "+79767896545","+79878907646","+79989018747","+79090129848",
            "+79101230949","+79212342050",
        ],
        "zimbabwe": [
            "+2637712345601","+2637823456702","+2637934567803","+2638045678904",
            "+2638156789005","+2638267890106","+2638378901207","+2638489012308",
            "+2638590123409","+2637701234510","+2637812345611","+2637923456712",
            "+2638034567813","+2638145678914","+2638256789015","+2638367890116",
            "+2638478901217","+2638589012318","+2638690123419","+2637702345520",
            "+2637813456621","+2637924567722","+2638035678823","+2638146789924",
            "+2638257890025","+2638368901126","+2638479012227","+2638580123328",
            "+2638691234429","+2637703456530","+2637814567631","+2637925678732",
            "+2638036789833","+2638147890934","+2638258901035","+2638369012136",
            "+2638470123237","+2638581234338","+2638692345439","+2637704567540",
            "+2637815678641","+2637926789742","+2638037890843","+2638148901944",
            "+2638259012045","+2638360123146","+2638471234247","+2638582345348",
            "+2638693456449","+2637705678550",
        ],
        "venezuela": [
            "+584121234501","+584129876502","+584141234603","+584124321704",
            "+584161234805","+584122345706","+584143456807","+584164567908",
            "+584125678909","+584146789010","+584127890111","+584148901212",
            "+584129012313","+584140123414","+584161234515","+584122345616",
            "+584143456717","+584164567818","+584125678919","+584146789020",
            "+584127891121","+584148902222","+584129013323","+584140124424",
            "+584161235525","+584122346626","+584143457727","+584164568828",
            "+584125679929","+584146780030","+584127891131","+584148902232",
            "+584129013333","+584140124434","+584161235535","+584122346636",
            "+584143457737","+584164568838","+584125679939","+584146780040",
            "+584127891141","+584148902242","+584129013343","+584140124444",
            "+584161235545","+584122346646","+584143457747","+584164568848",
            "+584125679949","+584146780050",
        ],
        "zambia": [
            "+260971234501","+260962345602","+260953456703","+260974567804",
            "+260965678905","+260956789006","+260977890107","+260968901208",
            "+260959012309","+260970123410","+260961234511","+260952345612",
            "+260973456713","+260964567814","+260955678915","+260976789016",
            "+260967890117","+260958901218","+260979012319","+260960123420",
            "+260951234521","+260972345622","+260963456723","+260954567824",
            "+260975678925","+260966789026","+260957890127","+260978901228",
            "+260969012329","+260950123430","+260971234531","+260962345632",
            "+260953456733","+260974567834","+260965678935","+260956789036",
            "+260977890137","+260968901238","+260959012339","+260970123440",
            "+260961234541","+260952345642","+260973456743","+260964567844",
            "+260955678945","+260976789046","+260967890147","+260958901248",
            "+260979012349","+260960123450",
        ],
        "sudan": [
            "+249911234501","+249922345602","+249933456703","+249914567804",
            "+249925678905","+249936789006","+249917890107","+249928901208",
            "+249939012309","+249910123410","+249921234511","+249932345612",
            "+249913456713","+249924567814","+249935678915","+249916789016",
            "+249927890117","+249938901218","+249919012319","+249920123420",
            "+249931234521","+249912345622","+249923456723","+249934567824",
            "+249915678925","+249926789026","+249937890127","+249918901228",
            "+249929012329","+249930123430","+249911234531","+249922345632",
            "+249933456733","+249914567834","+249925678935","+249936789036",
            "+249917890137","+249928901238","+249939012339","+249910123440",
            "+249921234541","+249932345642","+249913456743","+249924567844",
            "+249935678945","+249916789046","+249927890147","+249938901248",
            "+249919012349","+249920123450",
        ],
        "saudi": [
            "+966501234501","+966512345602","+966523456703","+966534567804",
            "+966545678905","+966556789006","+966567890107","+966578901208",
            "+966589012309","+966501123410","+966512234511","+966523345612",
            "+966534456713","+966545567814","+966556678915","+966567789016",
            "+966578890117","+966589901218","+966501012319","+966512123420",
            "+966523234521","+966534345622","+966545456723","+966556567824",
            "+966567678925","+966578789026","+966589890127","+966501901228",
            "+966512012329","+966523123430","+966534234531","+966545345632",
            "+966556456733","+966567567834","+966578678935","+966589789036",
            "+966501890137","+966512901238","+966523012339","+966534123440",
            "+966545234541","+966556345642","+966567456743","+966578567844",
            "+966589678945","+966501789046","+966512890147","+966523901248",
            "+966534012349","+966545123450",
        ],
        "yemen": [
            "+967711234501","+967712345602","+967713456703","+967714567804",
            "+967715678905","+967716789006","+967717890107","+967718901208",
            "+967719012309","+967711123410","+967712234511","+967713345612",
            "+967714456713","+967715567814","+967716678915","+967717789016",
            "+967718890117","+967719901218","+967711012319","+967712123420",
            "+967713234521","+967714345622","+967715456723","+967716567824",
            "+967717678925","+967718789026","+967719890127","+967711901228",
            "+967712012329","+967713123430","+967714234531","+967715345632",
            "+967716456733","+967717567834","+967718678935","+967719789036",
            "+967711890137","+967712901238","+967713012339","+967714123440",
            "+967715234541","+967716345642","+967717456743","+967718567844",
            "+967719678945","+967711789046","+967712890147","+967713901248",
            "+967714012349","+967715123450",
        ],
    },
    "instagram": {
        "germany": [
            "+4915201234601","+4915209876702","+4917612345803","+4915754321904",
            "+4916098766005","+4917523456206","+4915687654407","+4916034567908",
            "+4917845679009","+4915290123510","+4916745678311","+4917312345712",
            "+4915867890213","+4916423456814","+4917956789115","+4915334567916",
            "+4916789012417","+4917456789218","+4915612345719","+4916123789120",
            "+4917890123521","+4915478901322","+4916234567923","+4917012345724",
            "+4915890234625","+4916567890226","+4917234560927","+4915345679028",
            "+4916901234629","+4917678901330","+4915456789131","+4916012345832",
            "+4917789012633","+4915523456934","+4916290123535","+4917067890236",
            "+4915734561037","+4916845678338","+4917401234639","+4915268901440",
            "+4916756789141","+4917323456842","+4915890678243","+4916467890444",
            "+4917034567945","+4915712346146","+4916279012447","+4917846789248",
            "+4915423456949","+4916990123550",
        ],
        "russia": [
            "+79161234601","+79269876702","+79031234803","+79154321904",
            "+79261235005","+79372345906","+79483456107","+79594567208",
            "+79105678309","+79216789410","+79327890511","+79438901612",
            "+79549012713","+79650123814","+79761234915","+79872346016",
            "+79983457117","+79094568218","+79105679319","+79216790420",
            "+79327801521","+79438912622","+79549023723","+79650134824",
            "+79761245925","+79872357026","+79983468127","+79094579228",
            "+79101290329","+79212301430","+79323412531","+79434523632",
            "+79545634733","+79656745834","+79767856935","+79878968036",
            "+79989079137","+79090180238","+79101291339","+79212302440",
            "+79323413541","+79434524642","+79545635743","+79656746844",
            "+79767857945","+79878969046","+79989080147","+79090191248",
            "+79101202349","+79212313450",
        ],
        "zimbabwe": [
            "+2637712345701","+2637823456802","+2637934567903","+2638045679004",
            "+2638156789105","+2638267890206","+2638378901307","+2638489012408",
            "+2638590123509","+2637701234610","+2637812345711","+2637923456812",
            "+2638034567913","+2638145679014","+2638256789115","+2638367890216",
            "+2638478901317","+2638589012418","+2638690123519","+2637702345620",
            "+2637813456721","+2637924567822","+2638035678923","+2638146790024",
            "+2638257890125","+2638368901226","+2638479012327","+2638580123428",
            "+2638691234529","+2637703456630","+2637814567731","+2637925678832",
            "+2638036789933","+2638147891034","+2638258901135","+2638369012236",
            "+2638470123337","+2638581234438","+2638692345539","+2637704567640",
            "+2637815678741","+2637926789842","+2638037890943","+2638148902044",
            "+2638259012145","+2638360123246","+2638471234347","+2638582345448",
            "+2638693456549","+2637705678650",
        ],
        "venezuela": [
            "+584121234601","+584129876702","+584141234803","+584124321904",
            "+584161235005","+584122345906","+584143456107","+584164567208",
            "+584125678309","+584146789410","+584127890511","+584148901612",
            "+584129012713","+584140123814","+584161234915","+584122345016",
            "+584143456117","+584164567218","+584125678319","+584146789420",
            "+584127890521","+584148901622","+584129012723","+584140123824",
            "+584161234925","+584122345026","+584143456127","+584164567228",
            "+584125678329","+584146789430","+584127890531","+584148901632",
            "+584129012733","+584140123834","+584161234935","+584122345036",
            "+584143456137","+584164567238","+584125678339","+584146789440",
            "+584127890541","+584148901642","+584129012743","+584140123844",
            "+584161234945","+584122345046","+584143456147","+584164567248",
            "+584125678349","+584146789450",
        ],
        "zambia": [
            "+260971234601","+260962345702","+260953456803","+260974567904",
            "+260965679005","+260956789106","+260977890207","+260968901308",
            "+260959012409","+260970123510","+260961234611","+260952345712",
            "+260973456813","+260964567914","+260955679015","+260976789116",
            "+260967890217","+260958901318","+260979012419","+260960123520",
            "+260951234621","+260972345722","+260963456823","+260954567924",
            "+260975679025","+260966789126","+260957890227","+260978901328",
            "+260969012429","+260950123530","+260971234631","+260962345732",
            "+260953456833","+260974567934","+260965679035","+260956789136",
            "+260977890237","+260968901338","+260959012439","+260970123540",
            "+260961234641","+260952345742","+260973456843","+260964567944",
            "+260955679045","+260976789146","+260967890247","+260958901348",
            "+260979012449","+260960123550",
        ],
        "sudan": [
            "+249911234601","+249922345702","+249933456803","+249914567904",
            "+249925679005","+249936789106","+249917890207","+249928901308",
            "+249939012409","+249910123510","+249921234611","+249932345712",
            "+249913456813","+249924567914","+249935679015","+249916789116",
            "+249927890217","+249938901318","+249919012419","+249920123520",
            "+249931234621","+249912345722","+249923456823","+249934567924",
            "+249915679025","+249926789126","+249937890227","+249918901328",
            "+249929012429","+249930123530","+249911234631","+249922345732",
            "+249933456833","+249914567934","+249925679035","+249936789136",
            "+249917890237","+249928901338","+249939012439","+249910123540",
            "+249921234641","+249932345742","+249913456843","+249924567944",
            "+249935679045","+249916789146","+249927890247","+249938901348",
            "+249919012449","+249920123550",
        ],
        "saudi": [
            "+966501234601","+966512345702","+966523456803","+966534567904",
            "+966545679005","+966556789106","+966567890207","+966578901308",
            "+966589012409","+966501123510","+966512234611","+966523345712",
            "+966534456813","+966545567914","+966556679015","+966567789116",
            "+966578890217","+966589901318","+966501012419","+966512123520",
            "+966523234621","+966534345722","+966545456823","+966556567924",
            "+966567679025","+966578789126","+966589890227","+966501901328",
            "+966512012429","+966523123530","+966534234631","+966545345732",
            "+966556456833","+966567567934","+966578679035","+966589789136",
            "+966501890237","+966512901338","+966523012439","+966534123540",
            "+966545234641","+966556345742","+966567456843","+966578567944",
            "+966589679045","+966501789146","+966512890247","+966523901348",
            "+966534012449","+966545123550",
        ],
        "yemen": [
            "+967711234601","+967712345702","+967713456803","+967714567904",
            "+967715679005","+967716789106","+967717890207","+967718901308",
            "+967719012409","+967711123510","+967712234611","+967713345712",
            "+967714456813","+967715567914","+967716679015","+967717789116",
            "+967718890217","+967719901318","+967711012419","+967712123520",
            "+967713234621","+967714345722","+967715456823","+967716567924",
            "+967717679025","+967718789126","+967719890227","+967711901328",
            "+967712012429","+967713123530","+967714234631","+967715345732",
            "+967716456833","+967717567934","+967718679035","+967719789136",
            "+967711890237","+967712901338","+967713012439","+967714123540",
            "+967715234641","+967716345742","+967717456843","+967718567944",
            "+967719679045","+967711789146","+967712890247","+967713901348",
            "+967714012449","+967715123550",
        ],
    }
}

# ========== النصوص ==========
TEXTS = {
    "ar": {
        "choose_lang": "🌍 *أهلاً بك في البوت!*\n\nيرجى اختيار لغتك:",
        "subscribe_required": "📢 *يجب الاشتراك أولاً!*\n\nاشترك في القناة الرسمية للبوت ثم اضغط تحقق ✅",
        "subscribe_btn": "📢 اشترك في القناة",
        "verify_btn": "✅ تحقق من الاشتراك",
        "not_subscribed": "❌ لم تشترك بعد!\nيرجى الاشتراك في القناة ثم اضغط تحقق.",
        "subscribed_ok": "✅ تم التحقق! مرحباً بك 🎉",
        "choose_service": "🛠 *اختر الخدمة المطلوبة:*",
        "whatsapp": "💬 واتساب",
        "instagram": "📸 انستقرام",
        "choose_country": (
            "🌍 *اختر الدولة:*\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "germany":   "🇩🇪  ألمانيا",
        "russia":    "🇷🇺  روسيا",
        "zimbabwe":  "🇿🇼  زيمبابوي",
        "venezuela": "🇻🇪  فنزويلا",
        "zambia":    "🇿🇲  زامبيا",
        "sudan":     "🇸🇩  السودان",
        "saudi":     "🇸🇦  السعودية",
        "yemen":     "🇾🇪  اليمن",
        "your_number": (
            "┌─────────────────────┐\n"
            "│   📱 *رقمك الخاص*   │\n"
            "├─────────────────────┤\n"
            "│  `{number}`  │\n"
            "├─────────────────────┤\n"
            "│ 🌍 الدولة: {country}│\n"
            "│ 📱 الخدمة: {service}│\n"
            "└─────────────────────┘\n"
            "⏳ _سيصلك الكود عند طلبه_"
        ),
        "change_number": "🔄 تغيير الرقم",
        "change_country": "🌍 تغيير الدولة",
        "request_code": "📨 طلب الكود",
        "code_msg": (
            "┌──────────────────────┐\n"
            "│    🔐 *كود التحقق*   │\n"
            "├──────────────────────┤\n"
            "│                      │\n"
            "│  ❰ `{code}` ❱        │\n"
            "│                      │\n"
            "├──────────────────────┤\n"
            "│ 📞 *{number}*        │\n"
            "│ 🌍 {country}         │\n"
            "│ 📱 {service}         │\n"
            "├──────────────────────┤\n"
            "│ ⏱ صالح 5 دقائق      │\n"
            "│ 🔒 لا تشاركه أحداً  │\n"
            "└──────────────────────┘\n"
            "⚡️ *أدخله في التطبيق الآن!*"
        ),
        "back": "🔙 رجوع",
    },
    "en": {
        "choose_lang": "🌍 *Welcome to the Bot!*\n\nPlease choose your language:",
        "subscribe_required": "📢 *You must subscribe first!*\n\nSubscribe to the official channel then press Verify ✅",
        "subscribe_btn": "📢 Subscribe to Channel",
        "verify_btn": "✅ Verify Subscription",
        "not_subscribed": "❌ Not subscribed yet!\nPlease subscribe then press Verify.",
        "subscribed_ok": "✅ Verified! Welcome 🎉",
        "choose_service": "🛠 *Choose the required service:*",
        "whatsapp": "💬 WhatsApp",
        "instagram": "📸 Instagram",
        "choose_country": (
            "🌍 *Choose a Country:*\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "germany":   "🇩🇪  Germany",
        "russia":    "🇷🇺  Russia",
        "zimbabwe":  "🇿🇼  Zimbabwe",
        "venezuela": "🇻🇪  Venezuela",
        "zambia":    "🇿🇲  Zambia",
        "sudan":     "🇸🇩  Sudan",
        "saudi":     "🇸🇦  Saudi Arabia",
        "yemen":     "🇾🇪  Yemen",
        "your_number": (
            "┌─────────────────────┐\n"
            "│   📱 *Your Number*  │\n"
            "├─────────────────────┤\n"
            "│  `{number}`  │\n"
            "├─────────────────────┤\n"
            "│ 🌍 Country: {country}│\n"
            "│ 📱 Service: {service}│\n"
            "└─────────────────────┘\n"
            "⏳ _Code will be sent on request_"
        ),
        "change_number": "🔄 Change Number",
        "change_country": "🌍 Change Country",
        "request_code": "📨 Request Code",
        "code_msg": (
            "┌──────────────────────┐\n"
            "│  🔐 *Verify Code*    │\n"
            "├──────────────────────┤\n"
            "│                      │\n"
            "│  ❰ `{code}` ❱        │\n"
            "│                      │\n"
            "├──────────────────────┤\n"
            "│ 📞 *{number}*        │\n"
            "│ 🌍 {country}         │\n"
            "│ 📱 {service}         │\n"
            "├──────────────────────┤\n"
            "│ ⏱ Valid 5 minutes    │\n"
            "│ 🔒 Don't share it    │\n"
            "└──────────────────────┘\n"
            "⚡️ *Enter it in the app now!*"
        ),
        "back": "🔙 Back",
    },
    "hi": {
        "choose_lang": "🌍 *बॉट में आपका स्वागत है!*\n\nकृपया अपनी भाषा चुनें:",
        "subscribe_required": "📢 *पहले सब्सक्राइब करें!*\n\nचैनल सब्सक्राइब करें फिर Verify दबाएं ✅",
        "subscribe_btn": "📢 चैनल सब्सक्राइब करें",
        "verify_btn": "✅ वेरीफाई करें",
        "not_subscribed": "❌ सब्सक्राइब नहीं किया!\nचैनल सब्सक्राइब करें फिर Verify दबाएं।",
        "subscribed_ok": "✅ वेरीफाई हो गया! स्वागत है 🎉",
        "choose_service": "🛠 *सेवा चुनें:*",
        "whatsapp": "💬 WhatsApp",
        "instagram": "📸 Instagram",
        "choose_country": (
            "🌍 *देश चुनें:*\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        "germany":   "🇩🇪  जर्मनी",
        "russia":    "🇷🇺  रूस",
        "zimbabwe":  "🇿🇼  जिम्बाब्वे",
        "venezuela": "🇻🇪  वेनेजुएला",
        "zambia":    "🇿🇲  जाम्बिया",
        "sudan":     "🇸🇩  सूडान",
        "saudi":     "🇸🇦  सऊदी अरब",
        "yemen":     "🇾🇪  यमन",
        "your_number": (
            "┌─────────────────────┐\n"
            "│  📱 *आपका नंबर*     │\n"
            "├─────────────────────┤\n"
            "│  `{number}`  │\n"
            "├─────────────────────┤\n"
            "│ 🌍 देश: {country}   │\n"
            "│ 📱 सेवा: {service}  │\n"
            "└─────────────────────┘\n"
            "⏳ _कोड मांगने पर मिलेगा_"
        ),
        "change_number": "🔄 नंबर बदलें",
        "change_country": "🌍 देश बदलें",
        "request_code": "📨 कोड मांगें",
        "code_msg": (
            "┌──────────────────────┐\n"
            "│  🔐 *सत्यापन कोड*   │\n"
            "├──────────────────────┤\n"
            "│                      │\n"
            "│  ❰ `{code}` ❱        │\n"
            "│                      │\n"
            "├──────────────────────┤\n"
            "│ 📞 *{number}*        │\n"
            "│ 🌍 {country}         │\n"
            "│ 📱 {service}         │\n"
            "├──────────────────────┤\n"
            "│ ⏱ 5 मिनट वैध        │\n"
            "│ 🔒 किसी को न दें    │\n"
            "└──────────────────────┘\n"
            "⚡️ *अभी ऐप में दर्ज करें!*"
        ),
        "back": "🔙 वापस",
    }
}

COUNTRIES = ["germany","russia","zimbabwe","venezuela","zambia","sudan","saudi","yemen"]

def get_lang(context): return context.user_data.get("lang","ar")

def t(context, key): return TEXTS[get_lang(context)].get(key, key)

def country_keyboard(lang):
    tx = TEXTS[lang]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(tx["germany"],   callback_data="country_germany"),
         InlineKeyboardButton(tx["russia"],    callback_data="country_russia")],
        [InlineKeyboardButton(tx["saudi"],     callback_data="country_saudi"),
         InlineKeyboardButton(tx["yemen"],     callback_data="country_yemen")],
        [InlineKeyboardButton(tx["sudan"],     callback_data="country_sudan"),
         InlineKeyboardButton(tx["venezuela"], callback_data="country_venezuela")],
        [InlineKeyboardButton(tx["zimbabwe"],  callback_data="country_zimbabwe"),
         InlineKeyboardButton(tx["zambia"],    callback_data="country_zambia")],
    ])

# ========== /start ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update.message.from_user.id)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🇸🇦  العربية", callback_data="lang_ar")],
        [InlineKeyboardButton("🇬🇧  English", callback_data="lang_en")],
        [InlineKeyboardButton("🇮🇳  हिन्दी",  callback_data="lang_hi")],
    ])
    await update.message.reply_text(TEXTS["ar"]["choose_lang"], parse_mode="Markdown", reply_markup=keyboard)

# ========== broadcast ==========
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != ADMIN_ID:
        return
    msg = " ".join(context.args)
    if not msg:
        await update.message.reply_text("📝 الاستخدام:\n`/broadcast رسالتك هنا`", parse_mode="Markdown")
        return
    users = load_users()
    await update.message.reply_text(f"⏳ جاري الإرسال لـ *{len(users)}* مستخدم...", parse_mode="Markdown")
    success = failed = 0
    for uid in users:
        try:
            await context.bot.send_message(uid, f"📢 *رسالة من البوت:*\n\n{msg}", parse_mode="Markdown")
            success += 1
        except:
            failed += 1
    await update.message.reply_text(f"✅ اكتمل!\n✅ نجح: *{success}*\n❌ فشل: *{failed}*", parse_mode="Markdown")

async def users_count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != ADMIN_ID: return
    await update.message.reply_text(f"👥 *المستخدمون:* `{len(load_users())}`", parse_mode="Markdown")

# ========== اللغة ==========
async def handle_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.split("_")[1]
    context.user_data["lang"] = lang
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(TEXTS[lang]["subscribe_btn"], url=CHANNEL_LINK)],
        [InlineKeyboardButton(TEXTS[lang]["verify_btn"], callback_data="verify_sub")],
    ])
    await query.edit_message_text(TEXTS[lang]["subscribe_required"], parse_mode="Markdown", reply_markup=keyboard)

# ========== التحقق ==========
async def verify_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = get_lang(context)
    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, query.from_user.id)
        ok = member.status in ["member","administrator","creator"]
    except:
        ok = False
    if not ok:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(TEXTS[lang]["subscribe_btn"], url=CHANNEL_LINK)],
            [InlineKeyboardButton(TEXTS[lang]["verify_btn"], callback_data="verify_sub")],
        ])
        await query.edit_message_text(TEXTS[lang]["not_subscribed"], parse_mode="Markdown", reply_markup=keyboard)
        return
    save_user(query.from_user.id)
    await query.edit_message_text(TEXTS[lang]["subscribed_ok"], parse_mode="Markdown")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(TEXTS[lang]["whatsapp"],  callback_data="service_whatsapp")],
        [InlineKeyboardButton(TEXTS[lang]["instagram"], callback_data="service_instagram")],
    ])
    await query.message.reply_text(TEXTS[lang]["choose_service"], parse_mode="Markdown", reply_markup=keyboard)

# ========== الخدمة ==========
async def handle_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data["service"] = query.data.split("_",1)[1]
    lang = get_lang(context)
    await query.edit_message_text(TEXTS[lang]["choose_country"], parse_mode="Markdown", reply_markup=country_keyboard(lang))

# ========== الدولة ==========
async def handle_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    country = query.data.split("_",1)[1]
    context.user_data["country"] = country
    service = context.user_data.get("service","whatsapp")
    nums = NUMBERS[service][country]
    chosen = random.choice(nums)
    context.user_data["current_number"] = chosen
    context.user_data["used_numbers"] = {f"{service}_{country}": [chosen]}
    await show_number(query, context)

async def show_number(query, context):
    lang = get_lang(context)
    tx = TEXTS[lang]
    number  = context.user_data.get("current_number","")
    country = context.user_data.get("country","")
    service = context.user_data.get("service","")
    text = tx["your_number"].format(
        number=number,
        country=tx.get(country, country),
        service=tx.get(service, service),
    )
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(tx["request_code"], callback_data="request_code")],
        [InlineKeyboardButton(tx["change_number"],  callback_data="change_number"),
         InlineKeyboardButton(tx["change_country"], callback_data="change_country")],
    ])
    await query.message.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)

# ========== تغيير الرقم ==========
async def change_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    service = context.user_data.get("service","whatsapp")
    country = context.user_data.get("country","germany")
    nums = NUMBERS[service][country]
    key  = f"{service}_{country}"
    used = context.user_data.get("used_numbers",{}).get(key,[])
    available = [n for n in nums if n not in used] or nums
    chosen = random.choice(available)
    context.user_data["current_number"] = chosen
    context.user_data.setdefault("used_numbers",{})[key] = used + [chosen]
    await show_number(query, context)

# ========== تغيير الدولة ==========
async def change_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = get_lang(context)
    await query.edit_message_reply_markup(None)
    await query.message.reply_text(TEXTS[lang]["choose_country"], parse_mode="Markdown", reply_markup=country_keyboard(lang))

# ========== طلب الكود ==========
async def request_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang    = get_lang(context)
    tx      = TEXTS[lang]
    number  = context.user_data.get("current_number","")
    country = context.user_data.get("country","")
    service = context.user_data.get("service","")
    code    = str(random.randint(100000,999999))
    text = tx["code_msg"].format(
        code=code,
        number=number,
        country=tx.get(country, country),
        service=tx.get(service, service),
    )
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(tx["request_code"],   callback_data="request_code")],
        [InlineKeyboardButton(tx["change_number"],  callback_data="change_number"),
         InlineKeyboardButton(tx["change_country"], callback_data="change_country")],
    ])
    await query.message.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)

# ========== تشغيل البوت ==========
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start",     start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("users",     users_count))
    app.add_handler(CallbackQueryHandler(handle_language,      pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(verify_subscription,  pattern="^verify_sub$"))
    app.add_handler(CallbackQueryHandler(handle_service,       pattern="^service_"))
    app.add_handler(CallbackQueryHandler(handle_country,       pattern="^country_"))
    app.add_handler(CallbackQueryHandler(change_number,        pattern="^change_number$"))
    app.add_handler(CallbackQueryHandler(change_country,       pattern="^change_country$"))
    app.add_handler(CallbackQueryHandler(request_code,         pattern="^request_code$"))
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
