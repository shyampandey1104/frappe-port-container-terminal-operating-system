import unittest
from tos.engine import ContainerTerminalOperatingEngine

class TestContainerTerminalOS(unittest.TestCase):
    def test_yard_slotting_and_demurrage(self):
        engine = ContainerTerminalOperatingEngine()
        slot = engine.assign_yard_slot(
            container_code="MSKU-982104-5",
            size_ft=40,
            iso_type="REEFER",
            vessel_id="VSSL-EVER-GIVEN-04",
            block_id="BLOCK-4A",
            bay=12,
            row=3,
            tier=4
        )
        self.assertTrue(slot.is_reefer_plugged_in)
        self.assertEqual(slot.yard_block_id, "BLOCK-4A")

        demurrage = engine.calculate_demurrage(
            container_code="MSKU-982104-5",
            dwell_days=12, # 12 days dwell vs 5 free days = 7 billable days
            free_days=5,
            rate_per_day_usd=100.0
        )
        self.assertEqual(demurrage.billable_excess_days, 7)
        self.assertEqual(demurrage.total_demurrage_usd, 700.0)
        self.assertFalse(demurrage.is_cleared_for_gate_out)

if __name__ == "__main__":
    unittest.main()
