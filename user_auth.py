user_data = {}

def register_user(username: str, password: str, user_data_dict: dict) -> tuple[bool, str]:
  """Registers a new user."""
  if username in user_data_dict:
    return (False, "Username already exists.")
  else:
    user_data_dict[username] = (password,)
    return (True, "Registration successful.")

def login_user(username: str, password: str, user_data_dict: dict) -> tuple[bool, str]:
  """Logs in an existing user."""
  if username not in user_data_dict:
    return (False, "Invalid username or password.")
  else:
    stored_pw_tuple = user_data_dict[username]
    if password == stored_pw_tuple[0]:
      return (True, "Login successful.")
    else:
      return (False, "Invalid username or password.")
