def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")
def create_user():
    print(f"Caller thread ID: {threading.get_ident()}")
    user = User.objects.create(username='testuser')
if __name__ == '__main__':
    create_user()
