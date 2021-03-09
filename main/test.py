from account.models import Account

# account = Account.objects.find_all(
#     {Account.role: 'chef_projet'},
#     {Account.last_name: 1, Account.first_name: 1, Account._id: 0}
# )

all_chef_proj = Account.objects.get(role="chef_projet")
print(all_chef_proj)
