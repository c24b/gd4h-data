from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel, Field, conint, HttpUrl, EmailStr, AnyUrl
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime






from apps.role.models import RoleEn
from apps.organization.models import OrganizationEn
from apps.organization.models import OrganizationFr
from apps.role.models import RoleFr







class UserFr(BaseModel):
    name: str
    email: str
    organization: List[OrganizationFr] = []
    role: List[RoleFr]
    



class UserEn(BaseModel):
    name: str
    email: str
    organization: List[OrganizationEn] = []
    role: List[RoleEn]
    

    