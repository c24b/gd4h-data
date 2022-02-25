from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel, Field, conint, HttpUrl, EmailStr, AnyUrl
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime






from apps.comment.models import Comment
from apps.organization.models import OrganizationFr
from apps.dataset.models import DatasetFr
from apps.dataset.models import DatasetEn
from apps.organization.models import OrganizationEn

class DatasetFr(BaseModel):
    integration_status: Optional[bool] = None
    state: Optional[bool] = None
    last_inserted: Optional[datetime] = None
    last_modification: Optional[datetime] = None
    name: str
    acronym: Optional[str] = None
    organizations: List[OrganizationFr]
    description: str
    url: HttpUrl
    contact_type: List[str] = []
    contact: List[str] = []
    contact_type_comments: List[Comment] = []
    dataset_type: str
    environment: List[str] = []
    nature: Optional[str] = None
    subthematic: List[str] = []
    exposure_factor: List[str] = []
    exposure_factor_category: List[str]
    theme_category: Optional[str] = None
    is_opendata: bool
    license_name: Optional[str] = None
    license_type: List[str] = []
    has_restrictions: Optional[bool] = None
    restrictions_comments: List[Comment] = []
    has_pricing: Optional[bool] = None
    has_compliance: Optional[bool] = None
    pricing_comments: List[Comment] = []
    compliance_comments: List[Comment] = []
    data_format: List[str] = []
    other_access_points: List[str] = []
    data_domain: str
    related_referential: List[str] = []
    related_datasets: List[DatasetFr] = []
    automatic_update: Optional[bool] = None
    broadcast_mode: List[str] = []
    documentation_comments: List[Comment] = []
    last_updated: Optional[datetime] = None
    downloadable: Optional[bool] = None
    has_documentation: Optional[bool] = None
    has_filter: Optional[bool] = None
    has_missing_data: Optional[bool] = None
    has_search_engine: Optional[bool] = None
    missing_data_comments: List[Comment] = []
    technical_comments: List[Comment] = []
    temporal_scale: List[str] = []
    update_frequency: Optional[str] = None
    volume: Optional[str] = None
    year: List[str] = []
    is_geospatial_data: Optional[bool] = None
    administrative_territory_coverage: List[str] = []
    geographical_information_level: List[str] = []
    projection_system: List[str] = []
    related_geographical_information: Optional[bool] = None
    geographical_geospatial_coverage: List[str] = []
    geospatial_comments: List[Comment] = []
    comments: List[Comment] = []
    qualification_comments: List[Comment] = []
    context_comments: List[Comment] = []
    



class DatasetEn(BaseModel):
    integration_status: Optional[bool] = None
    state: Optional[bool] = None
    last_inserted: Optional[datetime] = None
    last_modification: Optional[datetime] = None
    name: str
    acronym: Optional[str] = None
    organizations: List[OrganizationEn]
    description: str
    url: HttpUrl
    contact_type: List[str] = []
    contact: List[str] = []
    contact_type_comments: List[Comment] = []
    dataset_type: str
    environment: List[str] = []
    nature: Optional[str] = None
    subthematic: List[str] = []
    exposure_factor: List[str] = []
    exposure_factor_category: List[str]
    theme_category: Optional[str] = None
    is_opendata: bool
    license_name: Optional[str] = None
    license_type: List[str] = []
    has_restrictions: Optional[bool] = None
    restrictions_comments: List[Comment] = []
    has_pricing: Optional[bool] = None
    has_compliance: Optional[bool] = None
    pricing_comments: List[Comment] = []
    compliance_comments: List[Comment] = []
    data_format: List[str] = []
    other_access_points: List[str] = []
    data_domain: str
    related_referential: List[str] = []
    related_datasets: List[DatasetEn] = []
    automatic_update: Optional[bool] = None
    broadcast_mode: List[str] = []
    documentation_comments: List[Comment] = []
    last_updated: Optional[datetime] = None
    downloadable: Optional[bool] = None
    has_documentation: Optional[bool] = None
    has_filter: Optional[bool] = None
    has_missing_data: Optional[bool] = None
    has_search_engine: Optional[bool] = None
    missing_data_comments: List[Comment] = []
    technical_comments: List[Comment] = []
    temporal_scale: List[str] = []
    update_frequency: Optional[str] = None
    volume: Optional[str] = None
    year: List[str] = []
    is_geospatial_data: Optional[bool] = None
    administrative_territory_coverage: List[str] = []
    geographical_information_level: List[str] = []
    projection_system: List[str] = []
    related_geographical_information: Optional[bool] = None
    geographical_geospatial_coverage: List[str] = []
    geospatial_comments: List[Comment] = []
    comments: List[Comment] = []
    qualification_comments: List[Comment] = []
    context_comments: List[Comment] = []
    

    