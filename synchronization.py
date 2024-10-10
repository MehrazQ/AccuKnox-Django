def user_saved_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5) 
    print("Signal handler finished.")
def create_user():
    print("Creating user...")
    user = User.objects.create(username='testuser')
    print("User created!")
if __name__ == '__main__':
    create_user()
