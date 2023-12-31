import unittest

from permissions import check_permission, PermissionDenied


class TestCheckPermission(unittest.TestCase):
    def test_invalid_role(self):
        with self.assertRaises(ValueError):
            check_permission('not_exist_role', {})
	
    def test_not_enough_permission(self):
        with self.assertRaises(PermissionDenied):
            check_permission('reviewer', {'edit', 'review'})

    def test_check_passed(self):
        actual = check_permission('manager', {'edit', 'review'})
        self.assertIsNone(actual)


# ROLE_PERMISSIONS = {
#     'viewer': {'view'},
#     'editor': {'view', 'edit'},
#     'reviewer': {'view', 'review'},
#     'manager': {'view', 'edit', 'review', 'publish'},
# }


# class PermissionDenied(Exception):
#     """ 権限がない場合のエラー
#     """


# def check_permission(user_role, requested_permissions):
#     """
#     ユーザーのロール(役職/役割) user_role が
#     求められた権限 requested_permissions をできるかどうか判定する。

#     user_role は文字列で、 `'viewer'` (閲覧者),
#     `'editor'` (編集者)など、仕事上の役割を表す。
#     ROLE_PERMISSIONS のキー値

#     requested_permissions は文字列の集合で、「何らかの処理に必要な権限 (複数)」を表す。
#     たとえば `{'view', 'publish'}` の場合「閲覧権限」「公開権限」を表す。

#     たとえば以下の場合「閲覧者が編集権限とレビュー権限を持つか？」とチェックできる。
#     閲覧者では権限が不十分なので `PermissionDenied` が送出される。

#     >>> check_permission('viewer', {'edit', 'review'})
#     PermissionDenied

#     権限が不足している場合 PermissionDenied 例外を送出する。
#     権限が十分な場合は何もしない。
#     存在しない role が指定された場合は ValueError を送出する
#     """
#     if user_role not in ROLE_PERMISSIONS:
#         raise ValueError('Invalid user role')

#     allowed_permissions = ROLE_PERMISSIONS[user_role]

#     if requested_permissions - allowed_permissions:
#         # 権限が不足している場合
#         raise PermissionDenied