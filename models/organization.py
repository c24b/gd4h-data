from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel, Field, conint, HttpUrl, EmailStr, AnyUrl
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime






from apps.user.models import UserFr
from apps.user.models import UserEn



from app.references.models import Organization_TypeEnumFrfrom app.references.models import Agent_TypeEnumFrfrom app.references.models import Agent_TypeEnumEnfrom app.references.models import Organization_TypeEnumEn



class OrganizationFr(BaseModel):
    organization_type: List[Organization_TypeEnumFr]
    acronym: Optional[str] = None
    agent_type: List[Agent_TypeEnumFr]
    image_url: Optional[HttpUrl] = None
    name: str
    url: HttpUrl
    description: Optional[str] = None
    members: List[UserFr] = []
    



class OrganizationEn(BaseModel):
    organization_type: List[Organization_TypeEnumEn]
    acronym: Optional[str] = None
    agent_type: List[Agent_TypeEnumEn]
    image_url: Optional[HttpUrl] = None
    name: str
    url: HttpUrl
    description: Optional[str] = None
    members: List[UserEn] = []
    

    