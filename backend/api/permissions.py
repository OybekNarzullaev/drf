from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # def has_permission(self, request, view):
    #     user = request.user
    #     # barcha ruxsatlarni ko'rish
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.view_product"):
    #             return True
    #         if user.has_perm("products.add_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         return False
    #     return False
    
     # # yuqoridagi kodga teng kuchlisi
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

    # admin panelda ruxsatlar labelini customize qilish
    perms_map = {
        'GET': ['%(app_label)s.add_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
   
    
    # agar user obj ni owneri bo'lsa
    # def has_object_permission(self, request, view, obj):
    #     return obj.owner == request.user