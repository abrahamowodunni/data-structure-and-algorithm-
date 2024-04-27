class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Base case: Check if the user is in the current group
    if user in group.get_users():
        return True

    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True

    return False

# Test Case 1: User in a subgroup
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)
print(is_user_in_group("sub_child_user", parent))  # Expected output: True

# Test Case 2: User not in any group
empty_group = Group("empty_group")
print(is_user_in_group("nonexistent_user", empty_group))  # Expected output: False

# Test Case 3: Null user in a subgroup
sub_child.add_user(None)
print(is_user_in_group(None, parent))  # Expected output: True