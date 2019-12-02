# created by Seredyak1
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth import get_user_model
User = get_user_model()


class TestUserAPI(APITestCase):
    """Test for User CRUDL"""
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """Create new user nad Return 201 status code"""
        data = {"first_name": "Sanya", "email": "test@test.com", "password": "secret_password"}

        response = self.client.post('/accounts/register/', data=data, format="json")

        self.assertEqual(201, response.status_code)
        self.assertEqual(1, User.objects.count())

    #Test right data
    def test_get_user_by_if_auth_and_owner(self):
        """Return auth user and Return 200 status code"""
        self.test_create_user()
        user = User.objects.last()
        self.client.force_authenticate(user)

        response = self.client.get('/accounts/profile/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(user.email, response.data['email'])

    def test_patch_user_if_auth_and_owner(self):
        """Update auth user and Return 200 status code"""
        self.test_get_user_by_if_auth_and_owner()
        user = User.objects.last()
        data = {"first_name": "USER name", "city": "TestCity"}

        response = self.client.patch('/accounts/profile/', data=data, format="json")

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(user.first_name, response.data['first_name'])
        self.assertEqual(user.email, response.data['email'])

    def test_delete_user_if_auth_and_owner(self):
        """Return 400 status code and notification"""
        self.test_get_user_by_if_auth_and_owner()
        user = User.objects.last()

        response = self.client.delete('/accounts/profile/')

        self.assertEqual(400, response.status_code)
        self.assertEqual('Only admin can delete user', response.data['detail'])

    #Test /profile/ if user not login an profile owner
    def test_get_user_if_not_auth(self):
        """Return 401 status code"""
        self.test_create_user()
        user = User.objects.last()

        response = self.client.get('/accounts/profile/')

        self.assertEqual(401, response.status_code)

    def test_patch_user_user_if_not_auth(self):
        """Return 401 status code"""
        self.test_get_user_if_not_auth()
        user = User.objects.last()
        data = {"email": "USER name", "city": "TestCity"}

        response = self.client.patch('/accounts/profile/', data=data, format="json")
        self.assertEqual(401, response.status_code)

    #Test create/ipdate user with wrong data
    def test_create_user_with_wrong_data(self):
        """Return 400 status code and don't create new user"""
        data = {"first_name": "Sanya", "email": "testtest.com", "password": "secret_password"}

        response = self.client.post('/accounts/register/', data=data, format="json")

        self.assertEqual(400, response.status_code)
        self.assertEqual(0, User.objects.count())

    #Test user login
    def get_user_jwt_token(self):
        """Return JWT token and 200 status code"""
        self.test_create_user()
        user = User.objects.last()
        data = {'email': user.email, 'password': "secret_password"}

        response = self.client.post('/accounts/login/', data=data, format="json")

        self.assertEqual(200, response.status_code)
        self.assertEqual(True, 'token' in response.data.keys())


class TestUserGETApi(APITestCase):
    """Test user list and user detail for AllowAny"""
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(first_name="Sanya", email="test1@test.com", password="secret_password")
        self.user2 = User.objects.create(first_name="Yura", email="test2@test.com", password="secret_password")

    def get_users_list(self):
        """Return users list nad 200 status code"""
        response = self.client.get('accounts/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.data))

    def get_user_detail(self):
        """Return user detail nad 200 status code"""
        user1 = User.objects.get(email="test1@test.com")

        response = self.client.get(f'accounts/{user1.id}')

        self.assertEqual(200, response.status_code)
        self.assertEqual(user1.email, response.data['email'])
