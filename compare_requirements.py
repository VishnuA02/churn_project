# compare_requirements.py

def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return set(line.strip() for line in f if line.strip())

colab_reqs = read_requirements("colab_requirements.txt")
django_reqs = read_requirements("django_requirements.txt")

only_in_colab = colab_reqs - django_reqs
only_in_django = django_reqs - colab_reqs

print("\n✅ Packages only in Colab:")
print("\n".join(sorted(only_in_colab)) or "None")

print("\n✅ Packages only in Django:")
print("\n".join(sorted(only_in_django)) or "None")
