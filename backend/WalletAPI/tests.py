from .models import Wallet, Profile
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='therealyou',
            email='test@gmail.com',
            password='test_pass'
        )
        profile = Profile.objects.get(pk=1)
        profile.last_name = "Jean"
        profile.first_name = "Dean"
        profile.verified = True
        profile.save()

        another_brick_in_the_wall = Wallet.objects.get(pk=1)
        another_brick_in_the_wall.usd_id = 14
        another_brick_in_the_wall.btc_id = 15
        another_brick_in_the_wall.save()

        cls.factory = RequestFactory()


    def test_user_mail_username(self):
        user = User.objects.get(pk=1)
        expected = f'{user.email}/{user.username}'
        self.assertEqual(expected, 'test@gmail.com/therealyou')

    def test_profile_last_name(self):
        profile = Profile.objects.get(pk=1)
        expected = f'{profile.last_name}'
        self.assertEqual(expected, 'Jean')

    def test_profile_first_name(self):
        profile = Profile.objects.get(pk=1)
        expected = f'{profile.first_name}'
        self.assertEqual(expected, 'Dean')

    def test_profile_verified(self):
        profile = Profile.objects.get(pk=1)
        expected = f'{profile.verified}'
        self.assertEqual(expected, 'True')

    def test_wallet_usd_account(self):
        wallet = Wallet.objects.get(pk=1)
        expected = f'{wallet.usd}'
        self.assertEqual(expected, '0.00')

    def test_wallet_btc_account(self):
        wallet = Wallet.objects.get(pk=1)
        expected = f'{wallet.btc}'
        self.assertEqual(expected, '0.00')

    def test_body_content(self):
        todo = Wallet.objects.get(pk=1)
        expected = f'{todo.usd_id}'
        self.assertEqual(expected, '14')

    def test_btc_id_accoun(self):
        todo = Wallet.objects.get(pk=1)
        expected = f'{todo.usd_id}'
        self.assertEqual(expected, '14')

    def test_profile_list_view(self):
        response = self.client.get(reverse('profile-list'))
        no_response = self.client.get('/author/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Dean')
