from pydantic import BaseModel

class dryBean(BaseModel):
    Area : float
    Perimeter : float
    MajorAxisLength: float
    MinorAxisLength : float
    AspectRation : float
    Eccentricity : float
    ConvexArea : float
    EquivDiameter : float
    Extent : float
    Solidity : float
    roundness : float
    Compactness : float
    ShapeFactor1 : float
    ShapeFactor2 : float
    ShapeFactor3 : float
    ShapeFactor4 : float