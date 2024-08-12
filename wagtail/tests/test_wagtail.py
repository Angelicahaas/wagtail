from django.test import TestCase
from wagtail import VERSION
from wagtail.templatetags.wagtailcore_tags import wagtail_feature_release_whats_new_link


class WagtailFeatureReleaseWhatsNewLinkTest(TestCase):

    def test_wagtail_feature_release_whats_new_link_final(self):
        # Simulando uma versão final do Wagtail
        with self.settings(WAGTAIL_VERSION=(6, 1, 2, 'final', 0)):
            major, minor, patch, release, num = (6, 1, 2, 'final', 0)
            expected_url = f"https://guide.wagtail.org/en-{major}.{minor}.x/releases/new-in-wagtail-{major}-{minor}/"
            result = wagtail_feature_release_whats_new_link()
            self.assertEqual(result, expected_url)

    def test_wagtail_feature_release_whats_new_link_non_final(self):
        # Simulando uma versão não final do Wagtail
        with self.settings(WAGTAIL_VERSION=(6, 1, 2, 'beta', 1)):
            expected_url = "https://guide.wagtail.org/en-latest/releases/latest/"
            result = wagtail_feature_release_whats_new_link()
            self.assertEqual(result, expected_url)
