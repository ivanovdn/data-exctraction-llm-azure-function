from typing import List, Optional, Union

from langchain_core.pydantic_v1 import BaseModel, Field


class FreightConfig(BaseModel):
    """Relevant information about delivery"""

    pickup_date: Optional[str] = Field(
        default=None, description="The date of pickup, if available"
    )
    pickup_time: Optional[str] = Field(
        default=None, description="The time of pickup, if available"
    )
    pickup_point: str = Field(
        description="The point of pickup", examples=["Los Angeles, Ca"]
    )
    pickup_zip: str = Field(description="The ZIP of pickup point")
    delivery_date: Optional[str] = Field(
        default=None, description="The date of delivery, if available"
    )
    delivery_time: Optional[str] = Field(
        default=None, description="The time of delivery, if available"
    )
    delivery_point: str = Field(
        description="The point of delivery", examples=["Los Angeles, Ca"]
    )
    delivery_zip: str = Field(description="The ZIP of delivery point")
    equipment_type: Optional[str] = Field(
        default=None, description="The type of equipment (trailer), if available"
    )
    weight: Optional[Union[str, float]] = Field(
        default=None, description="The weight of load, if available"
    )


class FreightConfigBakemark(BaseModel):
    """Relevant information about delivery"""

    pickup_date: Optional[str] = Field(
        default=None, description="The date of pickup, if available"
    )
    pickup_time: Optional[str] = Field(
        default=None, description="The time of pickup, if available"
    )
    delivery_date: Optional[str] = Field(
        default=None, description="The date of delivery, if available"
    )
    delivery_time: Optional[str] = Field(
        default=None, description="The time of delivery, if available"
    )
    equipment_type: Optional[str] = Field(
        default=None, description="The type of equipment (trailer), if available"
    )


class FreightConfigBakemarkImage(BaseModel):
    """Relevant information about delivery"""

    pickup_point: str = Field(
        description="The point of pickup", examples=["Los Angeles, Ca"]
    )
    pickup_zip: str = Field(description="The ZIP of pickup point")
    delivery_point: str = Field(
        description="The point of delivery", examples=["Los Angeles, Ca"]
    )
    delivery_zip: str = Field(description="The ZIP of delivery point")
    weight: Optional[Union[str, float]] = Field(
        default=None, description="The weight of load, if available"
    )


# other_requirements: Optional[list] = Field(default=[], description="Any other requirements, if available")
