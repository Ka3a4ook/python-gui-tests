from model.group import Group
import random


def test_delete_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    random_group = random.choice(app.groups.get_group_list())
    app.groups.delete_group(random_group)
    new_list = app.groups.get_group_list()
    old_list.remove(random_group)
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)
