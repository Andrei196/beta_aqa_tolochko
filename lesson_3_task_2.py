from smartphone import Smartphone

smartphone1=Smartphone("Iphone", "10", "89658741252")
smartphone2=Smartphone("Xiaomi", "5 pro", "89587456931")
smartphone3=Smartphone("samsung", "s22 ultra", "89255515547")
smartphone4=Smartphone("Nokia", "n70", "89963258247")
smartphone5=Smartphone("Honor", "70", "89654432879")

catalog=[smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]
for iprice in catalog:
    iprice.phone()