import unittest

from src.backend.database import initial_activities


class TestActivitiesSeedData(unittest.TestCase):
    def test_manga_maniacs_activity_is_seeded_with_expected_details(self):
        self.assertIn("Manga Maniacs", initial_activities)

        manga_maniacs = initial_activities["Manga Maniacs"]
        self.assertEqual(
            manga_maniacs["description"],
            "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
        )
        self.assertEqual(manga_maniacs["schedule_details"]["days"], ["Tuesday"])
        self.assertEqual(manga_maniacs["schedule_details"]["start_time"], "19:00")
        self.assertEqual(manga_maniacs["max_participants"], 15)


if __name__ == "__main__":
    unittest.main()
