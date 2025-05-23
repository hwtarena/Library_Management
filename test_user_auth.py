import unittest
import user_auth # The module to test

class TestUserAuth(unittest.TestCase):

    def setUp(self):
        """This method is called before each test."""
        # Reset user_data before each test to ensure test isolation
        user_auth.user_data.clear() 

    def test_register_user_success(self):
        """Test successful registration of a new user."""
        success, message = user_auth.register_user("testuser", "password123", user_auth.user_data)
        self.assertTrue(success)
        self.assertEqual(message, "Registration successful.")
        self.assertIn("testuser", user_auth.user_data)
        self.assertEqual(user_auth.user_data["testuser"], ("password123",))

    def test_register_user_already_exists(self):
        """Test registration if username already exists."""
        user_auth.register_user("testuser", "password123", user_auth.user_data) # First registration
        success, message = user_auth.register_user("testuser", "anotherpassword", user_auth.user_data) # Attempt to re-register
        self.assertFalse(success)
        self.assertEqual(message, "Username already exists.")
        # Ensure the original password was not overwritten
        self.assertEqual(user_auth.user_data["testuser"], ("password123",))

    def test_login_user_success(self):
        """Test successful login with correct credentials."""
        user_auth.register_user("testuser", "password123", user_auth.user_data)
        success, message = user_auth.login_user("testuser", "password123", user_auth.user_data)
        self.assertTrue(success)
        self.assertEqual(message, "Login successful.")

    def test_login_user_incorrect_password(self):
        """Test login with correct username but incorrect password."""
        user_auth.register_user("testuser", "password123", user_auth.user_data)
        success, message = user_auth.login_user("testuser", "wrongpassword", user_auth.user_data)
        self.assertFalse(success)
        self.assertEqual(message, "Invalid username or password.")

    def test_login_user_non_existent_username(self):
        """Test login with a username that does not exist."""
        success, message = user_auth.login_user("nonexistentuser", "password123", user_auth.user_data)
        self.assertFalse(success)
        self.assertEqual(message, "Invalid username or password.")

    def test_login_user_empty_user_data(self):
        """Test login when the user_data dictionary is empty."""
        success, message = user_auth.login_user("testuser", "password123", user_auth.user_data)
        self.assertFalse(success)
        self.assertEqual(message, "Invalid username or password.")

    def test_password_is_tuple(self):
        """Verify that the password is stored as a tuple."""
        user_auth.register_user("tupleuser", "securepass", user_auth.user_data)
        self.assertIsInstance(user_auth.user_data["tupleuser"], tuple)
        self.assertEqual(len(user_auth.user_data["tupleuser"]), 1)
        self.assertEqual(user_auth.user_data["tupleuser"][0], "securepass")

if __name__ == '__main__':
    unittest.main()
