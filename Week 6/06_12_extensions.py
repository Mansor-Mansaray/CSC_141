favorite_languages = {'languages': ['rust', 'python', 'go', 'c', 'haskell'],'jen': ['python', 'rust'],
 'sarah': ['c'],'edward': ['rust', 'go'],'phil': ['python', 'haskell']}
 
pool_of_languages = [language.capitalize() for language in favorite_languages['languages']]
print(f"Pool of languages: {', '.join(pool_of_languages)}")

for name, languages in favorite_languages.items():
    if name != 'languages':
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"{language.title()}")