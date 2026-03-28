from enum import Enum

class ColorContrastType(Enum):
    HighContrast = "High Contrast"
    LowContrast = "Low Contrast"

class Background(Enum):
    Neutral = "Neutral"
    NonNeutral = "Non Neutral"

class ColorHarmony(Enum):
    Monochromatic = "Monochromatic"
    Achromatic = "Achromatic"
    Achromaticn1 = "Achromatic+1"
    HighContrast = "High Contrast"
    Analogous = "Analogous"
    Complementary = "Complementary"

class NormalizedDesignStrategy(Enum):
    TrustLed = "Trust-led"
    ModernMinimal = "Modern Minimal"
    HighAction = "High Action"

class PopularityBucket(Enum):
    MarketLeader = "Market Leader"
    HighGrowth = "High Growth"
    NicheSpecialized = "Niche/Specialized"

class Company:
    def __init__(self, name, total_funding_raised, navbar_collapsable, background, color_contrast, color_harmony, normalized_design_strategy, popularity_bucket):
        self.name = name
        self.total_funding_raised = total_funding_raised
        self.navbar_collapsable = navbar_collapsable
        self.background = background
        self.color_contrast = color_contrast
        self.color_harmony = color_harmony
        self.normalized_design_strategy = normalized_design_strategy
        self.popularity_bucket = popularity_bucket

    def display_info(self):
        return f"Company Name: {self.name},\n Company Total Funding: ${self.total_funding_raised},\n Company Navbar Collapsable: {self.navbar_collapsable},\n Company UI Background: {self.background},\n Company UI Color Contrast: {self.color_contrast} \n Company UI Color Harmony: {self.color_harmony}, \n Company UI Normalized Design Strategy: {self.normalized_design_strategy}, \n Company market standing: {self.popularity_bucket}"