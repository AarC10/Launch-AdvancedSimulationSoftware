from rocketpy import SolidMotor

def getCesaroniM1890():
    return SolidMotor(
        thrustSource="./EngFiles/VoidMotor.eng",
        burnOut=5.38,
        grainNumber=4,
        grainDensity=1815,
        grainOuterRadius=33 / 1000,
        grainInitialInnerRadius=15 / 1000,
        grainInitialHeight=120 / 1000,
        interpolationMethod="linear"
    )