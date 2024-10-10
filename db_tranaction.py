def user_saved_handler(sender, instance, **kwargs):
    instance.username = 'modified_by_signal'
    instance.save()
    print("Signal handler executed: User modified.")
def create_user_with_rollback():
    try:
        with transaction.atomic():
            user = User.objects.create(username='original_user')
            print(f"User created: {user.username}")
            raise Exception("Forcing rollback")
    except Exception as e:
        print(f"Transaction rolled back: {e}")

if __name__ == '__main__':
    create_user_with_rollbacks()
    try:
        user = User.objects.get(username='modified_by_signal')
        print(f"User found: {user.username}")
    except User.DoesNotExist:
        print("User not found, changes rolled back.")
