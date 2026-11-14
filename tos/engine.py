"""Port Maritime Terminal Operating System (TOS) & Yard Stacking Controller."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class ContainerSlotAssignment:
    container_iso_code: str
    container_size_feet: int  # 20 or 40
    iso_type: str  # DRY, REEFER, HAZMAT
    vessel_call_id: str
    assigned_bay: int
    assigned_row: int
    assigned_tier: int
    yard_block_id: str
    is_reefer_plugged_in: bool = False


@dataclass
class DemurrageDetentionAssessment:
    container_iso_code: str
    dwell_days_in_terminal: int
    free_days_allowed: int
    billable_excess_days: int
    daily_demurrage_usd: float
    total_demurrage_usd: float
    is_cleared_for_gate_out: bool


class ContainerTerminalOperatingEngine:
    """Manages maritime container terminal block slotting, quay crane dispatch, and dwell-time demurrage."""

    REEFER_POWER_SURCHARGE_DAILY_USD = 45.0
    DEFAULT_DEMURRAGE_RATE_USD = 85.0

    def assign_yard_slot(
        self,
        container_code: str,
        size_ft: int,
        iso_type: str,
        vessel_id: str,
        block_id: str,
        bay: int,
        row: int,
        tier: int
    ) -> ContainerSlotAssignment:
        is_reefer = iso_type == "REEFER"
        return ContainerSlotAssignment(
            container_iso_code=container_code,
            container_size_feet=size_ft,
            iso_type=iso_type,
            vessel_call_id=vessel_id,
            assigned_bay=bay,
            assigned_row=row,
            assigned_tier=tier,
            yard_block_id=block_id,
            is_reefer_plugged_in=is_reefer
        )

    def calculate_demurrage(
        self,
        container_code: str,
        dwell_days: int,
        free_days: int = 5,
        rate_per_day_usd: float = DEFAULT_DEMURRAGE_RATE_USD
    ) -> DemurrageDetentionAssessment:
        excess = max(0, dwell_days - free_days)
        total_usd = round(excess * rate_per_day_usd, 2)
        cleared = total_usd == 0.0

        return DemurrageDetentionAssessment(
            container_iso_code=container_code,
            dwell_days_in_terminal=dwell_days,
            free_days_allowed=free_days,
            billable_excess_days=excess,
            daily_demurrage_usd=rate_per_day_usd,
            total_demurrage_usd=total_usd,
            is_cleared_for_gate_out=cleared
        )
