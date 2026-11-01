"""Simple rules used when the LLM is down or returns something unusable.

Works offline, so it plays the role a local datasource plays in the app.
"""

from app.features.outfit.data.model.outfit_model import OutfitModel
from app.features.outfit.domain.params.outfit_params import OutfitParams

_TEXT = {
    "en": {
        "top_cold": "Warm sweater",
        "top_mild": "Long-sleeve shirt",
        "top_hot": "T-shirt",
        "bottom_cold": "Long trousers",
        "bottom_hot": "Shorts or light trousers",
        "shoes_rain": "Waterproof boots",
        "shoes_hot": "Sandals or light sneakers",
        "shoes_default": "Sneakers",
        "jacket": "Jacket",
        "reason": "Basic suggestion based on temperature and rain chance.",
    },
    "ar": {
        "top_cold": "كنزة دافية",
        "top_mild": "قميص بكم طويل",
        "top_hot": "تيشيرت",
        "bottom_cold": "بنطلون طويل",
        "bottom_hot": "شورت أو بنطلون خفيف",
        "shoes_rain": "بوط مقاوم للمي",
        "shoes_hot": "صندل أو سنيكرز خفيف",
        "shoes_default": "سنيكرز",
        "jacket": "جاكيت",
        "reason": "اقتراح أساسي حسب الحرارة واحتمال المطر.",
    },
}


class OutfitLocalDataSource:
    def suggest_outfit(self, params: OutfitParams) -> OutfitModel:
        weather = params.weather
        text = _TEXT[params.lang]
        feels = weather.feels_like
        rainy = weather.rain_chance > 40

        if feels < 10:
            top, bottom = text["top_cold"], text["bottom_cold"]
        elif feels < 22:
            top, bottom = text["top_mild"], text["bottom_cold"]
        else:
            top, bottom = text["top_hot"], text["bottom_hot"]

        if rainy:
            shoes = text["shoes_rain"]
        elif feels >= 22:
            shoes = text["shoes_hot"]
        else:
            shoes = text["shoes_default"]

        return OutfitModel(
            top=top,
            bottom=bottom,
            shoes=shoes,
            jacket=text["jacket"] if feels < 10 else None,
            umbrella=rainy,
            sunscreen=weather.condition == "Clear" and weather.temp_max >= 20,
            reason=text["reason"],
        )
